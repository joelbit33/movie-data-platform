import pandas as pd

# simply a json to csv converter, saving some cleaning to sql, easier..
df = pd.read_json('../data/movies_data.json')
df.to_csv('test_csv.csv', index=False)