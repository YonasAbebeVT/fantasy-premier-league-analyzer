import pandas as pd
df = pd.read_html("premier-league.html", attrs={"id": "stats_standard"})[0]
df.columns = ['_'.join(col).strip for col in df.columns.values]
df.table()
