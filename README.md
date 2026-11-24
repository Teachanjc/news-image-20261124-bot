[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Teachanjc/news-image-20261124-bot/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Teachanjc/news-image-20261124-bot/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# news-image-20261124-bot

A newspaper front page summing up the world's news of Tuesday 24 November 2026 in one image: Israeli strikes killing Hamas security chief Naeem Abu Nahel in Gaza City, a Russian overnight attack on Zaporizhzhia killing two and wounding 40, foreign jets entering South Korea's air defence zone, US states suing Musk companies over sexualised images made with Grok, and JD Vance lobbying Nvidia's board to bring back Jensen Huang.

The image is drawn programmatically with Pillow (fixed fonts, fixed text, no network, no randomness) and shipped as `entry.png`; `main.py` copies it to `/output/entry.png`, so two runs produce byte-identical output.

## The five stories

1. **Gaza — Hamas security chief killed.** Israeli airstrikes on Tuesday killed Naeem Abu Nahel, director of Hamas' internal security apparatus, and six others, including two police officers, medics and police said. Earlier strikes in Khan Younis and near the Netzarim corridor killed six more people.
2. **Ukraine war, Zaporizhzhia — overnight attack kills two.** A Russian overnight attack struck an apartment building in Zaporizhzhia, killing two people and wounding 40, including four children, the regional governor said.
3. **Korea — jets enter the air defence zone.** Several Russian aircraft flew inside South Korea's air defence identification zone over waters between the Korean Peninsula and Japan, Seoul said, after island residents were told to take shelter.
4. **United States, AI — states sue over Grok images.** Oregon and Virginia sued Musk companies over sexualised images made with Grok, the latest legal fight over the chatbot.
5. **Business, Nvidia — Vance lobbied the board.** Trump and Vance pressed Nvidia's board over the weekend to reinstate Jensen Huang, who was brought back as chief executive on Monday, less than two weeks after he resigned.

The black strip at the foot adds three more items reported that day: NATO vowing to defend space after reports of a Russian nuclear-armed satellite, Trump moving to order faster federal death sentences, and the UK sanctioning five Myanmar generals after the ICJ genocide ruling.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
