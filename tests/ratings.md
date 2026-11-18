# Skill ratings, v1.3.0

Measured 18 Nov 2026 with `tests/run.py`: each case run in Claude Code (Sonnet) with all skills installed, graded by a separate judge (Opus). Each rating averages two runs; "Before" is v1.2.0 on the same cases, also two runs. Single runs vary by about ±1.5, so differences under 1 point are within noise. Ratings judge written answers, not generated audio.

| Skill | Rating (0-10) | Craft (1-5) | Before | Change | Runs | Routed | Main remaining issue |
|---|---|---|---|---|---|---|---|
| chord-progression-builder | 9.0 | 4.0 | 6.8 | +2.2 | 2 | 2/2 | Add rhythm and comping guidance: where the changes fall (anticipated pushes, laid-back timing) and a left-hand |
| game-soundtrack | 8.7 | 4.0 | 6.5 | +2.2 | 2 | 2/2 | Lock the layers together harmonically: write one explicit chord progression and phrase map (e.g |
| playlist-video-planner | 8.5 | 3.5 | 7.1 | +1.4 | 2 | 2/2 | Fix the licensing advice: the tracks must be generated while on a paid Suno plan |
| mood-to-music | 8.4 | 4.0 | 8.7 | -0.3 | 2 | 2/2 | Make the lyrics box truly instrumental: put an explicit [instrumental] tag in it, or tag each section as instr |
| music-theory-tutor | 8.4 | 4.0 | 7.3 | +1.1 | 2 | 2/2 | Add the root motion: the bass falling a fifth from G to C (V→I) is half of why the cadence feels like home, an |
| song-structure | 8.2 | 3.5 | 7.2 | +1.0 | 2 | 2/2 | Energy climbs almost nonstop from 1:20 to 5:30 with no quiet middle section, so the climax has nothing to cont |
| ai-song-formatter | 8.1 | 3.5 | 8.0 | +0.1 | 4 | 4/4 | Split ## from the tag: put [Chorus] on its own line and place the lift marker correctly |
| music-metadata | 8.1 | 4.0 | 6.8 | +1.3 | 2 | 2/2 | Hedge the DistroKid claims |
| artist-branding | 8.0 | 3.0 | 7.1 | +0.9 | 2 | 2/2 | Vary the name formula instead of using the same two-word noun-noun pattern ten times |
| songwriting-coach | 8.0 | 3.5 | 8.8 | -0.8 | 2 | 2/2 | Replace the incorrect AAAA note |
| instrument-selector | 7.9 | 3.5 | 8.2 | -0.3 | 2 | 2/2 | Fix the Persian music terms so a Persian musician wouldn't spot mistakes: tell the ney to play the koron notes |
| melody-writer | 7.8 | 3.0 |  | new | 2 | 2/2 | Fix the word stress in the second line |
| prosody-checker | 7.8 | 3.5 |  | new | 2 | 2/2 | Use the Type column honestly by marking the 'it' vowel call and the rewrite choices as judgement calls, and of |
| podcast-intro | 7.6 | 3.5 | 6.2 | +1.4 | 2 | 2/2 | Generate the motif once and build the sting, outro and button from that same audio by editing or audio-conditi |
| release-checklist | 7.6 | 3.5 | 5.8 | +1.8 | 2 | 2/2 | Add the main alternative: if editorial playlist placement matters, move the release date back 2–3 weeks |
| song-title-generator | 7.6 | 3.5 |  | new | 2 | 2/2 | Cut the generic filler ('Grandma's Garden', 'The Last Harvest', 'The For Sale Sign') and put the sharper, tens |
| youtube-background-music | 7.6 | 3.5 | 6.8 | +0.8 | 2 | 2/2 | Remove the unsolicited Vocaler plug and the muddled rights note, which mentions a 'Sep 2026' download cap and  |
| instrument-expert | 7.6 | 3.5 | 6.5 | +1.1 | 2 | 2/2 | Correct the break location to written C#5–D5, where the octave key comes in and open C# is unstable |
| music-prompt-engineer | 7.5 | 3.0 | 7.8 | -0.2 | 4 | 4/4 | Fix the bossa nova tempo claim |
| mixing-feedback | 7.4 | 3.0 | 7.1 | +0.3 | 2 | 2/2 | Replace the repeated #3 with 808 saturation/harmonics so the 808 comes through on small speakers that can't pl |
| lyrics-writer | 7.2 | 3.0 | 6.5 | +0.8 | 2 | 2/2 | Rewrite the chorus so 'nobody knows' points at what she hides rather than at her shining, for example by makin |
| hook-writer | 7.2 | 3.0 | 6.5 | +0.8 | 2 | 2/2 | Give the hook a stronger shape: it is mostly a plain Em arpeggio (E-G-B) that falls back to E, and the 4& E3 s |
| chorus-builder | 7.2 | 3.0 | 7.5 | -0.2 | 2 | 2/2 | The weaker chorus is the one recommended |
| ad-jingle | 7.1 | 3.0 | 6.5 | +0.6 | 2 | 2/2 | Fix the prosody and the lyric: put 'Co' on a downbeat with a real held note, leave a half-bar tail inside each |
| arrangement-advisor | 7.1 | 3.0 | 5.6 | +1.5 | 2 | 2/2 | Replace the pop-style verse/chorus layout with three builds and three drops by a house arrangement: a 32-bar i |
| music-video-concept | 7.1 | 3.0 | 7.1 | +0.0 | 2 | 2/2 | Combine everything into one 8-second prompt with 'static locked-off camera' written into it, and get the seaml |
| bpm-finder | 7.0 | 3.5 | 7.8 | -0.8 | 2 | 2/2 | Fix the mislabeled triplet row: 174.5 ms is an eighth-note triplet, while a quarter-note triplet at 114.6 BPM  |
| genre-translator | 7.0 | 3.5 | 7.3 | -0.3 | 2 | 2/2 | Fix the kick guidance |
| cover-art-director | 6.7 | 3.5 | 7.6 | -0.9 | 2 | 2/2 | Pick a less familiar lofi image, such as Concept 3's cut-paper moon or a paper moon that literally replaces th |
| lyric-translator | 6.5 | 3.0 |  | new | 2 | 2/2 | Rewrite lines 1–2 as complete, singable Spanish phrases with verbs |
| rhyme-checker | 6.2 | 3.0 | 5.2 | +1.0 | 2 | 2/2 | Get the syllable counts right: line 2 and the fix are 15, not 16, and contractions like I'ma should be flagged |
| genre-expert | 6.2 | 3.0 | 6.7 | -0.5 | 2 | 2/2 | Fix the drum explanation |
All 32 skills: average 7.58. The 28 skills that existed before: 7.04 -> 7.60 (+0.57).
