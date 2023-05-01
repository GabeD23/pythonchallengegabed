import csv

with open('challengefinal.py', 'r+') as csvfile:
    reader = csv.DictReader(csvfile)

    department_expenses = {}

    for row in reader:
        department = row['Department']
        expense = row['2012 Actual']

        if amount and amount.replace(',', '').replace('.', '').isdigit():
            amount = float(amount)
        else:
            amount = 0.0

        if expense:
            expense = float(expense)

            if department in department_expenses:
                department_expenses[department] += expense
            else:
                department_expenses[department] = expense

    for department, amount in department_expenses.items():
        formatted_expense = '${:,.2f}'.format(amount)

        print(f'{department}\t{formatted_expense}')
