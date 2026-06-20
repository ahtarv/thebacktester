import pandas as pd

class DataGenerator:
    def __init__(self,csv_path):
        self.csv_path = csv_path
        self._load_data()

    def _load_data(self):
        self.df = pd.read_csv(self.csv_path)
        self.df = self.df.sort_values(by='timestamp').reset_index(drop=True)

    def stream():
        for tick in self.df.itertuples(index=False, name="Tick"):
            yield tick