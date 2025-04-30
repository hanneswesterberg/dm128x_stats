import pandas as pd
from conversion import convert_to_long
from friedmanTest import friedman_per_condition
from nemenyiTest import nemenyi_test

df = pd.read_csv("corrected_ranks.csv")  # Read file
df = convert_to_long(df)  # Convert to long format
df['rank'] = df['rank'].astype(float)  # Make sure rank is float
pd.set_option('display.max_rows', None)  # Show all rows in the data frame

# FRIEDMAN TEST PER CONDITION
friedman1 = friedman_per_condition(df, ['audio', 'playback_speed'])
print(friedman1, "\n")

# NEMENYI POST-HOC
nemenyi_res = nemenyi_test(df)
for each in nemenyi_res:
    print(each)
    print('\n')
