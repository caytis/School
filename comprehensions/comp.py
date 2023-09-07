

# 1. Get names of all suppliers that supply bolts.
# 2. Get names of all suppliers that supply blue parts.
# 3. Get names of all suppliers not used in Athens projects
# 4. Get names and colors of all parts not used in Oslo
# 5. Get pairs of names of all suppliers that are located in the same city.
# 6. Print all suppliers out by city


{s.sname for s in suppliers for r in spj for j in projects 
 if r.sno == s.sno if j.jno == r.jno if j.city == 'London'}

#  {'Jones', 'Adams', 'Clark'}

london_projs = {j.jno for j in projects if j.city == 'London'}
london_supp_ids = {r.sno for r in spj if r.jno in london_projs}
london_supps = {s.sname for s in suppliers if s.sno in london_supp_ids}
print(london_supps)


# {'Adams'}
# {'Jones', 'Adams', 'Blake'}
# {'Blake'}
# {('Cam', 'Blue'), ('Cog', 'Red'), ('Nut', 'Red'), ('Bolt', 'Green'), ('Screw', 'Red')}
# {('Jones', 'Blake'), ('Smith', 'Clark')}
# {'Paris': {'Jones', 'Blake'}, 'Athens': {'Adams'}, 'London': {'Clark', 'Smith'}}