from itertools import combinations
# import json
# import pprint as pp


mydict = {
'K Lowry':[15,'PG','TOR'],
'E Bledsoe':[12.5,'PG', 'MIL'],
'G Hill':[9,'PG', 'MIL'],
'F Vanvleet':[5,'PG','TOR'],
'J Lin':[4,'PG','MIL'],
'M Brogdon':[10,'SG','MIL'],
'D Green':[9,'SG','TOR'],
'P Connagauton':[8,'SG','MIL'],
'N Powell':[5,'SG', 'TOR'],
'S Brown':[4.5,'SG','MIL'],
'J Meeks':[4,'SG','TOR'],
'P Mccaw':[4,'SG','TOR'],
'K Leonard':[22,'SF','PERMA'],  # Fixed Player
'K Middeleton':[14.5, 'SF', 'MIL'],
'N Mirotic':[9, 'SF', 'MIL'],
'O Anunoby':[5,'SF','TOR'],
'T Snell':[3.5,'SF','MIL'],
'M Miller':[3.5,'SF','TOR'],
'G Antekounmpo':[23,'PF','PERMA'],
'P Siakam':[15,'PF','TOR'],
'E Ilyasova':[8.5,'PF','MIL'],
'D Wilson':[4.5,'PF','MIL'],
'C Boucher':[4,'PF','TOR'],
'M Gasol':[12,'CE','TOR'],
'B Lopez':[10,'CE','MIL'],
'S Ibaka':[10,'CE','TOR'],
'E Moreland':[3.5,'CE','TOR'],
}

comb = list(combinations(mydict.keys(),8))
# print(mydict.keys())
print(len(comb))

a = [list(i) for i in comb]
# print(len(a))

b = []
for j in a:
    if mydict[j[0]][0]+mydict[j[1]][0]+mydict[j[2]][0]+mydict[j[3]][0]+mydict[j[4]][0]+mydict[j[5]][0]+mydict[j[6]][0]+mydict[j[7]][0] > 100:
        del j
    elif mydict[j[0]][0]+mydict[j[1]][0]+mydict[j[2]][0]+mydict[j[3]][0]+mydict[j[4]][0]+mydict[j[5]][0]+mydict[j[6]][0]+mydict[j[7]][0] < 96.5:
        del j
    else:
        b.append(j)

# print(len(b)) # 301444




constraints = [
    {
        "feature": "PG",
        "filter": lambda x: 1 <= len(x) <= 3,
    },
    {
        "feature": "SG",
        "filter": lambda x: 1 <= len(x) <= 3,
    },
    {
        "feature": "SF",
        "filter": lambda x: 0 <= len(x) <= 2,
    },
    {
        "feature": "PF",
        "filter": lambda x: 0 <= len(x) <= 2,
    },
    {
        "feature": "CE",
        "filter": lambda x: 1 <= len(x) <= 3,
    },
    {
        "feature": "MIL",
        "filter": lambda x: 2 <= len(x) <= 4,
    },
    {
        "feature": "TOR",
        "filter": lambda x: 2 <= len(x) <= 4,

    },
    {
        "feature": "PERMA",
        "filter": lambda x: len(x) == 2,

    },
]

def fill_constraints(players):
    for c in constraints:
        c["feature_set"] = {i for i, j in players.items() if c["feature"] in j}

def filter_player_types(teams, players):
    return [
        team for team in map(set, teams)
        if all(c["filter"](team & c["feature_set"]) for c in constraints)
    ]

fill_constraints(mydict)
op = filter_player_types(b, mydict)

#pp = pprint.PrettyPrinter(width=200,depth=6, compact=True)
print("Number of combinations :",len(op))

cost = len(op) * 33
print("Cost to assemble these teams will be : ₹",cost)


# import pandas as pd

# data = pd.DataFrame(op)
# data_t = data.T
# print(data)

# data_t.to_csv('__VS__.csv',header=True,index=None)

