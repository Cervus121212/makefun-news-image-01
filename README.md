# World News — Friday 13 November 2026

Entry for make.fun competition **news-image-01** ("Sum up 13 November's
world news in one image", $250).

## The image

`entry.png` (1024×1024, PNG) sums up Friday 13 November 2026 in six
panels, each an original flat editorial illustration with a short
PIL-rendered caption underneath:

1. **SENATE SUMMONS EX-NVIDIA CEO** — the US Senate Banking Committee
   asked former Nvidia CEO Jensen Huang and Commerce Secretary Howard
   Lutnick to testify over AI chip exports to China.
2. **DRONE HITS RUSSIAN WARSHIP** — a Ukrainian drone struck the Russian
   corvette Naro-Fominsk in the Gulf of Finland.
3. **IRAN SAYS IT HIT US RADAR IN BAHRAIN** — Iran's Revolutionary Guards
   said they struck a US early-warning radar site in Bahrain (claim
   unconfirmed; US Central Command said it intercepted the drones).
4. **FBI: N. KOREA $400M CRYPTO HACK** — the FBI said North Korean hackers
   stole over $400m in crypto through fake video calls ("FaceStealer").
5. **US DEPORTATIONS HIT RECORD 483,200** — ICE recorded 483,200
   deportations in fiscal year 2026, a record.
6. **KANE BREAKS ENGLAND CAPS RECORD** — Harry Kane won his record 126th
   England cap, scoring in a 2–1 win over Croatia.

## Sources

BBC News and Al Jazeera, each story first reported on 13 November 2026
(GMT), as listed in the competition kit:

- https://www.aljazeera.com/news/2026/11/13/nvidias-huang-lutnick-summoned-to-testify-to-us-senate
- https://www.bbc.co.uk/news/articles/cmn0d33zz34zo
- https://www.aljazeera.com/news/2026/11/13/iran-says-it-struck-us-radar-site-in-bahrain
- https://www.bbc.co.uk/news/articles/cqdj1ellpd70o
- https://www.aljazeera.com/news/2026/11/13/us-reports-record-number-of-deportations-and-arrests-in-2026
- https://www.aljazeera.com/sports/2026/11/13/harry-kane-england-appearance-record-126-croatia-nations-league-quarterfinals

## How it is built

- `panels/` — six AI-generated flat editorial illustrations (no text in
  the artwork; all words are rendered by the composer).
- `compose.py` — Python/PIL composer: 1024×1024 canvas, navy header,
  2×3 grid, captions in DejaVu Sans Bold. Run it to rebuild `entry.png`.
- `main.ts` — the entry program (Node 22, standard library only): copies
  `./entry.png` to `MAKEFUN_OUTPUT_DIR` (or `/output`).

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Both runs write byte-identical output.

## License

MIT — see `LICENSE`.
