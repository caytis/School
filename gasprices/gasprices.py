FILE = 'gas_prices.txt'
        
def processAll():
    prices = []
    with open(FILE) as file:
        for line in file:
            this = line.split(':')
            this[1] = this[1][:-1]
            date = this[0]
            price = this[1]
            prices.append([date, price])
    separateYears(prices)

def separateYears(prices):
    lastYear = 0
    lastMonth = '01'
    data = []
    thisYear = ['1000', '0']
    thisMonth = ['1000', '0']
    for line in prices:
        this = line[0].split('-')
        month = this[0]
        year = this[2]
        price = line[1]
        if month != lastMonth:
            thisYear[0] = low([thisMonth[0], thisYear[0]])
            thisYear[1] = high([thisMonth[1], thisYear[1]])
            thisMonth.pop(0)
            thisMonth.pop(0)
            thisYear.append(average(thisMonth))
            thisMonth = ['1000', '0']
            lastMonth = month
        if lastYear == 0:
            lastYear = year
        if year != lastYear:
            data.append(organize(lastYear, thisYear))
            lastYear = year
            thisYear = ['1000', '0']
        thisMonth.append(price)
        thisMonth[0] = low([price, thisMonth[0]])
        thisMonth[1] = high([price, thisMonth[1]])
    write(data)

def average(data):
    total = 0
    for price in data:
        total += float(price)
    average = total / len(data)
    return average.__round__(2)

def low(year):
    low = float(year[0])
    for month in year:
        if float(month) <= low:
            low = float(month)
    return low

def high(year):
    high = year[0]
    for month in year:
        if month >= high:
            high = month
    return high

def organize(num, year):
    data = []
    data.append(str(num))
    data.append(str(float(year[0]).__round__(2)))
    data.append(str(average(year)))
    data.append(str(float(year[1]).__round__(2)))
    for month in year[2:]:
        month = str(month.__round__(2))
        if len(month) < 4 :
            month += '0'
        data.append(month)
    return data

def write(data):
    for year in data:
        print(year[0] + ":")
        print("    Low: $" + year[1] + ", Avg: $" + year[2] + ", High: $" + year[3])
        print("    January    $" + year[4])
        print("    February   $" + year[5])
        print("    March      $" + year[6])
        print("    April      $" + year[7])
        print("    May        $" + year[8])
        print("    June       $" + year[9])
        print("    July       $" + year[10])
        print("    August     $" + year[11])
        print("    September  $" + year[12])
        print("    October    $" + year[13])
        print("    November   $" + year[14])
        print("    December   $" + year[15])
        print()
        print()

def main():
    processAll()

if __name__ == '__main__':
    main()