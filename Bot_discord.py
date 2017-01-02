import discord
import asyncio
import time
import random as rand
import pickle as cpk
import help_putsch
from datetime import date
from meow import meow
import blind
import quote
import binary
import stalk
import flame

try:
    f = open('ship.txt', 'rb')
    joueurs = cpk.load(f)
except:  # en theorie, ne sert qu'une fois !
    joueurs = []

try:
    f = open('birth.txt', 'rb')
    birth = cpk.load(f)
except:
    birth = {}


def coller(chaine):
    res = ""
    for f in chaine:
        res = res + f
    return res


def enlever_retours(chaine):
    res = chaine.replace('\n', ' ')
    res2 = res.replace('\r', ' ')
    return res2


def get_birthDay():
    global birth
    today = date.today()
    jj = today.day
    mm = today.month
    aa = today.year
    tmp = str(jj) + "/" + str(mm)
    res = []
    for f in birth:
        date_sans_annee = birth[f].split("/")
        annee = date_sans_annee[2]
        date_sans_annee = date_sans_annee[0] + "/" + date_sans_annee[1]
        if date_sans_annee == tmp:
            res.append(f)
            res.append(int(aa) - int(annee))
    return res


def mention(ID):
    return "<@" + ID + ">"


def get_id(chaine):
    if chaine[2] == "!":
        return (chaine[3:-1])
    else:
        return (chaine[2:-1])


def isint(nombre):
    try:
        nombre = int(nombre)
        return 1
    except:
        return 0



adminlist = ["141962573900808193", "117636215011803145", "85763178692083712", "163274384021127168", "157175506645680129", "176589945383813120"]

# @requires
#   @assigns
#   @ensures renvoie l'heure locale sous la forme Heures:minutes:secondes, le JJ/MM/AAA
#   @utilisation : heure()
def heure():
    a = time.localtime()
    return str(a.tm_hour) + ":" + str(a.tm_min) + ":" + str(a.tm_sec) + ", le " + str(a.tm_mday) + "/" + str(
        a.tm_mon) + "/" + str(a.tm_year)


def isBirthDay(chaine):
    res = chaine.split("/")
    if len(res) == 3:
        if isint(res[0]) and isint(res[1]) and isint(res[2]):
            if int(res[0]) > 0 and int(res[0]) < 32 and int(res[1]) > 0 and int(res[1]) < 13:
                return 1
    return 0


def remove_space(chaine):
    if chaine[0] == " " and chaine[-1] == " ":
        return enlever_retours(chaine[1:-1])
    elif chaine[0] == " ":
        return enlever_retours(chaine[1:])
    elif chaine[-1] == " ":
        return enlever_retours(chaine[:-1])
    else:
        return enlever_retours(chaine)


print("tout va bien")
client = discord.Client()  # aucune idée de ce que ca fait, mais ca marche
print("okay !")

hugcd = time.time()
birthcd = time.time()

liste_joueurs = []
InGame = 0
Game = None
player = None

playlist = []
pl = open('playlist.txt', 'r')
lignes = pl.readlines()
pl.close()
for f in lignes:
    tmp = f.split("&")
    if len(tmp) == 2:
        song = blind.Musique(url=tmp[0], nom=remove_space(tmp[1].lower()), artiste=None)
    elif len(tmp) == 3:
        song = blind.Musique(url=tmp[0], nom=remove_space(tmp[1].lower()), artiste=remove_space(tmp[2].lower()))
    playlist.append(song)

playlist = blind.Playlist(playlist)

@client.event
async def on_ready():  # Ce que le bot fait a sa connexion
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print("Connecté à : ")
    for f in client.servers:
        print(f.name)



