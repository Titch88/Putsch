# -*- coding: utf-8 -*-
import random
import praw


def Decoup(chaine) :
	chaine = chaine.replace('\n',' ')
	tmp = chaine.split(" ")
	res = []
	a = 0
	tmp2 = ""
	for f in tmp :
		if a < 10 :
			tmp2 = tmp2+" "+f
			a = a+1
		if a == 10 :
			res.append(tmp2)
			tmp2 = ""
			a = 0
	res.append(tmp2)
	return res


# https://www.reddit.com/r/jokes/.json?sort=new


def get_new() :
	global last
	UA = "Putsch_undertale"
	r = praw.Reddit(user_agent = UA)
	res = []

	sub = r.get_subreddit('Undertale').get_new(limit = 1)
	tmp = ""
	for g in sub :
		tmp = tmp + g.title+" , url : "+g.short_link+" || "
	print(tmp)
	try :
		if tmp == last :
			last = tmp[0]
			return 'None'
		else :
			last = tmp
			return tmp
	except :
		last = 'None'



	return res

#Sort le titre, le texte et l'url d'un subreddit = arg
def joke(arg = "", link = 0 ) :

	UA = "Nardco fait des blagues"
	r = praw.Reddit(user_agent = UA)
	a = random.randint(0,99)
	if arg != "" :
		subreddit = r.get_subreddit(arg)
	else :
		subreddit = r.get_subreddit('random')
	subs = subreddit.get_hot(limit = 100)
	subs = list(subs)


	titre = (subs[a]).title
	texte = (subs[a]).selftext
	url = (subs[a]).short_link
	texte = texte+ " | url : "+url

	if titre in texte :
		return Decoup(texte.encode('utf8'))

	else :
		return Decoup( (titre+" : "+ texte).encode('utf8'))

	return Decoup("Houston, on a un probleme...")
