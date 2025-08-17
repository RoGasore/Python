# Ce simple script Python est un vérificateur d'anagrammes.
Str = [
    ("chien", "niche"),
    ("gare", "rage"),
    ("maison", "raison"),
    ("marie", "aimer"),
    ("table", "ballon"),
    ("ange", "gena"),
    ("rêve", "èvre"),
    ("lait", "talons"),
    ("poisson", "poison"),
    ("scie", "cies"),
    ("ruer", "rure"),
    ("chat", "tach"),
    ("sain", "saint")
]

def est_anagramme(str1, str2):
    return sorted(str1) == sorted(str2)
    
for mot1, mot2 in Str:
    resultat = "est un anagramme" if est_anagramme(mot1, mot2) else "n'est pas un anagramme"
    print(f"'{mot1}' et '{mot2}' : {resultat}")
