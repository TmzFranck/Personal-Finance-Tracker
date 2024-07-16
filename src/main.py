from data_manager import DataManager
from finance_tracker import FinanceTracker

def main():
    data_manager = DataManager('transactions.csv')
    
    transactions = [{
        'date': '2020-01-01',
        'amount': 100,
        'category': 'income',
        'description': 'birthday gift'
    }, {
        'date': '2020-01-02',
        'amount': -50,
        'category': 'food',
        'description': 'restaurant'
    }]
    
    #data_manager.save_transactions(transactions)
    #print(data_manager.load_transactions())
    
    finance_tracker = FinanceTracker(data_manager)
    
    #finance_tracker.remove_transaction(('2020-01-01', 100, 'income', 'birthday gift'))
    
    finance_tracker.generate_report()
    
    
if __name__ == '__main__':
    main()