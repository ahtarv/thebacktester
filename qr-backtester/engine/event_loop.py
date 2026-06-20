import pandas as pd

class DataGenerator:
    def __init__(self,csv_path):
        self.csv_path = csv_path # we define the csv path
        self._load_data() # we load the data

    def _load_data(self):
        self.df = pd.read_csv(self.csv_path) # using pd reading csv
        self.df = self.df.sort_values(by='timestamp').reset_index(drop=True) #we s

    def stream():
        for tick in self.df.itertuples(index=False, name="Tick"):
            yield tick #converts each row of data frame into a  named tuple