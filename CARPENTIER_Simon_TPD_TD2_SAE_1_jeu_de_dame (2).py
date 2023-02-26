from re import L
import string
from typing import Final
from matplotlib.font_manager import X11FontDirectories
import numpy as np
import numpy.typing as npt

nombre_case:Final[int] = 10 #constante pour la taille du tableau
jeu_dame=npt.NDArray[np.int_] #type du tableau

damier:jeu_dame = np.empty([nombre_case,nombre_case]) # type: ignore #définition du tableau
damier[:][:]=0 #on rempli le tableau

#liste des types des variables
b : int
n : int 
i : int
j : int
x1 : int
y1 : int
x2 : int
y2 : int
x3 : int
y3 : int
x4 : int 
y4 : int
prise: str
Tour : bool
choix_coo : bool
victoire : bool
p : bool
couleur : int
nb_blancs : int
nb_noirs : int
nbr_cases_libre : int
autour_libre : bool
dame_b : int
dame_n : int
case_vide : bool
s : int
f : int
rejouer_dame : int


n=5
b=3
couleur = 3
nbr_cases_libre=0
dame_b=9
dame_n=2


def sur_damier(i,j):                            #verifie si la case séléctionnée est sur le damier
    return(i>=0 and i<=9 and j>=0 and j<=9)

def inversecouleur(couleur):                    #permet les changements de couleur (et donc de joueur)
    if couleur == 5:
        return 3
    if couleur == 3:
        return 5

def inversecouleur_dame(couleur):               #permet de définir quelles sont les dames de la couleur opposées (pour prise, verification etc..)
    if couleur == 5:
        return 9
    if couleur == 3:
        return 2

def dame(couleur):                              #nous affiche la dame liée a la couleur
    if couleur==3:
        return 9
    elif couleur==5:
        return 2

def verification(damier, couleur):              #verifie si on peut prendre un pion ou une dame et va nous permettre de l'imposer
    for i in range (0, nombre_case):
        for j in range (0, nombre_case):
            if damier[i,j]==couleur:
                if sur_damier(i-2, j-2): 
                    if damier[i-1,j-1]==inversecouleur(couleur) and damier[i-2, j-2]==0 :
                        print("on peut prendre le pion en haut a gauche")
                        return True
                    elif damier[i-1,j-1]==inversecouleur_dame(couleur) and damier[i-2, j-2]==0:
                        print("on peut prendre le pion en haut a gauche")
                        return True
                if sur_damier(i-2, j+2):
                    if damier[i-1,j+1]==inversecouleur(couleur) and damier[i-2, j+2]==0 :
                        print("on peut prendre le pion en haut a droite")
                        return True
                    elif damier[i-1,j+1]==inversecouleur_dame(couleur) and damier[i-2, j+2]==0 :
                        print("on peut prendre le pion en haut a droite")
                        return True
                if sur_damier(i+2, j-2):
                    if damier[i+1,j-1]==inversecouleur(couleur) and damier[i+2, j-2]==0 :
                        print("on peut prendre le pion en bas a gauche")
                        return True
                    elif damier[i+1,j-1]==inversecouleur_dame(couleur) and damier[i+2, j-2]==0 :
                        print("on peut prendre le pion en bas a gauche")
                        return True
                if sur_damier(i+2, j+2):
                    if damier[i+1,j+1]==inversecouleur(couleur) and damier[i+2, j+2]==0 :
                        print("on peut prendre le pion en bas a droite")
                        return True
                    elif damier[i+1,j+1]==inversecouleur_dame(couleur) and damier[i+2, j+2]==0 :
                        print("on peut prendre le pion en bas a droite")
                        return True
    for i in range (0, nombre_case):
        for j in range (0, nombre_case):
            if damier[i,j]==dame(couleur):
                if sur_damier(i-2, j-2): 
                    if damier[i-1,j-1]==inversecouleur(couleur) and damier[i-2, j-2]==0 :
                        print("on peut prendre le pion en haut a gauche")
                        return True
                    elif damier[i-1,j-1]==inversecouleur_dame(couleur) and damier[i-2, j-2]==0:
                        print("on peut prendre le pion en haut a gauche")
                        return True
                if sur_damier(i-2, j+2):
                    if damier[i-1,j+1]==inversecouleur(couleur) and damier[i-2, j+2]==0 :
                        print("on peut prendre le pion en haut a droite")
                        return True
                    elif damier[i-1,j+1]==inversecouleur_dame(couleur) and damier[i-2, j+2]==0 :
                        print("on peut prendre le pion en haut a droite")
                        return True
                if sur_damier(i+2, j-2):
                    if damier[i+1,j-1]==inversecouleur(couleur) and damier[i+2, j-2]==0 :
                        print("on peut prendre le pion en bas a gauche")
                        return True
                    elif damier[i+1,j-1]==inversecouleur_dame(couleur) and damier[i+2, j-2]==0 :
                        print("on peut prendre le pion en bas a gauche")
                        return True
                if sur_damier(i+2, j+2):
                    if damier[i+1,j+1]==inversecouleur(couleur) and damier[i+2, j+2]==0 :
                        print("on peut prendre le pion en bas a droite")
                        return True
                    elif damier[i+1,j+1]==inversecouleur_dame(couleur) and damier[i+2, j+2]==0 :
                        print("on peut prendre le pion en bas a droite")
                        return True
    
    return False

