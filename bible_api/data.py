import pandas as pd
import os

def load_data():
    csv_path = os.path.join(os.path.dirname(__file__), 'bible_data_set.csv')
    dataset = pd.read_csv(csv_path)
    return dataset
