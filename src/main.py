from data_manager import DataManager
from finance_tracker import FinanceTracker
from datetime import datetime
from transaction import Transaction


def get_amount():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            return amount
        except ValueError:
            print('Invalid amount. Please try again.')
            
def get_category():
    while True:
        category = input('Enter the caregory: ')
        if category in ('income', 'expense'):
            return category
        print('Invalid category. Please try again.')
        print('Valid categories are income and expense.')
        
def get_description():
    return input('Enter the descriotion: ')

def get_date():
    while True:
        try:
            date = input('Enter the date (YYYY-MM-DD): ')
            if datetime.strptime(date, '%Y-%m-%d'):
                return date
        except ValueError:
            print('Invalid date. Please try again.')
            print('Date format is YYYY-MM-DD')
            
        
def get_transaction(date, amount, category, description):
    transaction = Transaction(date, amount, category, description)
    return transaction.to_dict()
    
    
def main():
    while True:
        data_manager = DataManager('transactions.csv')
        finance_tracker = FinanceTracker(data_manager)
        print('1. Add transaction')
        print('2. Generate report')
        print('3. Remove transaction')
        print('4. Exit')

        transactions = data_manager.load_all_transactions()
        if len(transactions) > 0:
            print('Current state of transactions:')
            income = [float(i['amount']) for i in data_manager.get_categories('income')]
            depense = [float(i['amount']) for i in data_manager.get_categories('depense')]
            
            if len(income) > 0:
                print(f'Total income: {sum(income)}')
            else:
                print('Total income: 0')
            if len(depense) > 0:
                print(f'Total depense: {sum(depense)}')
            else:
                print('Total depense: 0')
         
        try:
            choice = input('Enter your choice: ')
            if choice == '1':
                date = get_date()
                amount = get_amount()
                category = get_category()
                description = get_description()
                transaction = get_transaction(date, amount, category, description)
                finance_tracker.add_transaction(transaction)
                print('Transaction added successfully.')
            elif choice == '2':
                finance_tracker.generate_report()
            elif choice == '3':
                transactions = data_manager.load_all_transactions()
                if len(transactions) == 0:
                    print('No transactions to remove.')
                    continue
                for index, transaction in enumerate(transactions):
                    print(f'{index + 1}. {transaction}')
                while True:
                    try:
                        index = int(input('Enter the index of the transaction you want to remove: '))
                        data_manager.remove_transaction(index)
                        print('Transaction removed successfully.')
                        transactions = data_manager.load_all_transactions()
                        if len(transactions) == 0:
                            print('No transactions.')
                        else:
                            for index, transaction in enumerate(transactions):
                                print(f'{index + 1}. {transaction}')
                        break
                    except ValueError:
                        print('Invalid index. Please try again.')
                        continue
            elif choice == '4':
                break
            else:
                print('Invalid choice. Please try again.')
                continue
        except KeyboardInterrupt:
            print('\n Exiting...')
            break    
if __name__ == '__main__':
    main()