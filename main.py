#### Imports et définition des variables globales

import random

FILENAME = "corpus.txt"
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
VOYELLES = list("aeiouy")
CONSONNES = list("bcdfghjklmnpqrstvwxz")

#### Fonctions secondaires

def read_data(filename):
    with open(filename, mode='r', encoding="utf8") as f:
        mots = f.readlines()
    return [ mot.strip() for mot in mots ]


def ensemble_mots(filename):
    """retourne les mots contenus dans filename

    Args:
        filename (str): nom du fichier

    Returns:
        list: la liste des mots

    """
    return set(read_data(filename))


def mots_de_n_lettres(mots, n):
    """retourne le sous ensemble des mots de n lettres

    Args:
        mots (set): ensemble de mots
        n (int): nombre de lettres

    Returns:
        set: sous ensemble des mots de n lettres
    """
    return { mot for mot in mots if len(mot) == n }


def mots_avec(mots, s):
    """retourne le sous ensemble des mots incluant la lettre l

    Args:
        mots (set): ensemble de mots
        s (str): chaine de caractères à inclure

    Returns:
        set: sous ensemble des mots incluant la chaine de caractères s
    """
    return { mot for mot in mots if s in mot }


def cherche1(mots, start, stop, n):
    """Retourne le sous-ensemble des mots de n lettres commençant par start et finissant par stop.

    Args:
        mots (set): ensemble de mots
        start (str): préfixe
        stop (str): suffixe
        n (int): nombre de lettres

    Returns:
        set: sous-ensemble des mots correspondant aux critères.

    """
    return { mot for mot in mots if len(mot) == n and mot.startswith(start) and mot.endswith(stop) }


def cherche2(mots, lstart, lmid, lstop, nmin, nmax):
    """
    Retourne le sous-ensemble de mots correspondant à plusieurs critères.

    Args:
        mots (set): ensemble de mots
        lstart (list): liste de préfixes possibles
        lmid (list): liste de chaînes de caractères à inclure
        lstop (list): liste de suffixes possibles
        nmin (int): nombre de lettres minimum
        nmax (int): nombre de lettres maximum

    Returns:
        set: sous-ensemble de mots filtrés
    """
    if not lstart or not lmid or not lstop:
        return set()

    mots_par_longueur = {mot for mot in mots if nmin <= len(mot) <= nmax}

    ensemble_start = {mot for mot in mots_par_longueur if any(mot.startswith(s) for s in lstart)}
    ensemble_mid = {mot for mot in mots_par_longueur if any(s in mot for s in lmid)}
    ensemble_stop = {mot for mot in mots_par_longueur if any(mot.endswith(s) for s in lstop)}

    return ensemble_start & ensemble_mid & ensemble_stop

# def cherche2(mots, lstart, lmid, lstop, nmin, nmax):
#     """retourne le sous ensemble des mots de n lettres commençant par lstart, contenant lmid et finissant par lstop

#     Args:
#         mots (set): ensemble de mots
#         lstart (str): première lettre
#         lmid (str): lettre à inclure
#         lstop (str): dernière lettre
#         nmin (int): nombre de lettres minimum
#         nmax (int): nombre de lettres maximum

#     Returns:
#         set: sous ensemble des mots de n lettres commençant par lstart, contenant lmid et finissant par lstop

#     """
    # good_length = { mot for mot in mots if len(mot) >= nmin and len(mot) <= nmax }
    # start = set()
    # mid = set()
    # stop = set()
    # for mot in good_length:
    #     for s in lstart:
    #         if mot.startswith(s):
    #             start.add(mot)
    #     for s in lstop:
    #         if mot.endswith(s):
    #             stop.add(mot)
    #     for s in lmid:
    #         if s in mot:
    #             mid.add(mot)

    # print(start)
    # print(mid)
    # print(stop)

    # return start & mid & stop


#### Fonction principale


def main():
    pass
    # mots = read_data(FILENAME)
    # print( [ mots[i] for i in [24499, 28281, 57305, 118091, 199316, 223435, 336455] ] )
    ens = ensemble_mots(FILENAME)
    # print( [ mot for mot in ["chronophage", "procrastinateur", "dangerosité", "gratifiant"] if mot in ens ] )
    m17 = mots_de_n_lettres(ens, 17)
    print(len(m17))
    print( random.sample(list(m17), 10) )
    # mk = mots_avec(ens, 'k')
    # print(len(mk))
    # print( random.sample(list(mk), 5) )
    # moo = mots_avec(ens, 'oo')
    # print(len(moo))
    # print( random.sample(list(moo), 5) )
    # mz14 = cherche1(ens, 'z', '', 14)
    # print(mz14)
    # m21z = cherche1(ens, '', 'z', 21)
    # print(m21z)
    mab17ez = mots_avec(cherche1(ens, 'sur', 'ons', 17), 'x')
    print(mab17ez)
    res = cherche2(ens, VOYELLES, [], CONSONNES, 21, 21)
    print(res)



if __name__ == "__main__":
    main()





















# def main():
#     mots = liste_mots(FILENAME)
    
#     print( [ mots[i] for i in [24499, 28281, 57305, 118091, 199316, 223435, 336455] ])
#     # ['bachi-bouzouks', 'bayadères', 'coloquintes', 'ectoplasmes', 'macchabées', 'oryctéropes', 'zouaves']
    
#     print([ mot for mot in ["chronophage", "procrastinateur", "dangerosité", "gratifiant"] if mot in mots ])
#     # ['dangerosité', 'gratifiant']
    
#     m7 = mots_de_n_lettres(mots, 7)
#     print(len(m7))
#     # # 27945 mots de 7 lettres
#     print( random.sample(list(m7), 5))

#     mk = mots_avec(mots, 'k')
#     print(len(mk))
#     # # 1621 mots contenant un k
#     print( random.sample(list(mk), 5))

#     m7k = m7 & mk
#     print(len(m7k))
#     # 180 mots de 7 lettres contenant un k

#     mw = mots_avec(mots, 'w')
#     mkw = mk & mw
#     print(len(mkw))
#     # 32 mots contenant un k ET un w

#     mz = mots_avec(mots, 'z')
#     print(len(mz))
#     # 35177 mots contenant un z

#     m_z = { mot for mot in mz if mot.startswith('z')}
#     print(len(m_z))    
#     # 796 mots commençant par z

#     mz_ = { mot for mot in mz if mot.endswith('z')}
#     print(len(mz_))    
#     # 33118 mots terminant par z

#     mznt = mz - m_z - mz_
#     print(len(mznt))
#     # print()
#     # # 1330 mots avec z en position non terminale

#     print(m_z & mz_)

#     print(mznt&mk)

#     m_k = { mot for mot in mk if mot.startswith('k')}
#     print(len(m_k))    
#     # 491 mots commençant par k

#     mk_ = { mot for mot in mk if mot.endswith('k')}
#     print(len(mk_))    
#     # 84 mots terminant par k

#     mknt = mk - m_k - mk_
#     print(len(mknt))
#     # print()
#     # 1052 mots avec k en position non terminale

#     print(mknt&mz)


# if __name__ == "__main__":
#     main()
    



