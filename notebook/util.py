import pandas as pd


def get_unique_dict(series):
    d = {}
    for idx, row in enumerate(series.unique()):
        d[row] = idx
    return d


def get_df(series, unique_dict, header):
    li = []
    for row in series:
        li.append(unique_dict[row])
    return pd.DataFrame.from_dict({header: li})


def get_unique_value(idx, unique_dict):
    for k, v in unique_dict.items():
        if idx == v:
            return k


def show_recommemd_beer(pred, name_dict, style_dict, df):
    pred_beer = pred[0]
    name = ''
    for k, v in name_dict.items():
        if v == pred_beer:
            name = k
    for row in df.itertuples():
        if name in row.name:
            print(row)
            print('style_id', style_dict[row.style])