@client.event
async def on_member_join(member) :
    canal = member.server.get_channel("164850873074188297")  #Identifiant du general sur undertale wikia
    moi = member.server.get_member(str(client.user.id))
    message = "Bonjour {0}, bienvenue sur le serveur ! Pourrais tu, stp, repondre à ces trois questions ? Age, Sexe, en couple ou non ?".format(member.mention)
    await client.send_typing(canal)
    await asyncio.sleep(5)
    await client.send_message(canal, message)
    await client.change_nickname(moi, "GentilPutsch")
    await client.send_typing(canal)
    await asyncio.sleep(5)
    await client.send_message(canal, "N'ecoute pas ce fou ! t'es pas obligé de repondre ! Quoique... ( ͡° ͜ʖ ͡°) ")
    await client.change_nickname(moi, "Putsch")
    await client.send_typing(canal)
    await asyncio.sleep(2)
    await client.send_message(canal, "Aaaaaargh TAIS TOI !!!! >.< ")









@client.event
async def on_message(message):
    global joueurs
    global hugcd
    global birth
    global birthcd

    global liste_joueurs
    global InGame
    global Game
    global playlist
    global player

    global adminlist



    msg = message.content
    msg = enlever_retours(msg)
    personne = message.author
    canal = message.channel
    serveur = str(message.server)
    # Dans le doute, toujours utiliser la methode str() pour ces trois variables
    # if module_red.get_new() != 'None' :
    #    await client.send_message(client.get_channel('237586260603043842'), module_red.get_new())

    #################### DEBUG ZONE ###############################
    print(client.user.mention)
    print(msg)

    #################################################################


    test = stalk.test(personne)
    if test is not None :
        if len(test) > 2 :

            tmpt = "dis donc toi, t'as vraiment cru que je te verrais pas changer de pseudo ? T'etais pas a l'aise avec ces pseudos ? " + " , ".join(test[-5:-1])
            await client.send_message(canal, tmpt)





    async for message in client.logs_from(canal, limit=10):
        if message.author == client.user and time.time() - hugcd <= 60 and "gros" in message.content:
            cnt = message.content
            add = "= " + str(int(60 - time.time() + hugcd))
            if "TEMPS RESTANT" in cnt:
                cnt = cnt.split("=")[0]
            else:
                add = "TEMPS RESTANT = " + add

            cnt = cnt + add
            await client.edit_message(message=message, new_content=cnt)
    if personne.name not in joueurs:
        joueurs.append(personne.name)
        g = open('ship.txt', 'wb')
        cpk.dump(joueurs, g)
        g.close()

    if time.time() - birthcd > 14400 and get_birthDay() != []:
        ids = get_birthDay()
        print(ids)
        c = 0
        birthcd = time.time()
        while c < len(ids) - 1:
            await client.send_message(canal, "Un bon anniversaire à " + mention(ids[c]) + " ! Felicitations, " + str(
                ids[c + 1]) + " ans aujourd'hui ! ")
            c = c + 2

    if InGame == 1:
        jou = str(personne)[:-5]
        # print(playlist.current.nom.lower())
        # print(playlist.current.artiste.lower())
        # print(jou in Game.joueurs)
        # print(str(msg))
        # print (Game.joueurs)
        # print(playlist.taille)
        msg = "b " + msg + " b "

        if (str(playlist.current.nom) in str(msg).lower() or (
                str(playlist.current.artiste) in str(msg).lower() and str(playlist.current.artiste) != str(
                None))) and jou in Game.joueurs:
            if playlist.current.nom in msg and playlist.current.artiste in msg:
                app = 2
            else:
                app = 1
            Game.score(jou, app)
            await client.send_message(canal, jou + " marque " + str(app) + " point(s) pour ça !")
            playlist.go_next()
            print("A venir : ")
            print(playlist.current.nom)
            print(playlist.current.artiste)
            await client.send_message(canal, " Chanson suivante ...")
            await asyncio.sleep(2)
            player.stop()
            player = await Game.voice.create_ytdl_player(playlist.current.url)
            player.start()

            if max(Game.scores) >= 10:
                win = Game.get_joueur(max(Game.scores))
                await client.send_message(canal, win + " a gagné !")
                Ingame = 0
                Game = None
                liste_joueurs = []
                await client.send_message(canal, "Reset reussi !")

    if msg.startswith('!addquote'):
        if len(msg.split(" ")) > 1:
            msg = msg.split(" ")
            msg.pop(0)
            msg = " ".join(msg)

            q = quote.Quote(msg, heure(), str(message.server.id))
        else:
            # recuperer le msg precedent
            async for message in client.logs_from(canal, limit=2):
                q = message

            q = str(q.author).split("&")[0] + " : " + str(q.content)
            print(" Q EGALE = ", q)
            q = quote.Quote(q, heure(), str(message.server.id))
        try:

            quote.addQuote(q)
            await client.send_message(canal, "Citation enregistrée !")
        except:
            await client.send_message(canal, "euh, how about, no ? ")

    elif msg.startswith('!delquote') and str(personne.id) in adminlist :
        if len(msg.split(" ")) > 1 :
            rep = quote.delQuote( str(message.server.id),  msg.split(" ")[1])
            await client.send_message(canal, rep )
    elif msg.startswith('!delquote') and str(personne.id) not in adminlist :
        await client.send_message(canal, "permission denied")


    elif msg.startswith('!admin') :
        if str(personne.id) in adminlist :
            await client.send_message(canal, "vous etes un admin")
        else :
            await client.send_message(canal, "vous n'etes pas un admin ! ")




    elif msg.startswith('!getquote'):
        msg = str(msg)
        print("msg = ", msg)
        msg = msg.split(" ")
        msg.pop(0)
        msg = " ".join(msg)
        tmp = quote.getQuote(str(message.server.id), msg)
        await client.send_message(canal, tmp[0])

    elif msg.startswith('!whenquote'):
        msg = msg.split(" ")
        if len(msg) > 1:
            await client.send_message(canal, quote.whenQuote(str(message.server.id), msg[1]))
    elif msg.startswith('!countquote'):
        await client.send_message(canal, "Nombre de quotes pour " + serveur + " : " + str(
            quote.countQuote(str(message.server.id))))

    elif msg.startswith('!azerty') :
        splt = msg.split(" ")
        print(splt)
        if len(splt) > 1 :
            cible = get_id(splt[1])
            prs = message.server.get_member(cible)
            await client.send_message(canal, stalk.get(prs)[0])


    elif msg.startswith('fuck') :
        await client.send_typing(canal)
        await asyncio.sleep(5)
        await client.send_message(canal, "Nom de dieu de putain de bordel de merde de saloperie de connard d'enculé de ta mère" )

    elif msg.startswith('!flame') :
        await client.send_typing(canal)
        await asyncio.sleep(5)
        await client.send_message(canal, flame.generer())




    elif msg.startswith('!mute') and "Titch" in str(personne) or msg.startswith('!unmute') and "Titch" in str(personne):
        msg = msg.split(' ')
        if len(msg) > 1:
            id_cible = get_id(msg[1])
            cible = "ce mec"
            if msg[0] == '!mute':
                await client.send_message(canal, mute.add_mute('mutes.txt', id_cible, str(cible)))
            if msg[0] == '!unmute':
                await client.send_message(canal, mute.del_mute('mutes.txt', id_cible + "\n", str(cible)))



    elif "quand" in str(msg).lower() :
        today = date.today()
        aa = today.year + 1

        await client.send_message(canal, "Avant "+str(aa)+" !" )


    elif " yo " in str(msg).lower() and rand.randint(0, 5) == 2 or "yo" in str(msg).lower() and len(
            str(msg).split(" ")) < 3 and rand.randint(0, 5) == 2:
        await client.send_message(canal, "Kai watch !")
    elif 'lenny' in str(msg):  # lenny
        await client.send_message(canal, " ( ͡° ͜ʖ ͡°)")

    elif msg.startswith('help'):
        splt = msg.split(" ")
        if len(splt) == 1:
            await client.send_message(canal, help_putsch.get_help())
        else:
            await client.send_message(canal, help_putsch.get_help(splt[1]))


    elif msg.startswith('!birth'):
        split = msg.split(" ")
        if len(split) == 1:
            try:
                await client.send_message(canal, str(personne)[:-5] + " est né(e) le " + str(birth[personne.id]))
            except:
                await client.send_message(canal,
                                          str(personne)[:-5] + ", utilise ```!birth jj/mm/aaaa``` pour t'enregistrer !")

        else:
            if isBirthDay(split[1]):
                birth[personne.id] = split[1]
                g = open('birth.txt', 'wb')
                cpk.dump(birth, g)
                g.close()
                await client.send_message(canal, str(personne)[:-5] + ", tu as bien enregistré ton anniversaire !")

            else:
                cible = get_id(split[1])
                try:
                    await client.send_message(canal,
                                              str(message.server.get_member(cible))[:-5] + " est né(e) le " + str(
                                                  birth[cible]))
                except:
                    await client.send_message(canal,
                                              str(message.server.get_member(cible))[:-5] + " n'est pas dans la bd ....")


    elif msg.startswith('!hug') and time.time() - hugcd > 60:
        split = msg.split(" ")
        hugcd = time.time()
        print(split)
        for f in message.server.emojis:
            if f.name == "DeterminationSOUL":
                emote = f

        if len(split) > 1:
            cible = split[1]
            print(cible)
            if "everyone" in cible.lower():
                cible = "@everyone"
                send = "OPEN CALINS  !!!! " + mention(personne.id) + " fait un gros calin à " + str(
                    cible) + " ! " + str(emote) + " "

            else:
                cible = mention(get_id(str(cible)))
                send = mention(personne.id) + " fait un gros calin à " + str(cible) + " ! " + str(emote) + " "

            with open('/home/titch/hug.gif', 'rb') as f:
                await client.send_file(canal, f, content=send)
        else:
            async for message in client.logs_from(canal, limit=10):
                q = message
                if message.author != personne:
                    q = message
                    break
            cible = q.author
            with open('/home/titch/hug.gif', 'rb') as f:
                await client.send_file(canal, f, content=mention(personne.id) + " fait un gros calin à " + mention(
                    cible.id) + " ! " + str(emote) + " ")



    elif msg.startswith('!ship') and int(canal.id) == 240835193550667777:
        split = msg.split(" ")
        if len(split) > 1:
            if isint(split[1]):
                nbr = int(split[1])
                if nbr > 5:
                    nbr = 5

                tmp = []
                players = list(joueurs)
                for f in range(nbr):
                    tmp.append(players.pop(rand.randint(0, len(players) - 1)))
                res = ""
                for f in tmp:
                    res = res + "**" + f + "** ``x`` "

                await client.send_message(canal, res[:-6])
            else:
                if len(split) > 2:
                    if split[1] == "undr":
                        if isint(split[2]):
                            nbr = int(split[2])
                            if nbr > 5:
                                nbr = 5
                            tmp = []
                            players = list(joueurs)
                            persos = [" Dacticiel ", "Culgore ", "Puissang ", "Cucticiel ", "Meurtpas ",
                                      " Meurtpas la Démorte ", " Ondine la Démorte ", " Perso ", " Frisquet ",
                                      " Tonne de metta ", " Tonedemeta ", " Rencontréunetonne ", " Rencontrébeaucoup ",
                                      " AlphysDeputt ", " Fleurette ", " Kappa Fleurette ",
                                      " Fleurette Boutiquedeclichés ", " Excepté ", " Parchemin ", " Sieste",
                                      "poignarde", "regarde", " Repognarder ", " McSlip ", " Trodéso ",
                                      " Chienportant ", " Chienple ", " Mannequinsensé ", " Fou crétin ",
                                      " Mannequinandouille ", " Mannequimbécile ", " Manchérubin ", " Manchiard ",
                                      " Manchôme ", " Grillerautour ", " Réservirène ", " Jérigolé ", " Soleignard ",
                                      " Geintbeaucoup ", " Grenouilleça ", " Minuscumoule ", " Ptita ", " Tamoyen ",
                                      " Grauta ", " Grota ", " Fougique ", " Pyrocorde ", " Tête mémoire ",
                                      " Légumoïde ", " Neigecanard ", " Canetoneige ", " Froidcanard ", " Canetofroid ",
                                      " Laveutoa ", " Chapôglace ", " Chapôgelé ", " Aviondere ", " Tsunderport ",
                                      " Muffet à volonté ", " Muffête ", " Ognon", "san ", " Volcanaille ",
                                      " Parsniquer ", " Giftrotte ", " Reinoël ", " Cerf Noël ", " Pain au citron ",
                                      " Personnerivière ", " Rivièreindividu ", " Ruissindividu ", " Individuvial ",
                                      " Personaffluent ", " Toby Renard ", " Toby SiècleRenard ", " Chieant ",
                                      " Cabommerdant ", " Caninsupportable ", " Piafaucheur ", " A.B Fantômeurt ",
                                      " A.B Fantômains ", " Gazétoile"]
                            print(players)
                            for f in range(nbr):
                                if f % 2:
                                    tmp.append(players.pop(rand.randint(0, len(players) - 1)))
                                else:
                                    tmp.append(persos.pop(rand.randint(0, len(persos) - 1)))
                            res = ""
                            for f in tmp:
                                res = res + "**" + f + "** ``x`` "

                            await client.send_message(canal, res[:-6])


    elif msg.startswith('!blind'):
        args = msg.split(" ")
        if args[1] == "join":
            ppl = str(personne)[:-5]
            if ppl not in liste_joueurs:
                liste_joueurs.append(ppl)
                await client.send_message(canal, ppl + " a rejoint la partie !")
            else:
                liste_joueurs.remove(ppl)
                await client.send_message(canal, ppl + " a quitté la partie !")

        elif args[1] == "start" and len(liste_joueurs) >= 1 and InGame == 0:
            await client.send_message(canal, "La partie va commencer, les joueurs sont : " + ", ".join(liste_joueurs))
            # Commencer la partie
            InGame = 1
            chann_blind = client.get_channel("164040287071633408")
            voice = await client.join_voice_channel(chann_blind)
            Game = blind.Game(liste_joueurs, voice)
            player = await voice.create_ytdl_player(playlist.current.url)
            player.start()
            await client.send_message(canal, "Et c'est parti, chanson 1 !")

        elif args[1] == "list":
            await client.send_message(canal, "Liste des joueurs : " + ", ".join(liste_joueurs))

        elif args[1] == "reset":
            Ingame = 0
            Game = None
            liste_joueurs = []
            await client.send_message(canal, "Done !")

    elif "[[" in str(msg) and "]]" in str(msg):
        splt = str(msg).split(" ")
        for f in splt:
            if "[[" in f[:2] and "]]" in f[-2:]:
                await client.send_message(canal, "<http://fr.undertale.wikia.com/wiki/" + f[2:-2] + ">")


    elif msg.startswith('!meow'):
        await client.send_message(canal, meow())

    elif binary.is_binary(str(msg)):
        await client.send_message(canal, binary.convert_from_ascii(str(msg)))

    elif msg.startswith('!date'):
        spl = msg.split(" ")
        if len(spl) >= 2:
            print(spl[1])
            print(get_id(spl[1]))
            print(str(message.server.get_member(get_id(spl[1]))))

            personne = message.server.get_member(get_id(spl[1]))
        date_serv = personne.joined_at
        date_ = personne.created_at
        cnt = str(personne) + " a rejoint le serveur le : " + str(
            date_serv) + "\n et a créé son compte discord le " + str(date_)

        await client.send_message(canal, cnt)


    elif client.user.mention in str(msg.replace("!", "")) :
        msg = msg.replace("!", "")
        msg = msg.replace(client.user.mention, "")
        #cleverbot eventuellement








    elif "Titch" in str(personne):

        if msg.startswith('!initQuote') :
            await client.send_message(canal,quote.initialisation() )

        if msg.startswith('!modreload'):
            reload(quote)
            reload(admin)
            reload(mute)
            await client.send_message(canal, "Merci chef !")

tokenf = open("token.txt", 'r')
token = tokenf.readline()
tokenf.close()

u = str(token.replace("\n", ""))


client.run(u)
