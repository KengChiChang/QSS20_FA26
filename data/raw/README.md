# Where the raw data come from

All files here are unmodified copies of the teaching data for Kosuke Imai's
*Quantitative Social Science*, from the `qsspy` repository
(<https://github.com/jeffallen13/qsspy>, commit `ad86b19`, GPL-2.0).

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
