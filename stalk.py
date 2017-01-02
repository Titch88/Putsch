import sqlite3

conn = sqlite3.connect("stalk.db")


def execute_requete(requete) :
    global conn
    c = conn.cursor()
    c.execute(requete)
    conn.commit()
    c.close()


def test(personne) :
    global conn
    pseudo_serv = personne.nick
    nick = 1
    if personne.nick is None :
        nick = 0
    pseudo_client = str(personne)[:-5]
    id = personne.id
    ident = "id"+str(id)

    execute_requete("CREATE TABLE IF NOT EXISTS {0} (id INTEGER PRIMARY KEY AUTOINCREMENT, client_side TEXT, server_side TEXT )".format(ident))
    rqt = "SELECT id, client_side, server_side FROM {0}".format(ident)
    cur = conn.cursor()
    cur.execute(rqt)
    liste = cur.fetchall()
    cur.close()
    tmp = 1
    for f in liste :
        if nick == 1 :
            if f[1] == pseudo_client and f[2] == pseudo_serv :
                tmp = 0
        else :
            if f[1] == pseudo_client :
                tmp = 0
    if tmp == 1 :
        pseudo_client = pseudo_client.replace("'", "''")
        if nick == 1 :
            pseudo_serv = pseudo_serv.replace("'", "''")
        execute_requete("INSERT INTO {0} (client_side, server_side) VALUES( '{1}','{2}' )".format(ident, pseudo_client, pseudo_serv))
        return get(personne)[1]
    else :
        return None

def get(personne) :
    global conn
    id = "id"+ str(personne.id)

    rqt = "SELECT id, client_side, server_side FROM {0}".format(id)
    cur = conn.cursor()
    cur.execute(rqt)
    liste = cur.fetchall()
    cur.close()
    res = []
    for f in liste :
        if f[1] not in res :
            res.append(f[1])
        if f[2] is not None and f[2] not in res:
            res.append(f[2])
    try :
        res.remove(str(None))
    except :
        pass

    retour = "Cette personne a utilisé les pseudos suivants :  \n  ```"+ " \n".join(res) + "```"
    return retour,res




