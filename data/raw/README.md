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
| `face.csv` | one US Senate race, 2000 to 2006: winner, loser, parties, votes, and the share of experiment subjects who judged each candidate the more competent face (Todorov et al. 2005) | lecture 13 |
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

## Voteview roll calls (lecture 14)

`voteview/` holds the Voteview files that lecture 14 and its activity read,
saved by `QSS20_book/scripts/fetch_lec14_voteview.py` from
<https://voteview.com/data>: the 80th House (1947 to 1948) files on 2026-10-27 at 17:09 and
the rest that day at 21:18 (Pacific). `source-record.json` lists each URL, retrieval
time (UTC), and status. A rerun of the script keeps the files already saved.

| File | One row is | Used in |
|---|---|---|
| `HSall_members.csv.gz` | one member in one Congress and chamber (House, Senate, or President), every Congress through the 119th, with party, state, and the DW-NOMINATE positions `nominate_dim1` and `nominate_dim2` | lecture 14 |
| `H113_votes.csv.gz` to `H119_votes.csv.gz` | one member's vote on one roll call in that House (`cast_code`: 1 to 3 yea, 4 to 6 nay, 7 to 9 present or not voting) | lecture 14 |
| `H118_rollcalls.csv` | one recorded vote of the 118th House, with its date, bill number, question, result, and description (`vote_desc`; `dtl_desc` is empty for this House) | lecture 14 |
| `H080_members.csv`, `H080_rollcalls.csv`, `H080_votes.csv.gz` | the same three kinds of row for the 80th House | the lecture 14 activity |

The `.gz` files are gzip-compressed; `pd.read_csv` reads them directly. The votes
files also carry the president's positions on some roll calls; keep the members
whose `chamber` is `House`. The 119th House (2025 to 2026) was still in session on
2026-10-27, so its votes and positions are a snapshot as of that day. The
DW-NOMINATE scores here are a later release than those in `congress.csv`, which
ends with the 112th Congress (correlation 0.98 for the 90th House, checked
2026-10-27). Cite as: Lewis, Jeffrey B., Keith Poole, Howard Rosenthal, Adam
Boche, Aaron Rudkin, and Luke Sonnet (2026). *Voteview: Congressional Roll-Call
Votes Database*. <https://voteview.com/>. The site states no data license; its
data page says the release "is provided without warranty."
