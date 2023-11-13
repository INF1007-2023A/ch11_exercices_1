"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


def compute_damage_output(level, power, attack, defense, crit_chance, random_range):
	level_factor = (2 * level) / 5 + 2
	weapon_factor = power
	atk_def_factor = attack / defense
	critical = random.random() <= crit_chance
	modifier = (2 if critical else 1) * random.uniform(*random_range)
	damage = ((level_factor * weapon_factor * atk_def_factor) / 50 + 2) * modifier
	return int(round(damage)), critical


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

	# TODO: use

	# TODO: compute_damage

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


def run_battle(c1: Character, c2: Character):
	attacker = c1
	defender = c2
	num_turns = 1
	print(f"{attacker.name} starts a battle with {defender.name}!\n")
	while True:
		# TODO: Appliquer l'attaque
		# TODO: Si le défendeur est mort, afficher un message et briser la boucle
		# TODO: Incrémenter le nb de tours et échanger attaquant/défendeur
		pass
	return num_turns 
