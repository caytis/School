from collections import namedtuple


partsFILE = 'parts.txt' # comprehensions\
projectsFILE = 'projects.txt'
suppliersFILE = 'suppliers.txt'
spjFILE = 'spj.txt'

parts = list()
projects = set()
suppliers = set()
spj = set()


def makeTuples():
    global parts
    global projects
    global suppliers
    global spj
    parts = readFile(partsFILE)
    projects = readFile(projectsFILE)
    suppliers = readFile(suppliersFILE)
    spj = readFile(spjFILE)

def readFile(FILE):
    all = list()

    with open(FILE) as file:

        i = 0
        for line in file:
            this = line.strip().split(',')

            if i == 0:
                name = this[0].strip()
                i += 1
            elif i == 1:
                data = namedtuple(name, this)
                i += 1
            else:
                all.append(data._make(this))
                
    file.close()
    return all


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
    makeTuples()

    print({s.sname for s in suppliers for r in spj for p in parts if r.sno == s.sno if p.pno == r.pno if p.pname == "Bolt"}) #1. Get names of all suppliers that supply bolts.

    print({s.sname for s in suppliers for r in spj for p in parts if r.sno == s.sno if p.pno == r.pno if p.color == "Blue"}) #2. Get names of all suppliers that supply blue parts.

    print({s.sname for s in suppliers for r in spj for j in projects if (not r.sno == s.sno, j.city == "Athens") and (r.sno == s.sno, not j.city == "Athens", j.jno == r.jno)}) #3. Get names of all suppliers not used in Athens projects

    #4. Get names and colors of all parts not used in Oslo (not A, B), (A, not B, C)

    #5. Get pairs of names of all suppliers that are located in the same city.

    #6. Print all suppliers out by city


if __name__ == '__main__':
    main()