def rejouer(damier, couleur, x2, y2):           #fait rejouer le joueur si il peut reprendre avec son pion
    if damier[y2,x2]==couleur or damier[y2,x2]==dame(couleur): 
        if sur_damier(y2-2, x2-2): 
            if (damier[y2-1,x2-1]==inversecouleur(couleur) or damier[y2-1,x2-1]==inversecouleur_dame(couleur)) and damier[y2-2, x2-2]==0 :
                print("Rejouez pour continuez la prise avec le même pion")
                return False
        if sur_damier(y2-2, x2+2):
            if (damier[y2-1,x2+1]==inversecouleur(couleur) or damier[y2-1,x2+1]==inversecouleur_dame(couleur)) and damier[y2-2, x2+2]==0 :
                print("Rejouez pour continuez la prise avec le même pion")
                return False
        if sur_damier(y2+2, x2-2):
            if (damier[y2+1,x2-1]==inversecouleur(couleur) or damier[y2+1,x2-1]==inversecouleur_dame(couleur)) and damier[y2+2, x2-2]==0 :
                print("Rejouez pour continuez la prise avec le même pion")
                return False
        if sur_damier(y2+2, x2+2):
            if (damier[y2+1,x2+1]==inversecouleur(couleur) or damier[y2+1,x2+1]==inversecouleur_dame(couleur)) and damier[y2+2, x2+2]==0 :
                print("Rejouez pour continuez la prise avec le même pion")
                return False
    return True

def creer_dame(damier):                         #change les pions en dames quand les conditions sont bonnes
    i: int
    j : int
    i = 0
    for j in range (0, nombre_case):
        if damier[i, j]==3:
            damier[i,j] = 9
    
    i = 9
    for j in range (0, nombre_case):
        if damier[i,j]==5:
            damier[i,j]=2

    return(damier)

def milieu(x1, y1, x2, y2):                     #nous permet de faire les prises
    return (y1+y2)//2, (x1+x2)//2

def nb_blanc(damier):                           #compte le nombre de pions blancs et de dames blanches 
    i : int
    j : int
    nbr_pion_b = 0
    for i in range (0, nombre_case):
        for j in range (0, nombre_case):
            if damier[i,j]==3 or damier[i,j]==9 :
                nbr_pion_b += 1
    return nbr_pion_b

