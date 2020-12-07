# Créé par lucas.magnac, le 07/12/2020 en Python 3.7

from random import *
from tkinder import *

Listemots = []
Secret = [1]
Mots = str
Mafenetre = Tk()
Mafenetre.title('Jeu du  pendu')
Mafenetre.geometry('300x100+400+200')
M=StringVar()
LabelMot = Label(MaFenetre, text = 'Mot')
TxtLettre = Entry(MaFenetre)

def fliretxt():
    with open("Liste.txt","r") as liste:
        ligne = liste.readline()
        while ligne != "":
            Listemots.append(ligne.rstrip('\n'))
            ligne = liste.readline()

def fmots():
    Mots = random.choice(Listemots)
    Secret[0] = Mots[0]
    for i in range(len(Mots)-1):
        Secret.append("_")
    M.set(Secret)
    return Mots

def ftrouver(pMots):
    BoutonProposer = Button(Mafenetre, text = 'Proposer' )
    BoutonProposer.pack(side = 'top', padx = 5, pady = 5)
    i = 8
    n = 1
    Lettres = []
    while i >= 0:
        Tentative = input("Une lettre ? ")

        if (Tentative in Lettres):
            print("Vous ave déjà proposé cette lettre")

        if ((Tentative not in pMots)):
            print("Plus que",i,"vies")
            i = i-1
            if i ==7:
                PhotoImage(file = 'bonhomme7')
            if i ==6:
                PhotoImage(file = 'bonhomme6')
            if i ==5:
                PhotoImage(file = 'bonhomme5')
            if i ==4:
                PhotoImage(file = 'bonhomme4')
            if i ==3:
                PhotoImage(file = 'bonhomme3')
            if i ==2:
                PhotoImage(file = 'bonhomme2')

        for j in range(len(pMots)):
            if (Tentative == pMots[j] and (Secret[j] == "_")):
                Secret[j] = Tentative
                n += 1
                print(n)
            Lettres.append(Tentative)

        print(Secret)

        if (n == len(pMots)):
            print("Gagné !")
            fmenu()
    PhotoImage(file = 'bonhomme1')
    print("Perdu !")
    fmenu()

def fmenu():
    reponse = input("Voulez vous rejouer ? (o/n): ")
    if (reponse == ("o" or "O")):
        fjeu()
    if (reponse == ("n" or "N")):
        fliretxt()
    else :
        print("réponse pas comprise, réesayez...")
        fmenu()

def fjeu():
    fliretxt()
    pMots = fmots()
    ftrouver(pMots)

Mafenetre.mainloop()



