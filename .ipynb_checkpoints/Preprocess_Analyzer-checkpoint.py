#!/usr/bin/env python
# coding: utf-8

import anywidget
import traitlets
import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

def to_json(instance: dict, widget) -> list[dict]:
    return {
        "df": instance["df"].to_json(orient="records")
    }

class MyWidget(anywidget.AnyWidget):
    _esm = pathlib.Path("widget.js")
    
    _data = traitlets.Dict().tag(sync=True, to_json=to_json)
    _data2 = traitlets.Dict().tag(sync=True, to_json=to_json)
    _data3 = traitlets.Dict().tag(sync=True, to_json=to_json)
    _data4 = traitlets.Dict().tag(sync=True, to_json=to_json)
    _data5 = traitlets.Dict().tag(sync=True, to_json=to_json)    
    _data6 = traitlets.Dict().tag(sync=True, to_json=to_json)    

    def __init__(self, df, df2, df3, df4, df5, df6):
        super().__init__(_data={"df": df}, _data2={"df": df2}, _data3={"df": df3}, _data4={"df": df4}, _data5={"df": df5}, 
                        _data6 = {"df": df6})
        #super().__init__(_data2={"df": df2})

    
    @property
    def df(self):
        return self._data["df"]

    @df.setter
    def df(self, new_df):
        self._data = { "df": new_df }


def ppa_widget(df1_original, df2_original):
    df1 = df1_original.drop(["CountyId", "RegionId", "StateId"], axis =  1, inplace = False)
    df2 = df2_original.drop(["CountyId", "RegionId", "StateId"], axis =  1, inplace = False)
    
    common_col = np.intersect1d(df1.columns, df2.columns)
    drop_col = df1.columns.difference(df2.columns)
    add_col = df2.columns.difference(df1.columns)

    df_drop = df1[drop_col]
    df_add = df2[add_col]

    df1_com = df1[common_col]
    df2_com = df2[common_col]

    df1_num = df1_com.select_dtypes(include='number')
    df2_num = df2_com.select_dtypes(include='number')
    cat_col = np.setdiff1d(list(df1_com.columns), list(df1_num.columns))
    df1_cat = df1_com[cat_col]
    df2_cat = df2_com[cat_col]
    
    df1_num_sum = data_format(df1_num)
    df2_num_sum = data_format(df2_num)
    
    
    if df_add.empty == False:
        df_add_sum = data_format(df_add)

    else:
        data = [[0,0,0,0,0,0,0,0,"NoneAdded",0,0,0]]
        df_add_sum = pd.DataFrame(data, columns=['count', 'mean', 'std', 'min', 'q1', 'q2', 'q3', 'max', 'label', 'zeros', 'outliers', 'missing'], index = ["NoneAdded"])
    if df_drop.empty == False:
        df_drop_sum = data_format(df_drop)
    else:
        data = [[0,0,0,0,0,0,0,0,"NoneDropped",0,0,0]]
        df_drop_sum = pd.DataFrame(data, columns=['count', 'mean', 'std', 'min', 'q1', 'q2', 'q3', 'max', 'label', 'zeros', 'outliers', 'missing'], index = ["NoneDropped"])
    


    df_zero = pd.DataFrame(0, columns=df_add_sum.columns, index=df_add_sum.index)
    df_zero["label"] = df_add_sum["label"]
    df_diff = df2_num_sum[["count", "mean", "std", "min", "q1", "q2", "q3", "max", "zeros", "outliers", "missing"]].subtract(
        df1_num_sum[["count", "mean", "std", "min", "q1", "q2", "q3", "max", "zeros", "outliers", "missing"]])

    
    df_div = df_diff[["count", "mean", "std", "min", "q1", "q2", "q3", "max", "zeros", "outliers", "missing"]].div(
    df1_num_sum[["count", "mean", "std", "min", "q1", "q2", "q3", "max", "zeros", "outliers", "missing"]])
    df_div.replace([np.inf, -np.inf], 25.0, inplace=True)
    df_div.fillna(0, inplace = True)
    df_div = df_div.abs()
    df_div['change'] = df_div.sum(axis=1, numeric_only=True)
    df_div['change_log'] = df_div["change"].apply(np.log10)
    df_div["change_log"].replace([-np.inf], -2.0, inplace=True)



    scaler = MinMaxScaler(feature_range=(0, 5.0))
    df_div['change_scale'] = scaler.fit_transform(df_div['change'].values[:, None])
    df_div['change_scale'] = df_div['change_scale']

    df_div['label'] = df_div.index

    df_change = df_div[["change", "change_log", "change_scale", "label"]]
        
    return Widget(df=df_change, df2 = df1_num_sum, df3 = df2_num_sum, df4 = df_drop_sum, df5 = df_add_sum, df6 = df_zero)


def my_scaler(var):
    return (5 - 0) * ( (var - min(var)) / (max(var) - min(var)) ) + 0


def data_format(df1_num):
    df1_num_sum = df1_num.describe().transpose()
    df1_num_sum['label'] = df1_num_sum.index
    
    result1 = []
    for x in df1_num_sum["label"]:
        result1.append(df1_num.loc[df1_num[x].eq(0.0)].shape[0])
    df1_num_sum["zeros"] = result1
    
    result1 = []
    for index, row in df1_num_sum.iterrows():
        max = row["mean"] + 3*row["std"]
        min = row["mean"] - 3*row["std"]
        res = 0
        for x in df1_num[row["label"]]:
            if x < min or x > max:
                res = res + 1
        result1.append(res)
    df1_num_sum["outliers"] = result1
    
    result1 = []
    for x in df1_num:
        result1.append(df1_num[x].isna().sum())
    df1_num_sum["missing"] = result1
    
    df1_num_sum = df1_num_sum.rename(columns={"25%": "q1", "50%": "q2", "75%": "q3"})

    df1_num_sum["std"] = np.trunc(10 * df1_num_sum["std"]) / 10
    df1_num_sum["mean"] = np.trunc(10 * df1_num_sum["mean"]) / 10
    df1_num_sum["q1"] = np.trunc(10 * df1_num_sum["q1"]) / 10
    df1_num_sum["q2"] = np.trunc(10 * df1_num_sum["q2"]) / 10
    df1_num_sum["q3"] = np.trunc(10 * df1_num_sum["q3"]) / 10

    return df1_num_sum

