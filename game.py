"""
Chapitre 11.1

Code simulant un combat.
"""


import utils

from character import Character, Weapon


def run_battle(c1: Character, c2: Character):
	attacker = c1
	defender = c2
	num_turns = 1
	print(f"{attacker.name} starts a battle with {defender.name}!\n")
	while True:
		# TODO: Appliquer l'attaque
		# TODO: Si le défendeur est mort (hp == 0), afficher un message et briser la boucle
		# TODO: Incrémenter le nb de tours et échanger attaquant/défendeur
		pass
	return num_turns
