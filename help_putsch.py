

def get_help(topic = "general") :
    if topic == "general" :
        return "**topic d'aides disponibles : ** \
        \n```quote, hug, ship, birth, blind, date, meow ``` \
        \n Bot par **Titch** aka maitre du monde "

    elif topic == "quote" :
        return "```!getquote <machin> : obtenir une quote à propos de machin \
        \n Note : bonjour je suis bite peut etre trouvé en tapant : !getquote bonjour % bite \
        \n!addquote <quote> : ajoute une quote (Si pas d'argument : msg precedent)\
        \n!whenquote <numero> : connaitre la date d'une quote\
        \n!countquote : Compter le nombre de quotes du serveur```"

    elif topic == "hug" :
        return "```!hug @quelqu'un : Faire un calin à quelqu'un\
        \n!hug : Faire un calin a la derniere personne qui a envoyé un message```"

    elif topic == "ship" :
        return "```\n!ship <numero> : Mettre <numero> personnes en couple, au hasard\
        \n!ship undr <numero> : Mettre <numero> personnes en couple, en mixant avec des personnages d\'Undertale```"

    elif topic == "birth" :
        return "```!birth : Renvoie votre date de naissance\
        \n!birth @quelqu'un : Renvoie la date de naissance de quelqu\'un\
        \n!birth jj/mm/aaaa : Enregistre votre date de naissance ```"

    elif topic == "blind" :
        return "``` \n!blind join : rejoindre/quitter le blindtest\
        \n!blind start : commencer le blindtest\
        \n!blind reset : reset le blindtest \
        \n NB : necessité d'ecrire les reponses en MAJUSCULES```"

    elif topic == "date" :
        return "```!date @quelqu'un' : affiche la date de creation de compte discord et de join du serveur de @quelqu'un'\ ```"

    elif topic == "meow" :
        return "```!meow : faire apparaitre une photo de chat tout mignon ```"
    else :
        return "Pas d'aide pour ce topic"





