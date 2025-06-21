# Fantasy Premier League Performance Analyzer

This project analyzes Premier League player stats to help improve Fantasy Premier League (FPL) decision-making. Using rich statistical data from FBref.com, it identifies trends and player performance indicators relevant to fantasy managers.

---

## 📊 Step 1 – Data Acquisition

I sourced player performance data from [FBref.com](https://fbref.com/en/comps/9/stats/Premier-League-Stats), a reliable provider of advanced football statistics.

### ⚙️ How I Collected the Data

Since the tables are dynamically loaded with JavaScript, I couldn’t scrape the raw HTML directly using `pandas.read_html()`. Instead:

1. I opened the stats page in a browser and let the full table load.
2. I saved the page as `premier-league.html`.
3. I loaded it using the following code:

```python
import pandas as pd

df = pd.read_html("premier-league.html", attrs={"id": "stats_standard"})[0]
