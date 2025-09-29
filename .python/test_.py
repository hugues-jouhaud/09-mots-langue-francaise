import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import cherche2, read_data

FILENAME = "corpus.txt"

@pytest.fixture(scope="module")
def setup():
    try:
        data = read_data(FILENAME)
    except:
        data = []
    return data


def test_cherche2_debut_milieu_fin():
    ensemble_mots = {'programmation', 'python', 'codage', 'algorithme'}
    lstart = ['pro', 'py']
    lmid = ['ram', 'cod']
    lstop = ['ion', 'me']
    longueur = (5, 15)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'programmation', 'algorithme'}

def test_cherche2_debut_vide():
    ensemble_mots = {'programmation', 'python', 'codage', 'algorithme'}
    lstart = []
    lmid = ['ram', 'cod']
    lstop = ['ion', 'me']
    longueur = (5, 15)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'programmation', 'algorithme'}

def test_cherche2_milieu_vide():
    ensemble_mots = {'programmation', 'python', 'codage', 'algorithme'}
    lstart = ['pro', 'py']
    lmid = []
    lstop = ['ion', 'me']
    longueur = (5, 15)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'programmation', 'python'}

def test_cherche2_fin_vide():
    ensemble_mots = {'programmation', 'python', 'codage', 'algorithme'}
    lstart = ['pro', 'py']
    lmid = ['ram', 'cod']
    lstop = []
    longueur = (5, 15)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'programmation'}

def test_cherche2_tous_listes_vides():
    ensemble_mots = {'programmation', 'python', 'codage', 'algorithme'}
    lstart = []
    lmid = []
    lstop = []
    longueur = (5, 15)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'programmation', 'python', 'codage', 'algorithme'}

def test_cherche2_longueur_min():
    ensemble_mots = {'prog', 'python', 'code'}
    lstart = ['py']
    lmid = ['yth']
    lstop = ['on']
    longueur = (6, 10)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'python'}

def test_cherche2_longueur_max():
    ensemble_mots = {'programmation', 'python', 'codage'}
    lstart = ['pro']
    lmid = ['ram']
    lstop = ['ion']
    longueur = (5, 12)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'programmation'}

def test_cherche2_aucun_mot_correspond():
    ensemble_mots = {'prog', 'codage', 'python'}
    lstart = ['xyz']
    lmid = ['abc']
    lstop = ['uvw']
    longueur = (5, 10)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == set()

def test_cherche2_juste_un_mot():
    ensemble_mots = {'algorithme'}
    lstart = ['algo']
    lmid = ['rit']
    lstop = ['me']
    longueur = (5, 20)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'algorithme'}

def test_cherche2_aucun_mot():
    ensemble_mots = set()
    lstart = ['pro']
    lmid = ['ram']
    lstop = ['ion']
    longueur = (5, 15)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == set()

def test_cherche2_mots_de_taille_minimale():
    ensemble_mots = {'pr', 'py', 'co'}
    lstart = ['pr', 'py']
    lmid = []
    lstop = []
    longueur = (2, 2)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'pr', 'py'}

def test_cherche2_mots_de_taille_maximale():
    ensemble_mots = {'programmation', 'python', 'codage'}
    lstart = ['pro', 'py']
    lmid = []
    lstop = []
    longueur = (5, 10)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'python', 'codage'}

def test_cherche2_commence_par_et_se_termine_par():
    ensemble_mots = {'promotion', 'program', 'position'}
    lstart = ['pro']
    lmid = []
    lstop = ['tion']
    longueur = (5, 15)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'promotion'}

def test_cherche2_juste_milieu():
    ensemble_mots = {'parallèle', 'codage', 'programmation'}
    lstart = []
    lmid = ['lle', 'gram']
    lstop = []
    longueur = (5, 20)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'parallèle', 'programmation'}

def test_cherche2_mot_contenant_milieu_mais_pas_fin():
    ensemble_mots = {'programmation', 'python', 'codage', 'algorithme'}
    lstart = ['pro']
    lmid = ['ram']
    lstop = ['me']
    longueur = (5, 15)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == set()

def test_cherche2_mot_contenant_toutes_conditions():
    ensemble_mots = {'programmation', 'paradoxal', 'codex'}
    lstart = ['pro', 'par']
    lmid = ['ado']
    lstop = ['al']
    longueur = (5, 20)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'paradoxal'}

def test_cherche2_mot_tres_court():
    ensemble_mots = {'a', 'ab', 'abc'}
    lstart = ['a']
    lmid = []
    lstop = ['b', 'c']
    longueur = (1, 2)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'ab'}

def test_cherche2_pas_de_mot_de_cette_longueur():
    ensemble_mots = {'algorithme', 'python', 'codage'}
    lstart = []
    lmid = []
    lstop = []
    longueur = (20, 25)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == set()

def test_cherche2_tous_mots_filtrés_par_milieu():
    ensemble_mots = {'programmation', 'python', 'codage'}
    lstart = []
    lmid = ['xyz']
    lstop = []
    longueur = (5, 20)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == set()

def test_cherche2_liste_mot_unique_pas_filtré():
    ensemble_mots = {'seulement'}
    lstart = ['se']
    lmid = []
    lstop = []
    longueur = (5, 10)
    assert cherche2(ensemble_mots, lstart, lmid, lstop, longueur) == {'seulement'}


