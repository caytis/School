import pandas as pd
import matplotlib.pyplot as plt
import statistics
# import threading

def parse():
    csv = open("Ozone/daily_44201_2021.csv").readlines()
    # counties = open("Ozone/counties.txt").readlines()
    categories = [x.strip('"\n') for x in csv[0].split(',')]
    divvied = []
    lines = []
    for i in range(len(csv) - 1):
        lines.append(csv[i + 1].strip().split(',"'))
        divvied.append({})
        cat = 0
        for x in range(len(lines[i])):
            item = lines[i][x]
            if (len(item.split(' ')) <= 1) and (len(item.split(',')) >= 1):
                for neww in item.strip('," \n').split(','):
                    divvied[i][categories[cat]] = neww
                    if cat < 28: cat += 1
            else:
                divvied[i][categories[cat]] = item.strip(',"')
                if cat < 28: cat += 1

    # threading.Thread()
    states = {}
    for line in divvied:
        state = line.get("State Name").lower()
        county = line.get("County Name").lower()
        if state not in states.keys():
            states[state] = {}
        if county not in states[state].keys(): # has utah in utah? there's a few things messed up
            states[state][county] = []
        states[state][county].append(line)

    statecodes = open("Ozone/state_codes-1.txt").readlines()
    codes = {}
    for line in statecodes:
        items = line.strip().split(',')
        codes[items[0]] = items[1]

    return states, codes

def ask(states, codes):
    inp = input("Enter 2-letter state code (Q to quit): ").upper()  # Check for invalid
    if inp == 'Q':
        return
    if inp not in codes:
        print('Invalid state code!\n')
        ask(states, codes)
        return
    state = codes[inp].lower()
    while(True):
        i = 1
        for countyy in states[state]:
            print(f'{i}: {countyy}')
            i += 1
        num = int(input("Enter number for county: "))
        x = 1
        county = ""
        for countyy in states[state]:
            if num == x:
                county = countyy.lower()
                break
            x += 1
        if not county:
            print('\nInvalid county number!\n')
            continue
        dest = input("Choose destination for plot: \n      1     Screen\n      2     File\n")
        if dest == '1':
            plot(states[state][county])
            
        if dest == '2':
            file = input('Enter file with extension of jpg|png|pdf: ')
            plot(states[state][county], file)
        yn = input(f'Another {state} county? (y/n): ').lower()
        if yn == 'y':
            continue
        else:
            ask(states, codes)
        return

def plot(data, dest=None):
    aqi = [int(line['AQI'].strip()) for line in data]
    avg = statistics.mean(aqi)
    color = 'green'
    if avg > 50:
        color = 'red'
    _, axis = plt.subplots()
    axis.plot(aqi, color, linewidth=0.5)
    if dest:
        plt.savefig(dest)
    else:
        plt.show()
    return

if __name__ == '__main__':
    print("Loading data...")
    states, codes = parse()
    ask(states, codes)