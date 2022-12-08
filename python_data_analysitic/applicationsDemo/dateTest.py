from datetime import date, datetime


def subDate(date1, date2):
    diff = str(datetime.strptime(date1, '%m/%d/%Y') - datetime.strptime(date2, '%m/%d/%Y'))
    return diff


today = date.today().strftime('%m/%d/%Y')
previous_package_date = '12/10/2021'
a = subDate('12/10/2022', previous_package_date)
print(a)
