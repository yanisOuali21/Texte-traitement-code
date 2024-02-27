def moyenne(liste_note : list[int], liste_coeff : list[int])-> float:
    """Renvoie la moyenne de toutes les notes en prenant compte de leurs coefficients.

    Précondition : len(liste_note) == len(liste_coeff)
    Exemple(s) :
    $$$ moyenne([10,15,20], [1,1,1])
    15
    $$$ moyenne([15,16,17] ,[2,1,3])
    16.166666666666668
    """
    res = 0
    nb_note = 0
    for i in range(len(liste_note)):
        res = res + liste_note[i]*liste_coeff[i]
    for e in liste_coeff:
        nb_note = nb_note + e
    return res/nb_note
def echantillonne(n : int, chaine : str)-> str:
    """Renvoie une chaine contenant un échantillonage d'un caractere sur n de chaine.

    Précondition : 0<n<len(chaine) 
    Exemple(s) :
    $$$ echantillonne(3, 'azertyuiop')
    'arup'
    """
    res = ''
    for i in range(len(chaine)):
        if i%n == 0:
            res = res + chaine[i]
    return res

def miroir(chaine : str)-> str:
    """Renvoie la chaine inversé.

    Précondition : 
    Exemple(s) :
    $$$ miroir('azerty')
    'ytreza'

    """
    res = chaine[::-1]
    return res

def minimum(liste : list[int]) -> int:
    """Renvoie le plus petit élément de la liste.

    Précondition : len(liste) != 0
    Exemple(s) :
    $$$ minimum([12,14,11])
    11
    $$$ minimum([1,2,3])
    1
    """
    liste_tampon = [liste[0]]
    for e in liste:
        if e < liste_tampon[0]:
            liste_tampon[0] = e
    return liste_tampon[0]

def ajout_tiret(liste : list[str]) -> str:
    """Renvoie une chaine de caractere avec un tiret entre chaque mot.

    Précondition : 
    Exemple(s) :
    $$$ ajout_tiret(["n\'est", 'il', 'pas', 'vrai ?'])
    "n\'est-il-pas-vrai ?"
    $$$ ajout_tiret(['vrai ?'])
    'vrai ?'
    """
    res = ''
    for e in liste:
        if e == liste[-1]:
            res = res + e
        else:
            res = res + e + '-'
    return res

def decoupage(texte : str, separateur : str) -> list[str]:
    """Découpe la phrase et met les mots dans une liste.

    Précondition : separateur ne doit pas être vide
    Exemple(s) :
    $$$ decoupage('Tu as fini tes devoirs ? Non, pas encore.', ',.; !?')
    ['Tu', 'as', 'fini', 'tes', 'devoirs','', '','Non','','pas', 'encore']
    $$$ decoupage('','.')
    []

    """
    liste_tampon = []
    res = []
    mot = ''
    for e in separateur:
        liste_tampon.append(e)
    for i in range(len(texte)):
        if texte[i] not in liste_tampon:
            mot = mot+texte[i]
        else:
            res.append(mot)
            mot = ''
    return res

def matchs(liste1 : list[str], liste2 : list[str]) -> list[tuple[str,str]]:
    """Renvoie les matchs possibles.

    Précondition : 
    Exemple(s) :
    $$$ matchs(['Tous avec Montfort', 'Seniors de Montjoie'], ['Bleus de Geix', 'En avant Saint Jean', "L'avenir"])
    [('Tous avec Montfort', 'Bleus de Geix'), ('Tous avec Montfort', 'En avant Saint Jean'), \
('Tous avec Montfort', "L'avenir"),('Seniors de Montjoie', 'Bleus de Geix'), ('Seniors de Montjoie', 'En avant Saint Jean'), ('Seniors de Montjoie', "L'avenir")]
    """
    res = []
    for e in liste1:
        for e2 in liste2:
            res.append((e,e2))
    return res
def compte_motif(chaine1 : str, chaine2 : str)-> int:
    """Renvoie le nombre de motif dans la chaine

    Précondition : 
    Exemple(s) :
    $$$ compte_motif('la','lalala')
    3
    $$$ compte_motif('la', 'bonjour')
    0
    """
    compteur = 0
    tampon = ''
    for e in chaine2:
        tampon = tampon + e
        if tampon == chaine1:
            compteur = compteur + 1
            tampon = ''
    return compteur

def premieres_occurrences(chaine : str)-> str:
    """Renvoie une chaine contenant la premiere occurence.

    Précondition : 
    Exemple(s) :
    $$$ premieres_occurrences("abbbaabcd")
    'ababcd'
    """
    res = ''
    derniere_lettre = ''
    for e in chaine:
        if derniere_lettre == e:
            derniere_lettre = e
        else:
            res = res + e
            derniere_lettre = e
    return res

def repete(chaine : str, liste : list[int])-> str:
    """Renvoie une chaine de caractere avec les lettres repetes un nombres de fois.

    Précondition : len(liste) > len(chaine)
    Exemple(s) :
    $$$ repete("abcd", [3, 0, 2, 1])
    'aaaccd'
    $$$ repete("boom", [2,5,6,9])
    "bbooooooooooommmmmmmmm"
    $$$ repete("",[2,5,30])
    ""
    """
    res = ""
    for i in range(len(chaine)):
        res = res + chaine[i]*liste[i]
    return res


def suffixes(chaine : str) -> list[str]:
    """renvoie la liste de ses suffixes.

    Précondition : 
    Exemple(s) :
    $$$ suffixes('fin')
    ['', 'n', 'in', 'fin']
    $$$ suffixes('')
    ['']
    """
    res = ['']
    chaine_a_ajouter = ''
    chaine_reverse = miroir(chaine)
    for e in chaine_reverse:
        chaine_a_ajouter = chaine_a_ajouter + e
        res.append(miroir(chaine_a_ajouter))
    return res
    

def resume(chaine : str ) -> str:
    """Renvoie la chaîne résumée de la chaîne chaine qui indique le nombre d’occurrences consécutives de chaque caractère

    Précondition : None
    Exemple(s) :
    $$$ resume("abbbaabc")
    '1a3b2a1b1c'

    """
    res = ''
    dernier_lettre_parcouru = chaine[0]
    compteur = 0
    for i in range(1,len(chaine)):
        if chaine[i] == dernier_lettre_parcouru:
            compteur = compteur + 1
        else :
            compteur = compteur + 1
            res = res + str(compteur) + dernier_lettre_parcouru
            dernier_lettre_parcouru = chaine[i]
            compteur = 0
    res = res + str(compteur+1) + dernier_lettre_parcouru
    return res


def construit_mots(mots1 : list[str] , mots2 : list[str]) -> list:
    """Renvoie la liste des mots possibles en appariant les mots des listes

    Précondition : 
    Exemple(s) :
    $$$ 

    ""
