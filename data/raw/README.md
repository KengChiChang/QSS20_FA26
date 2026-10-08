# Where the raw data come from

The files at the top level are unmodified copies of the teaching data for
Kosuke Imai's *Quantitative Social Science*, from the `qsspy` repository
(<https://github.com/jeffallen13/qsspy>, commit `ad86b19`, GPL-2.0). The
folders `pokemon/`, `nyc/`, `mlb/`, `wikipedia/`, and `quotes/` hold API
responses and web pages saved for lectures 8 to 10; see the second table below.

| File | One row is | Used in |
|---|---|---|
| `congress.csv` | one member of the House, or a president, in one Congress (80th–112th), with DW-NOMINATE scores | lectures 4 to 6 |
| `federalist/` | one Federalist essay per text file | lectures 2 and 3 |
| `FLVoters.csv` | one registered Florida voter: surname, county, voting district, age, gender, race | lectures 6 and 7 |
| `names.csv` | one surname from the 2000 Census list of surnames held by at least 100 people, with the percentage of people in each group | lecture 7 |
| `FLCensusVTD.csv` | one Florida voting district (county, VTD), with its population and the share of residents in each group | lecture 7 |

The Florida and surname files accompany Imai, K., and Khanna, K. (2016),
"Improving Ecological Inference by Predicting Individual Ethnicity from Voter
Registration Records," *Political Analysis* 24(2): 263–272.

Read `FLVoters.csv` with `keep_default_na=False, na_values=['NA']` and
`names.csv` with `keep_default_na=False`: `NULL` is a real surname.

## Saved API responses and web pages (lectures 8 to 10)

Each folder holds the response bodies exactly as the server sent them, and a
`source-record.json` with each request's full URL, UTC retrieval time, status,
and User-Agent (the instructor's contact details removed). All were saved on 2026-10-08 (UTC) by
`QSS20_book/scripts/fetch_lec08_10_data.py`. None needed an API key.

| Folder | One file is | Source and terms | Used in |
|---|---|---|---|
| `pokemon/` | one PokeAPI resource: `pikachu.json` (one Pokémon), `type-water.json` (one type) | PokeAPI, <https://pokeapi.co>; free, no key | lecture 8 |
| `nyc/` | `fatal-crashes-page-N.json`: up to 1,000 police-reported crashes that killed at least one person, 16 columns; `deaths-by-year.json`: crashes and deaths per year, counted by the server; `persons-killed-page-N.json`: up to 1,000 people killed, one row per person; `fatal-crash-vehicles-batch-N.json`: the vehicles in up to 200 of the fatal crashes | NYC Open Data, Motor Vehicle Collisions: Crashes (<https://data.cityofnewyork.us/d/h9gi-nx95>), Persons (`f55k-p6yu`), and Vehicles (`bm4k-52h4`); NYC Open Data terms of use | lectures 8 and 10 |
| `mlb/` | `teams-hitting-YYYY.json`: hitting totals for all 30 teams in one season, 2015 to 2025 | MLB Stats API (<https://statsapi.mlb.com>); MLB Advanced Media, individual non-commercial use | lecture 8 activity |
| `wikipedia/` | one saved article page: `us-traffic-deaths.html` ("Motor vehicle fatality rate in U.S. by year"), `nyc-boroughs.html` ("Boroughs of New York City"), `vision-zero.html` ("Vision Zero"); plus `robots.txt` | Wikipedia; text under CC BY-SA 4.0; Wikimedia asks programs to send a User-Agent with contact information | lecture 9 and its activity |
| `quotes/` | `page-1.html`, the first page of a site built for scraping practice; `robots.txt` (the site has none: status 404) | Quotes to Scrape (<https://quotes.toscrape.com>) | lecture 9 |

The NYC API writes numbers and dates as text and leaves a field out of a
record when it has no value. The snapshot's last crash is dated 2026-05-04;
the persons table runs to 2026-06-09.

Lecture 9 writes two derived tables to `data/derived/`: `us_traffic_deaths.csv`
(one row per year, 1899 to 2025, parsed from `wikipedia/us-traffic-deaths.html`)
and `nyc_boroughs.csv` (one row per borough, 2020 Census population, parsed from
`wikipedia/nyc-boroughs.html`). Lecture 10 builds `data/derived/traffic.duckdb`
from these files; Git ignores it.
