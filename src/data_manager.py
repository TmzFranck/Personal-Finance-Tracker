import pandas as pd
import csv
class DataManager:
    def __init__(self, transaction_file):
        self.transaction_file = transaction_file
    
    def load_transactions(self, start_date, end_date):
        with open (self.transaction_file, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader if start_date <= row['date'] <= end_date]
            

    def save_transactions(self, transactions):
        with open (self.transaction_file, 'a' , newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'amount', 'category', 'description'])
            for transaction in transactions:
                writer.writerow(transaction)

    def load_all_transactions(self):
        with open (self.transaction_file, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
        
    def remove_transaction(self, index):
        df = pd.read_csv(self.transaction_file)
        df = df.drop(df.index[index - 1])
        df.to_csv(self.transaction_file, index=False)
        
    def get_categories(self, category):
        transactions = self.load_all_transactions()
        return [i for i in transactions if i['category'] == category]