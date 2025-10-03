etudiants = [
    {"nom": "Ama","note": 16, "année": 2},
    {"nom": "Maxime","note": 15, "année": 2},
    {"nom": "Bob","note": 12, "année": 1},
    {"nom": "Mathis","note": 19, "année": 1},
]


admis = [x for x in etudiants if x["note"] >= 12]

annees = set(x["année"] for x in admis)

moyennes = {}
for annee in annees:
    notes = [x["note"] for x in admis if x["année"] == annee]
    moyennes[annee] = sum(notes) / len(notes)

print(moyennes)


mention = lambda x: "TB" if x >= 16 else "B" if x >= 14 else "AB"
mentions = dict(map(lambda x: (x["nom"], mention(x["note"])), admis))

print("Moyennes :", moyennes)
print("Mentions :", mentions)
