import pandas as pd
pd.set_option('display.precision', 1)
pd.set_option('display.width', None)        # None means all data displayed
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
'''
Pandas 2D dataset are called dataframe.
This example shows several methods of the dataframe.
'''

def main(): 
    df = pd.read_csv("data/covid.csv", 
                               engine = 'python') #,
#                               skipinitialspace = True, 
#                               sep = '[*# ]+')
#    print(df)
    pd.set_option('display.width', 80)
    df = df.sort_values(by=['geography'])
    print(df.head())       # first five rows
    print(df.tail())       # last five rows
    print(df.sample(5))    # random sample of rows
    print(df.shape)        # number of rows/columns in a tuple
    print(df.describe())   # calculates measures of central tendency
    df.info()              # memory footprint and datatypes

    tmax = df.sort_values('tmax', axis=0, ascending=False)
    pd.set_option('display.max_rows', 20)
    print(tmax)
main()
