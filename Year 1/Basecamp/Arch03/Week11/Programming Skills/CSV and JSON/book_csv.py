import csv

villains = [
    ["Doctor", "No"],
    ["Rosa", "Klebb"],
    ["Mister", "Big"],
    ["Auric", "Goldfinger"],
    ["Ernst", "Blofeld"],
]

with open("villains.csv", "wt") as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)


with open("villains.csv", "rt") as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin]


with open("villains.csv", "rt") as fin:
    cin = csv.DictReader(fin, fieldnames=["First", "Last"])
    villains = [row for row in cin]

print(villains)

villains = [
    {"first": "Doctor", "last": "No"},
    {"first": "Rosa", "last": "Klebb"},
    {"first": "Mister", "last": "Big"},
    {"first": "Auric", "last": "Goldfinger"},
    {"first": "Ernst", "last": "Blofeld"},
]
with open("villains.csv", "wt") as fout:
    cout = csv.DictWriter(fout, ["first", "last"])
    cout.writeheader()
    cout.writerows(villains)


# it automatically grabs the first row and uses it as key;value
with open('villains.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]

print(villains)