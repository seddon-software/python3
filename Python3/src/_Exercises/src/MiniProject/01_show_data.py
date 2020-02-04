import pandas as pd
import geopandas

pd.set_option('display.precision', 1)
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 500)

# read in WIND data
WIND_df = pd.read_csv("wtk_site_metadata.csv")
print(WIND_df)
print(WIND_df.sample(5))

