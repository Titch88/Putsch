# -*- coding: utf-8 -*-
import time
import random
import sqlite3


conn = sqlite3.connect("quote.db")


def execute_requete(requete) :
    global conn
    try :
        c = conn.cursor()
        c.execute(requete)
        conn.commit()
        c.close()
        return True
    except :
        return False



class Quote :

#       constructeur de classe
#       @assigns Une quote
#       @requires what, when, where = chaine
#       @ensures contructeur

    def __init__(self, what, when, where) :
        self.texte = what
        self.date = when
        self.lieu = where


def addQuote(Q) :
    Q.texte = Q.texte.replace("'", "''")
    rqt = "INSERT INTO quotes (contenu, date, lieu) VALUES( '{0}','{1}','{2}' )".format(Q.texte, Q.date, Q.lieu)
    execute_requete(rqt)


def getQuote(serveur, message = "") :
    global conn
    if message.isnumeric() :
        rqt = "SELECT id, contenu, date FROM quotes WHERE lieu LIKE '%{0}%' AND id =={1}".format(serveur, message)
    else :
        rqt = "SELECT id, contenu, date FROM quotes WHERE lieu LIKE '%{0}%' AND contenu LIKE '%{1}%'".format(serveur, message)  # lieu LIKE '{0}' AND
    cur = conn.cursor()
    cur.execute(rqt)
    liste = cur.fetchall()
    cur.close()

    if len(liste) == 1 :
        retour = "```C\n Quote numero : " + str(liste[0][0]) + "```\n" + liste[0][1]
    else :
        r = random.randrange(0,len(liste) - 1)
        retour = "```C\n Quote numero : " + str(liste[r][0]) + "```\n" + liste[r][1]
    return retour, liste

def countQuote(serveur) :
    global conn

    rqt = "SELECT count(*) FROM quotes WHERE lieu LIKE '%{0}%' ".format(serveur)
    cur = conn.cursor()
    cur.execute(rqt)
    liste = cur.fetchall()
    cur.close()
    print(liste)
    return str(liste[0][0])



def whenQuote(serveur, numero) :
    a = getQuote(serveur, numero)[1]
    return "La quote numero " + str(numero) + " a été enregistrée à " + str(a[0][2])


def delQuote(serveur, numero) :
    rqt = "DELETE FROM quotes WHERE id=={0} AND lieu LIKE '%{1}%' ".format(numero, serveur)
    if execute_requete(rqt) == True :
        return "Suppression reussie"
    else :
        return "Suppression ratée :/"




def initialisation() :

    execute_requete("DROP TABLE IF EXISTS quotes")
    execute_requete("CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY AUTOINCREMENT, contenu TEXT, date TEXT, lieu TEXT)")
    f = open('quotes.txt', "r", encoding='utf8')
    lignes = f.readlines()
    f.close()
    longueur = len(lignes)
    tmp = 0
    for i in lignes :
        g = i.split("&")
        q = Quote(g[1], g[2], "154659533199769601")
        if g[3] == "Wikia Undertale Français" or g[3] == "Wiki Undertale Français" :
            addQuote(q)
