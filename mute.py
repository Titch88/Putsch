# coding -*- utf-8 -*-
import discord

def get_mute(fichier) :
    fi = open(fichier, 'r')
    res = fi.readlines()
    fi.close()
    return res

def add_mute(fichier,ident,pseudo) :
    fi = open(fichier, 'a')
    fi.write(ident)
    fi.write("\n")
    fi.close()
    return "Okay, j'ai rendu muet "+pseudo+" !"

def del_mute(fichier, ident, pseudo) :
    fi = open(fichier, 'r')
    tmp = fi.readlines()
    fi.close()
    ident = ident
    fi = open(fichier, 'w')
    for f in tmp :
        if f != ident :
            fi.write(f)
    fi.close()
    return "Ok, j'ai rendu la parole à "+pseudo+" !"
