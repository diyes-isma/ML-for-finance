import pandas as pd
import numpy as np


class DataErrorHandling(Exception):
    "This class aims to handle errors"
    pass

def dataReader(path: str) -> pd.DataFrame:
    try:
        if path.endswith('.csv'):
            return pd.read_csv(path)
        elif path.endswith('.xlsx') or path.endswith('.xls'):
            return pd.read_excel(path)
    except:
        raise DataErrorHandling("Please provide a valide path.")


def dataTransform_date(df: pd.DataFrame, target='') -> pd.DataFrame:
    df[target] = pd.to_datetime(df[target], dayfirst=True)

    # Date components
    df['year'] = df[target].dt.year
    df['month'] = df[target].dt.month
    df['day'] = df[target].dt.day
    df['day_of_week'] = df[target].dt.dayofweek

    # Time components
    df['hour'] = df[target].dt.hour
    df['minute'] = df[target].dt.minute
    
    # Weekend
    df['is_weekend'] = df[target].isin([5, 6]).astype(int)
    
    return df

def quoted_spread(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df['quoted_spread'] = np.where(df['side']==1, df['mid']-df['price'], df['price']-df['mid'])
        return df
    except:
        raise DataErrorHandling("Please check the data.")

    
