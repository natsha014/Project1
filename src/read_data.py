import pandas as pd


def read_csv(path: str) -> list[dict]:
    """Чтение файла CSV и приведение его в список словарей"""
    df = pd.read_csv(path, delimiter=";")
    df_dict = df.to_dict("records")
    return df_dict


def read_excel(path: str) -> list[dict]:
    """Чтение файла Excel и приведение его в список словарей"""
    df = pd.read_excel(path)
    df_dict = df.to_dict("records")
    return df_dict
