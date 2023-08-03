import os
from enum import Enum
from typing import Optional, Literal

import pandas as pd


_DATA_PATH = r"C:\Users\bobaw\PycharmProjects\sjuul\data"


def save_df_as_csv(
    df: pd.DataFrame, name: str, path: str = _DATA_PATH, mode: Literal["w", "a"] = "w"
) -> None:
    header = mode == "w"
    full_path = os.path.join(path, name) + ".csv"
    df.to_csv(full_path, mode=mode, header=header)


def df_from_csv(
    name: str,
    path: str = _DATA_PATH,
    index_col: Optional[int] = 0,
    separator: Literal[",", ";"] = ",",
) -> pd.DataFrame:
    full_path = os.path.join(path, name) + ".csv"
    return pd.read_csv(full_path, sep=separator, header=0, index_col=index_col)
