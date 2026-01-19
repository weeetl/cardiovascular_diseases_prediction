import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Простая предобработка данных.
    
    :param df: Исходный DataFrame
    :return: Preprocessed DataFrame
    """
    
    df.drop(['Unnamed: 0', 'Troponin', 'CK-MB', 'id'], axis=1, inplace=True)
    
    df.dropna(inplace=True)

    
    df.columns = [
    col.lower().replace(' ', '_') for col in df.columns]
    
    cols = ['diabetes', 'family_history', 'smoking', 'obesity', 'alcohol_consumption', 'previous_heart_problems', 'medication_use', 'stress_level', 'physical_activity_days_per_week']
    df[cols] = df[cols].astype(int)
    
    
    return df