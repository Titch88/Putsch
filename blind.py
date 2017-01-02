# -*-  coding utf8 -*-
import random
import youtube_dl
import asyncio


class Musique :

    def __init__(self, nom, artiste, url):
        self.nom = nom
        self.artiste = artiste
        self.url = url


class Playlist :

    def __init__(self, lst):
        self.liste = lst
        self.current = lst[0]
        self.taille = len(lst)

    def go_next(self):
        for f in range(len(self.liste)) :
            if self.liste[f] == self.current :
                try :
                    self.current = self.liste[f+1]
                    break
                except :
                    self.current = self.liste[0]
                    break






class Game :
    def __init__(self, lst, voice):
        self.joueurs = lst  #Stocker les pseudos des joueurs

        self.scores = len(lst) * [0]
        self.voice = voice

    def score(self, joueur, ctn):
        self.scores[self.joueurs.index(joueur)] = self.scores[self.joueurs.index(joueur)] +  ctn

    def get_score(self, joueur):
        return self.score[self.joueurs.index(joueur)]

    def get_joueur(self, score):
        return self.joueurs[self.scores.index(score)]


