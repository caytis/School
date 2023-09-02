FILE = 'gas_prices.txt'
        
def processAll():
    prices = []
    with open(FILE) as file:
        for line in file:
            this = line.split(':')
            date = this[0]
            price = this[1]
            prices.append([date, price])
    separateYears(prices)

def separateYears(prices):
    lastYear = 0
    lastMonth = '01'
    data = []
    thisYear = []
    thisMonth = []
    for line in prices:
        this = line[0].split('-')
        month = this[0]
        year = this[2]
        price = line[1]
        if month != lastMonth:
            thisYear.append(average(thisMonth))
            thisMonth = []
            lastMonth = month
        if year != lastYear:
            data.append(organize(lastYear, thisYear))
            lastYear = year
            thisYear = []
        thisMonth.append(price)
    write(data)

def average(data):
    total = 0
    for price in data:
        total += price
    average = total / len(data)
    return average

def low(year):
    low = 0
    for month in year:
        if month < low:
            low = month
    return low

def high(year):
    high = 0
    for month in year:
        if month > high:
            high = month
    return high

def organize(num, year):
    data = []
    data.append(num)
    data.append(low(year))
    data.append(average(year))
    data.append(high(year))
    for month in year:
        data.append(month)
    return data

def write(data):
    # with open(FILE, "w+") as file:
    #     file.write('') #gets rid of old hours
    
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

# if __name__ == '__main__':
#     main()