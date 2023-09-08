
partsFILE = 'comprehensions\parts.txt'
projectsFILE = 'comprehensions\projects.txt'
suppliersFILE = 'comprehensions\suppliers.txt'
spjFILE = 'comprehensions\spj.txt'


def makeTuples():
    parts = readFile(partsFILE)
    projects = readFile(projectsFILE)
    suppliers = readFile(suppliersFILE)
    spj = readFile(spjFILE)
    
    return parts, projects, suppliers, spj

def readFile(FILE):
    data = list()
    names = list()

    with open(FILE) as file:

        i = 0
        for line in file:
            values = dict()
            this = line.split(',')

            if i == 0:
                values['name'] = this[0].strip() #??? TODO: need to make this accessible
            elif i == 1:
                for word in this:
                    # if i == 1:
                    #     beginning = word[0]
                    names.append(word.strip())
            else:
                x = 0
                for word in this:
                    values[names[x] + str(i - 1)] = word.strip()
                    x += 1
                data.append(values)
            i += 1
    file.close()
    return data


def get(lyst):
    pass

# {s.sname for s in suppliers for r in spj for j in projects 
#  if r.sno == s.sno if j.jno == r.jno if j.city == 'London'}

# #  {'Jones', 'Adams', 'Clark'}

# london_projs = {j.jno for j in projects if j.city == 'London'}
# london_supp_ids = {r.sno for r in spj if r.jno in london_projs}
# london_supps = {s.sname for s in suppliers if s.sno in london_supp_ids}
# print(london_supps)


# # {'Adams'}
# # {'Jones', 'Adams', 'Blake'}
# # {'Blake'}
# # {('Cam', 'Blue'), ('Cog', 'Red'), ('Nut', 'Red'), ('Bolt', 'Green'), ('Screw', 'Red')}
# # {('Jones', 'Blake'), ('Smith', 'Clark')}
# # {'Paris': {'Jones', 'Blake'}, 'Athens': {'Adams'}, 'London': {'Clark', 'Smith'}}

def main():
    parts, projects, suppliers, spj = makeTuples()
    get(suppliers, "bolts")
    # # 1. Get names of all suppliers that supply bolts.
    # # 2. Get names of all suppliers that supply blue parts.
    # # 3. Get names of all suppliers not used in Athens projects
    # # 4. Get names and colors of all parts not used in Oslo
    # # 5. Get pairs of names of all suppliers that are located in the same city.
    # # 6. Print all suppliers out by city

if __name__ == '__main__':
    main()