def nb_noir(damier):                            #compte le nombre de pions noirs et les dames noires 
    i : int
    j : int
    nbr_pion_n = 0
    for i in range (0, nombre_case):
        for j in range (0, nombre_case):
            if damier[i,j]==5 or damier[i,j]==2 :
                nbr_pion_n += 1
    return nbr_pion_n

def case_libre(couleur, nbr_cases_libre):       #trouve toutes les cases libres (qui contiennent un 0)
    nbr_cases_libre = 0
    for i in range(0, nombre_case):
        for j in range(0, nombre_case):
            if couleur==5:
                if damier[i,j]==3 or damier[i,j]==9:
                    if sur_damier(i - 1, j - 1):
                        if damier[i - 1, j - 1] == 0:
                            nbr_cases_libre +=1
                    if sur_damier(i - 1, j + 1):
                        if damier[i - 1, j + 1] == 0:
                            nbr_cases_libre +=1
            elif couleur==3:
                if damier[i,j]==5 or damier[i,j]==2:
                    if sur_damier(i + 1, j - 1):
                        if damier[i + 1, j - 1] == 0:
                            nbr_cases_libre +=1
                    if sur_damier(i + 1, j + 1):
                        if damier[i + 1, j + 1] == 0:
                            nbr_cases_libre +=1
    if nbr_cases_libre != 0:
        print("Le jeu continue !")
    return nbr_cases_libre

def condition_victoire(damier, couleur):        #permet de mettre un terme a la partie si les conditions de victoires sont réunies
    autour_libre = case_libre(couleur, nbr_cases_libre)
    nb_blancs = nb_blanc(damier)
    nb_noirs = nb_noir(damier)
    if nb_blancs == 0 :
        print("Le joueur aux pions noir a gagné") 
        return True   
    elif nb_noirs == 0 :
        print("Le joueur au pions blancs a gagné")
    elif (autour_libre == 0) and verification(damier,inversecouleur(couleur))==False :
        print(annonce_victoire(couleur))
        return True
    else:
        return False

def annonce(couleur):                           #permet l'alternance du print joueur
    if couleur == 5:
        print("Tour du joueur aux pions noirs")
    if couleur == 3:
        print("Tour du joueur aux pions blancs")
        
def annonce_victoire(couleur):                  #sert à l'annonce de la victoire dans le cas de blocage
    if couleur == 3:
        print("Le jour aux pions blancs a gagné")
    if couleur == 5:
        print("Le jour aux pions noirs a gagné")

for i in range(0, 3, 2):                        #on rempli le damier des pions noirs et blancs
    for j in range(1, 10, 2):
        damier[i,j]=n
        
for i in range(1, 4, 2):
    for j in range(0, 9, 2):
        damier[i,j]=n
        
for i in range(6, 9, 2):
    for j in range(1, 10, 2):
        damier[i,j]=b
        
for i in range(7, 10, 2):
    for j in range(0, 9, 2):
        damier[i,j]=b
        
        
print(damier)


victoire = False

