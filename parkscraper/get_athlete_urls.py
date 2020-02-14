"""Generate URLs from athlete numbers."""

import pandas as pd

def get_athlete_urls() -> set:
    df = pd.read_csv("../data/athletes.csv")

    df["athleteURL"] = (
        "https://www.parkrun.com.au/results/athleteresultshistory/?athleteNumber="
        + df["athleteNumber"].astype(str)
    )
    return list(df["athleteURL"])

if __name__ == "__main__":
    print(get_athlete_urls())