"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	UNARMED_POWER = 20
	
	# TODO: __init__
	
	# TODO: Propriétés
	
	# TODO: make_unarmed


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""




def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	# TODO: Afficher le résultat
	pass


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, nb tours, etc.
	# TODO: Pour toujours:
		# TODO: Appliquer l'attaque
		# TODO: Si le défendeur est mort, afficher un message et briser la boucle
		# TODO: Incrémenter le nb de tours et échanger attaquant/défendeur
	# TODO: Retourner nombre de tours effectués
	pass
