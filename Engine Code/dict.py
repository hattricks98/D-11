from itertools import combinations
import pprint

# accepting only those candidates that has the rating >= 8.5
mydict = {'D kock':[9.5,'wk','RCB'],'R sharma':[9.5,'bat','RCB'],
'S Yadav':[9,'bat','RCB'], 'K Pollard':[8.5,'bat','RCB'],'Wiliam':[10,'bat','RR'],
'M Pandey':[9.5,'bat','CSK'],'M Guptill':[9,'bat','RR'],'E Louis':[8.5,'bat','RCB'],'H Pandey':[10,'all','CSK'],'M Nabbi':[9,'all','CSK'],
'K Pandey':[8.5,'all','RCB'],
'V Shankar':[8.5,'all','RR'],'A sharma':[8,'all','RR'],'J bumrah':[9,'bowl','RCB'],'Malinga':[8.5,'bowl','RCB'],
'R Chahar':[8.5,'bowl','RCB'],'B kumar':[8.5,'bowl','RR'],'K Hamid':[8.5,'bowl','RR'],'S Kaul': [8.5,'bowl','RR'],'R Khan':[9,'bowl','CSK']}

comb = list(combinations(mydict.keys(),11))
# print(mydict.keys())
# print(len(comb)) # 352716

a = [list(i) for i in comb]
names = mydict.keys()
# print(names)

b = []
for j in a: 
    if mydict[j[0]][0]+mydict[j[1]][0]+mydict[j[2]][0]+mydict[j[3]][0]+mydict[j[4]][0]+mydict[j[5]][0]+mydict[j[6]][0]+mydict[j[7]][0]+mydict[j[8]][0]+mydict[j[9]][0]+mydict[j[10]][0] > 99: 
        del j
    elif mydict[j[0]][0]+mydict[j[1]][0]+mydict[j[2]][0]+mydict[j[3]][0]+mydict[j[4]][0]+mydict[j[5]][0]+mydict[j[6]][0]+mydict[j[7]][0]+mydict[j[8]][0]+mydict[j[9]][0]+mydict[j[10]][0] < 98:
        del j
    else: 
        b.append(j)

# print(len(b)) # 301444


constraints = [
    {
        "feature": "wk",
        "filter": lambda x: len(x) == 1,
    },
    {
        "feature": "bat",
        "filter": lambda x: len(x) == 4,
    },
    {
        "feature": "bowl",
        "filter": lambda x: len(x) == 3,
    },
    {
        "feature": "all",
        "filter": lambda x: len(x)== 3,
    },
    {
        "feature": "RR",
        "filter": lambda x:2 <= len(x) <= 5,
    },
    {
        "feature": "CSK",
        "filter": lambda x: len(x) == 4,
    }
    
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

pp = pprint.PrettyPrinter(width=200,depth=6, compact=True)
pp.pprint(op)
st = op.sort()
print(st)
# print(type(op))
# import random

# for x in op[0]:
#     captain = random.choice(x)
#     print(captain)

# data_t.to_csv('result.csv',header=True,index=None)

# data = pd.DataFrame(op)
# data_t = data.T
# print(data)

# data_t.to_csv('result2.csv',header=True,index=None)