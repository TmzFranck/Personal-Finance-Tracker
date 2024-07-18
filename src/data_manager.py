
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
