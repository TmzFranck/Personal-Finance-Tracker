import pandas as pd
import matplotlib.pyplot as plt
class FinanceTracker:
    def __init__(self, data_manager):
        self.data_manager = data_manager
    
    def add_transaction(self, transaction):
        self.data_manager.save_transactions(transaction)
    
    
    def remove_transaction(self, index):
        df = pd.read_csv(self.data_manager.transaction_file)
        df = df.drop(df.index[index - 1])
        df.to_csv(self.data_manager.transaction_file, index=False)
    
    def generate_report(self):
        transactions = self.data_manager.load_transactions()
        
        # TODO: generate a report with the following information:
    