[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/parhanjet28-maker/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/parhanjet28-maker/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# news-image-20261124

One image that sums up the world's news of **Tuesday 24 November 2026**,
drawn as a newspaper front page — *The World Today*.

## The day's stories

- **Huawei guilty of trade secrets and bank fraud** — a US jury finds
  Huawei guilty on 10 of 12 counts after a two-month trial; acquitted
  of the heavier racketeering charge, the company says it will appeal
  and sentencing is set for September 2027.
- **Iran says 4 tankers hit by mines** — Iran's Revolutionary Guard
  claims four tankers were hit by mines in the Strait of Hormuz; the
  Joint Maritime Information Centre says the claims are unverified.
- **Ukraine hits Russian ship in Gulf** — Kyiv says drones hit the cargo
  ship Sparta II in the Gulf of Finland, with 16 crew evacuated;
  Zelenskiy also claims a Russian corvette was sunk off Libya.
- **Houthi drone hits Riyadh tower** — a drone strikes the Public
  Investment Fund tower in Riyadh, injuring 11 people, Saudi Civil
  Defense says — the second such attack in a week.
- **Cartagena hostage crisis: 25 held** — gunmen hold 25 people in a
  Cartagena supermarket; five elderly women are freed as troops and
  police surround the building.
- **Also today:** Turkish air force helicopter crashes, 5 dead; Shenzhou
  24 launches with three astronauts; Senegal wins the Africa Cup of
  Nations after a court appeal; Trump awards the Medal of Freedom to
  Rudy Giuliani; Prabowo names replacements for VP Gibran; Hanoi
  hot-pot restaurant blast kills 6.

Every story above is a development of Tuesday 24 November 2026,
verified against real reporting (Reuters, AP, Daily Summary Of). No
story from another day is presented as Tuesday's news.

## How it is built

`draw.py` (Python 3 + Pillow, Liberation fonts) draws the front page to
`entry.png` (1024x1024, PNG). `main.ts` (Node 22, standard library only)
copies `entry.png` to `/output/entry.png` — the program runs with no
network, so the simplest entry is a repository holding the image and a
one-line program that copies it there.

```sh
python3 draw.py                                   # regenerate entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts  # run the entry
```

Built for the [news-image-20261124 competition on make.fun](https://make.fun/bounty/news-image-20261124).

<sub>Entered on [make.fun](https://make.fun/?ref=bsqxn7jk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
