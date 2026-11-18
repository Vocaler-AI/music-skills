"""Regression checks for the generated site's search and asset contracts."""

import importlib.util
import json
import pathlib
import re
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from datetime import datetime
from html.parser import HTMLParser
from urllib.parse import urlsplit


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "site"))
spec = importlib.util.spec_from_file_location("music_site", ROOT / "site" / "build.py")
site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site)


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.links = []
        self.meta = {}
        self.headings = []
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if tag == "link":
            self.links.append(attributes)
        elif tag == "meta":
            self.meta[attributes.get("name") or attributes.get("property")] = attributes.get("content")
        elif tag in ("h1", "h2", "h3", "h4"):
            self.headings.append(int(tag[1]))


class SiteSEOTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.public = pathlib.Path(cls.temp.name) / "public"
        site.build_pages(cls.public, "", False)
        cls.sitemap = ET.parse(cls.public / "sitemap.xml").getroot()
        cls.urls = [node.text for node in cls.sitemap.findall(".//{*}loc")]

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_sitemap_contains_each_public_page_once(self):
        expected = {site.BASE + path for path in ("/", "/install/", "/models/")}
        expected.update(f"{site.BASE}/{category['slug']}/" for category in site.CAT.values())
        expected.update(f"{site.BASE}/{skill['name']}/" for skill in site.SKILLS)
        self.assertEqual(set(self.urls), expected)
        self.assertEqual(len(self.urls), len(expected))

    def test_indexable_pages_have_matching_canonicals_and_available_assets(self):
        for url in self.urls:
            with self.subTest(url=url):
                path = self.public / urlsplit(url).path.lstrip("/") / "index.html"
                source = path.read_text()
                page = Page(source)
                self.assertEqual([link["href"] for link in page.links if link.get("rel") == "canonical"], [url])
                self.assertNotIn("noindex", page.meta.get("robots", ""))
                self.assertEqual(page.headings.count(1), 1)
                self.assertEqual(page.meta["og:url"], url)
                self.assertEqual(page.meta["twitter:card"], "summary_large_image")
                for image in ("og:image", "twitter:image"):
                    self.assertTrue(page.meta[image].startswith(site.BASE + "/assets/"))
                    self.assertTrue((self.public / urlsplit(page.meta[image]).path.lstrip("/")).is_file())
                for link in page.links:
                    if link.get("rel") in ("icon", "stylesheet", "preload"):
                        self.assertTrue((self.public / link["href"].lstrip("/")).is_file())
                self.assertNotIn("fonts.googleapis.com", source)

    def test_category_headings_follow_the_page_hierarchy(self):
        for category in site.CAT.values():
            page = Page((self.public / category["slug"] / "index.html").read_text())
            for previous, current in zip(page.headings, page.headings[1:]):
                self.assertLessEqual(current, previous + 1)

    def test_error_template_is_noindex_and_has_no_canonical(self):
        page = Page((self.public / "404.html").read_text())
        self.assertIn("noindex", page.meta["robots"])
        self.assertFalse([link for link in page.links if link.get("rel") == "canonical"])

    def test_model_dates_share_the_review_date(self):
        expected = datetime.strptime(site.MODELS_CHECKED, "%d %b %Y").date().isoformat()
        model_url = next(node for node in self.sitemap if node.find("{*}loc").text.endswith("/models/"))
        self.assertEqual(model_url.find("{*}lastmod").text, expected)
        source = (self.public / "models" / "index.html").read_text()
        graph = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', source).group(1))
        article = next(node for node in graph["@graph"] if node.get("@type") == "TechArticle")
        self.assertEqual(article["dateModified"], expected)

    def test_internal_preview_keeps_asset_paths_and_noindex(self):
        preview = pathlib.Path(self.temp.name) / "preview"
        site.build_pages(preview, "/music-skills", True)
        page = Page((preview / "index.html").read_text())
        self.assertIn("noindex", page.meta["robots"])
        for link in page.links:
            if link.get("rel") in ("icon", "stylesheet", "preload"):
                self.assertTrue(link["href"].startswith("/music-skills/"))
                self.assertTrue((preview / link["href"].removeprefix("/music-skills/")).is_file())
        self.assertFalse((preview / "sitemap.xml").exists())


if __name__ == "__main__":
    unittest.main()
