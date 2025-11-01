import json

import pandas as pd


def read_csv(path: str) -> str:
    """Чтение файла CSV и приведение его в json"""
    df = pd.read_csv(path)
    df_dict = df.to_dict("records")
    df_json = json.dumps(df_dict, ensure_ascii=False, indent=4)
    return df_json


def read_excel(path: str) -> str:
    """Чтение файла Excel и приведение его в json"""
    df = pd.read_excel(path)
    df_dict = df.to_dict("records")
    df_json = json.dumps(df_dict, ensure_ascii=False, indent=4)
    return df_json
