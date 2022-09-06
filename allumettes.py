# le jeu des allumettes
tour = 1
N, p_max = 20, 3
joueurs = ["Joueur A", "Joueur B"]
prises = []
print("Bienvenue dans le jeu des allumettes!")

def reste_de_la_division_par_2(n):
    return n % 2

def num_joueur(n):
    r = reste_de_la_division_par_2(n)
    return 1 - r

while N > 1:
    print("Il y a", N, "allumettes. ", end="")
    print("Prise max: " + str(p_max))
    print(joueurs[num_joueur(tour)], "combien en prenez-vous?")
    prise_str = input()
    prises.append(prise_str)
    prise = int(prise_str)
    if prise > p_max or prise < 1:
        print("Triche !")
    N = N - prise
    tour = tour + 1
    
if N == 1:
    print("Gagné !")
elif N == 0:
    print("Perdu !")
else:
    print("C'est trop !")
    
print("Prises:")
for p in range(len(prises)):
    print(prises[p], end=" - ")
print()