while victoire == False :
    Tour = False                                #on initialise le tour a False
    case_vide = True                            #on réinitialise case_vide dans le cas ou il a été laissé à False à la fin d'une tentative de déplacement d'une dame sur plusieurs cases qui n'a pas aboutit
    print("Rappel : Pion blanc : 3, Pion noir : 5, Dame blanche : 9, Dame noire : 2")       #Rappel aux joueurs la description des pions
    annonce(couleur)                            #annonce quel est le joueur qui doit jouer 
    while Tour==False:                          #tant que le tour n'est pas égal à True, le joueur rejoue son tour, Tour est True si et seulement si un joueur va jusqu'au bout d'un déplacement
        choix_coo = False                       #permet de s'assurer que le joueur choisi un pion de sa couleur
        prise = verification(damier, couleur)   #type: ignore #donne la valeur a prise qui nous sert a faire la prise obligatoire
        while choix_coo==False:                 #tant que le joueur ne sélectionne pas un de ses pions, il recommence la sélection
            x1=int(input("Entrez la coordonnée X du pion que vous souhaitez bouger (exemple X;Y) : "))      #choix de la coordonnée qui correspond au j
            y1=int(input("Entrez la coordonnée Y du pion que vous souhaitez bouger (exemple X;Y) : "))      #choix de la coordonnée qui correspond au i
            if damier[y1,x1]==couleur or damier[y1,x1]==dame(couleur):                                      #verification que le joueur sélectionne bien un de ses pions
                choix_coo = True
            else:
                print("Cette coordonnée ne renvoie pas à un de vos pions")                                  #le joueur n'a pas sélectionner un de ses pions ou une de ses dames, il recommence
            
        #on vient de vérifier que le premier joueur a bien sélectionner son pion


        x2=int(input("Entrez la coordonnée X2 de l'endroit ou vous voulez bouger le pion (exemple X;Y) : "))    #le joueur sélectionne la coordonnée d'arrivée correspondant au j
        y2=int(input("Entrez la coordonnée Y2 de l'endroit ou vous voulez bouger le pion (exemple X;Y) : "))    #le joueur sélectionne la coordonnée d'arrivée correspondant au i
        
        #on vient de sélectionner les coordonnées d'arrivée
        
        x1=x1   #j'initialise x1 qui a été entré précedemment pour éviter les lignes d'erreurs dans le code
        y1=y1   #j'initialise y1 qui a été entré précedemment pour éviter les lignes d'erreurs dans le code
        
        if (x2-x1>0) and (y2-y1>0):                             #utile dans le cas ou la dame doit effectuer une prise en bas à droite
            x3=int(x2-1)
            y3=int(y2-1)
            x4=int(x2-2)
            y4=int(y2-2)
        elif (x2-x1<0) and (y2-y1>0):                           #utile dans le cas ou la dame doit effectuer une prise en bas à gauche
            x3=int(x2+1)
            y3=int(y2-1)
            x4=int(x2+2)
            y4=int(y2-2)
        elif (x2-x1>0) and (y2-y1<0):                           #utile dans le cas ou la dame doit effectuer une prise en haut à droite
            x3=int(x2-1)
            y3=int(y2+1)
            x4=int(x2-2)
            y4=int(y2+2)
        elif (x2-x1<0) and (y2-y1<0):                           #utile dans le cas ou la dame doit effectuer une prise en haut à gauche
            x3=int(x2+1)
            y3=int(y2+1)
            x4=int(x2+2)
            y4=int(y2+2)
        
        #cette boucle if n'est utile que dans le cas ou le joueur voudra effectuer une prise avec sa dame
        
        x3=x3   #j'initialise x3 qui a été entré précedemment pour éviter les lignes d'erreurs dans le code 
        y3=y3   #j'initialise y3 qui a été entré précedemment pour éviter les lignes d'erreurs dans le code
        x4=x4   #j'initialise x4 qui a été entré précedemment pour éviter les lignes d'erreurs dans le code
        y4=y4   #j'initialise y4 qui a été entré précedemment pour éviter les lignes d'erreurs dans le code
        
        
        if sur_damier(y2,x2):       #on verifie que les coordoonées de damier[y2,x2] sont bien dans le damier, sinon le joueur les ressaisis
            if damier[y1,x1]==3 and -1<=x1-x2<=1 and x1-x2!=0 and y1-y2==1 and damier[y2,x2]==0 and prise== False:      #le pion doit etre dirigé en diagonale, vers une case vide
                damier[y2,x2]=damier[y1,x1]                                                                             #la case d'arrivée prends la valeur de la case de départ
                damier[y1,x1]=0                                                                                         #la case de départ est maintenant vide dû au déplacement du pion
                print("Le pion a été déplacé")
                Tour = True                                                                                             #le tour est donc égal à True car le déplacement est fait
                #déplacement simple d'un pion blanc
                
            elif damier[y1,x1]==5 and -1<=x1-x2<=1 and x1-x2!=0 and -1==y1-y2 and damier[y2,x2]==0 and prise== False:   #le pion doit être dirigé en diagonale, vers une case vide
                damier[y2,x2]=damier[y1,x1]                                                                             #la case d'arrivée prends la valeur de la case de départ
                damier[y1,x1]=0                                                                                         #la case de départ est maintenant vide dû au déplacement du pion
                print("Le pion a été déplacé")
                Tour = True                                                                                             #le tour est donc égal à True car le déplacement est fait
                #déplacement simple d'un pion noir
            
            elif ((-2==x1-x2 and y1-y2==2) or (2==x1-x2 and -2==y1-y2) or (-2==x1-x2 and -2==y1-y2) or (2==x1-x2 and y1-y2==2)) and prise==True:    #le pion effectue une prise
                damier[milieu(x1, y1, x2, y2)]=0                                                                                                    #la case du pion qui va être pris devient vide
                damier[y2,x2]=damier[y1,x1]                                                                                                         #la case d'arrivée qui était vide prends la valeur du pion qui prend
                damier[y1,x1]=0                                                                                                                     #la case de départ est maintenant vide
                print("Le pion a été pris")
                Tour = rejouer(damier, couleur, x2, y2)                                                                                             #le tour prends la valeur de la fonction rejouer, qui va detecter si le joueur doit rejouer ou si il ne peut pas
                #prise d'un pion ou d'une dame par un pion de la couleur opposé ou une dame de la couleur opposé
            
            elif damier[y1,x1]==dame(couleur) and damier[y2,x2]==0 and x1!=x2 and y1!=y2 and (x2-x1==-1 or x2-x1==1) and ((y2-y1==-1 or y2-y1==1) ) and not ((int(damier[y3,x3])==inversecouleur(couleur) or int(damier[y3,x3])==inversecouleur_dame(couleur)) and int(damier[y4,x4])==0):
                damier[y2,x2]=damier[y1,x1]                                                                             #la case d'arrivée prends la valeur de la case de départ
                damier[y1,x1]=0                                                                                         #la case de départ est maintenant vide dû au déplacement du pion
                print("La dame a été déplacée d'une case")
                Tour = True                                                                                             #le tour est donc égal à True car le déplacement est fait
                #déplacement d'une dame d'une seule case
            
            elif damier[y1,x1]==dame(couleur) and damier[y2,x2]==0 and x1!=x2 and y1!=y2 and (x2-x1==-2 or x2-x1==2) and (y2-y1==-2 or y2-y1==2) and damier[milieu(x1, y1, x2, y2)]==0 and not ((int(damier[y3,x3])==inversecouleur(couleur) or int(damier[y3,x3])==inversecouleur_dame(couleur)) and int(damier[y4,x4])==0):
                damier[y2,x2]=damier[y1,x1]                                                                             #la case d'arrivée prends la valeur de la case de départ
                damier[y1,x1]=0                                                                                         #la case de départ est maintenant vide dû au déplacement du pion
                print("La dame a été déplacée de deux cases")
                Tour = True                                                                                             #le tour est donc égal à True car le déplacement est fait
                #déplacement d'une dame de 2 cases
                
            elif damier[y1,x1]==dame(couleur) and damier[y2,x2]==0 and x1!=x2 and y1!=y2 and not ((int(damier[y3,x3])==inversecouleur(couleur) or int(damier[y3,x3])==inversecouleur_dame(couleur)) and int(damier[y4,x4])==0):
                s=1
                f=1

                if (x2-x1>0) and (y2-y1>0):                             #déplacement de la dame en bas à droite
                    while (x1+f<=x2) and case_vide == True:             #verification que la diagonale allant de la case de départ à la case d'arrivée est bien vide
                        if damier[y1+s,x1+f] != 0:
                            case_vide = False
                        if not x2-x1==y2-y1:                            #verification que le déplacement se fait bien en diagonale
                            print("Ce n'est pas en diagonale, ressaissisez les coordonnées")
                            case_vide = False
                        s+=1
                        f+=1
                elif (x2-x1<0) and (y2-y1>0):                           #déplacement de la dame en bas à gauche
                    while (x1-f>=x2) and case_vide == True:             #verification que la diagonale allant de la case de départ à la case d'arrivée est bien vide
                        if damier[y1+s,x1-f] != 0:
                            case_vide = False
                        if not (y2-y1)==(x2-x1)+2*(y2-y1):              #verification que le déplacement se fait bien en diagonale
                            print("Ce n'est pas en diagonale, ressaissisez les coordonnées")
                            case_vide = False
                        s+=1
                        f+=1
                        
                        
                elif (x2-x1>0) and (y2-y1<0):                           #déplacement de la dame en haut à droite
                    while (x1+f<=x2) and case_vide == True:             #verification que la diagonale allant de la case de départ à la case d'arrivée est bien vide
                        if damier[y1-s,x1+f] != 0:
                            case_vide = False
                        if not (x2-x1)==(y2-y1)+2*(x2-x1):              #verification que le déplacement se fait bien en diagonale
                            print("Ce n'est pas en diagonale, ressaissisez les coordonnées")
                            case_vide = False
                        s+=1
                        f+=1
                elif (x2-x1<0) and (y2-y1<0):                           #déplacement de la dame en haut à gauche
                    while (x1-f<=x2) and case_vide == True:             #verification que la diagonale allant de la case de départ à la case d'arrivée est bien vide
                        if damier[y1-s,x1-f] != 0:
                            case_vide = False
                        if not x2-(x1-f)==y2-(y1-s):                    #verification que le déplacement se fait bien en diagonale
                            print("Ce n'est pas en diagonale, ressaissisez les coordonnées")
                            case_vide = False
                        s+=1
                        f+=1

            
                if case_vide == False:                                  #si le déplacement n'est pas en diagonale, ou que la diagonale n'est pas vide, le tour est False, le joueur recommence 
                    print("Mauvaise coordonnées veuillez réessayer")
                    Tour = False
                elif case_vide == True:                                 #les conditions du déplacement de la dame sont réunies, le déplacement va avoir lieu
                    print("La dame a été déplacée de plusieurs cases") 
                    damier[y1,x1]=0                                     #la case de départ devient vide
                    damier[y2,x2]=dame(couleur)                         #le pion séléctionnant étant obligatoirement une dame, la case d'arrivée contient maintenant une dame de la couleur du joueur en cours
                    Tour=True                                           #le tour a été effectué, le tour est terminé
                #déplacement simple d'une dame de plusieurs cases
                 
            elif damier[y1, x1]==dame(couleur) and damier[y2,x2]==0 and (int(damier[y3,x3])==inversecouleur(couleur) or int(damier[y3,x3])==inversecouleur_dame(couleur)) and int(damier[y4,x4])==0 and x1!=x2 and y1!=y2 :
                '''L'idée ici est décomposer la prise en deux parties, la première consiste a vérifier comme pour un déplacement que la diagonale jusqu'a devant le pion est vide.
                En fonction de l'orientation du déplacement qu'on a vu dans la boucle if qui commence à la ligne 299, on obtient damier[y4,x4] qui représente en réalité la case 
                qui se situe juste avant le pion qui doit être pris. De plus, on a damier[y3,x3] qui représente le pion qui va être pris. On a toujours damier[y2,x2] qui est la case
                d'arrivée finale de la dame, qui doit être vide.
                Une fois qu'on a vérifier que la prise était en diagonale, et que la diagonale jusqu'au pion est vide, on effectue la prise.'''
                
                s=1
                f=1
                if (x4-x1>0) and (y4-y1>0):                             #verification que la diagonale en bas à droite est libre jusqu'à devant le pion
                    while (x1+f<=x4) and case_vide == True:
                        if damier[y1+s,x1+f] != 0:
                            case_vide = False
                        if not x4-x1==y4-y1:                            #verification que le déplacement se fait bien en diagonale
                            print("Ce n'est pas en diagonale, ressaissisez les coordonnées")
                            case_vide = False
                        s+=1
                        f+=1
                        
                elif (x4-x1<0) and (y4-y1>0):                           #verification que la diagonale en bas à gauche est libre jusqu'à devant le pion
                    while (x1-f>=x4) and case_vide == True:
                        if damier[y1+s,x1-f] != 0:
                            case_vide = False
                        if not (y4-y1)==(x4-x1)+2*(y4-y1):              #verification que le déplacement se fait bien en diagonale
                            print("Ce n'est pas en diagonale, ressaissisez les coordonnées")
                            case_vide = False
                        s+=1
                        f+=1
                        
                        
                elif (x4-x1>0) and (y4-y1<0):                           #verification que la diagonale en haut à droite est libre jusqu'à devant le pion
                    while (x1+f<=x4) and case_vide == True:
                        if damier[y1-s,x1+f] != 0:
                            case_vide = False
                        if not (x4-x1)==(y4-y1)+2*(x4-x1):              #verification que le déplacement se fait bien en diagonale
                            print("Ce n'est pas en diagonale, ressaissisez les coordonnées")
                            case_vide = False
                        s+=1
                        f+=1
                        
                elif (x4-x1<0) and (y4-y1<0):                           #verification que la diagonale en haut à gauche est libre jusqu'à devant le pion
                    while (x1-f<=x4) and case_vide == True:
                        if damier[y1-s,x1-f] != 0:
                            case_vide = False
                        if not x4-x1==y4-y1:                            #verification que le déplacement se fait bien en diagonale
                            print("Ce n'est pas en diagonale, ressaissisez les coordonnées")
                            case_vide = False
                        s+=1
                        f+=1

                if case_vide == False:                                  #si le déplacement n'est pas en diagonale ou que la diagonale n'est pas vide jusqu'au pion, il n'y aura pas de prise
                    print("Mauvaise coordonnées veuillez réessayer")
                    Tour = False
                elif case_vide == True:                                 #toutes les conditions sont réunies, la prise va être effectuée
                    print("La dame a pris le pion")
                    damier[y1,x1]=0                                     #la case de départ devient vide
                    damier[y2,x2]=dame(couleur)                         #la case d'arrivée contient donc la dame qui a efféctuée la prise
                    damier[y3,x3]=0                                     #le pion a été pris
                    print(damier)
                    rejouer_dame=int(input("Saisissez 1 si vous POUVEZ poursuivre la prise, saisissez 0 si vous ne POUVEZ PAS : "))     #on donne la possibilité aux joueurs de rejouer dans le cas ou il PEUT poursuivre la prise
                    if rejouer_dame==1:
                        Tour=False
                    elif rejouer_dame==0:
                        Tour=True
                #prise d'un pion ou d'une dame par une dame
                
            else:
                print("Mauvaise coordonnées, réessayez !")          #aucune des possibilités de prise ou de déplacement n'est possible, le joueur recommence son tour jusqu'à réussir un déplacement ou une prise
        
        print(creer_dame(damier))                                   #print le damier et change les pions en dame si besoin
    victoire=condition_victoire(damier, couleur)  # type: ignore    #la victoire prends la valeur boolééenne de la fonction condition de victoire qui donne la victoire à un joueur si ses pions sont immobilisés ou qu'il n'a plus de pions
    couleur=int(inversecouleur(couleur))                            #la couleur change ce qui implique qu'au tour prochain, on change de joueur
print("Bravo au vainqueur ! Fin de la partie.")                     #on sort de la boucle While victoire==False, un joueur à donc gagner, fin de la partie