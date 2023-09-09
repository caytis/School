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
    
    ath_projs = {j.jno for j in projects if j.city == 'Athens'} #3. Get names of all suppliers not used in Athens projects
    ath_supp_ids = {r.sno for r in spj for j in ath_projs if r.jno == j}
    ath_supps = {s.sname for s in suppliers if s.sno in ath_supp_ids}
    ath_not = {s.sname for s in suppliers if s.sname not in ath_supps}
    print(ath_not)

    os_projs = {j.jno for j in projects if j.city == 'Oslo'} #4. Get names and colors of all parts not used in Oslo
    os_part_ids = {l.pno for l in spj for jno in os_projs if l.jno == jno}
    os_parts = {(p.pname, p.color) for p in parts for pno in os_part_ids if p.pno != pno}
    print(os_parts)

    name_pairs = {(n1.sname, n2.sname) for n1 in suppliers for n2 in suppliers if n1.sno != n2.sno if n1.city == n2.city} #5. Get pairs of names of all suppliers that are located in the same city.
    # print({p for p in name_pairs if p[0] != p[1]})

    #6. Print all suppliers out by city


if __name__ == '__main__':
    main()