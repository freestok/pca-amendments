import pandas as pd

sheet_id = '1zHPyYMQohB26zup97N2UPOCAuo21tOxrCwtmRIGokng'

dfs = []
for i in range(12):
    sheet_name = str(i + 1)
    print(sheet_name)
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

    df = pd.read_csv(url)
    df = df[['Presbytery', 'Unnamed: 3', 'Unnamed: 4']].copy()
    df['item'] = f'Item {sheet_name}'
    df.columns = ['presbytery', 'for', 'against', 'item']
    df = df.loc[pd.notna(df.presbytery)]
    dfs.append(df)

final_df = pd.concat(dfs)
final_df.to_csv('presbytery_data.csv', index=False)