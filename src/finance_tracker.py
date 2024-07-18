import pandas as pd
import matplotlib.pyplot as plt
class FinanceTracker:
    def __init__(self, data_manager):
        self.data_manager = data_manager
    
    def add_transaction(self, transaction):
        self.data_manager.save_transactions(transaction)
    
    def generate_report(self):
        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True
        
        df = pd.read_csv(self.data_manager.transaction_file)
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        df = df.dropna(subset=['amount'])
        df.groupby('category')['amount'].sum().plot(kind='bar')

        plt.show()
    