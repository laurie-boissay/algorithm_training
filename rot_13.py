#!/usr/bin/python3.8
# #coding:u8

"""
Créer une fonction qui décale chaque lettre de 13 places : Rotate by 13 places.
"""

alphabet_rot_13 = {
	"a" : "n" ,
	"b" : "o" ,
	"c" : "p" ,
	"d" : "q" ,
	"e" : "r" ,
	"f" : "s" ,
	"g" : "t" ,
	"h" : "u" ,
	"i" : "v" ,
	"j" : "w" ,
	"k" : "x" ,
	"l" : "y" ,
	"m" : "z" ,
	"n" : "a" ,
	"o" : "b" ,
	"p" : "c" ,
	"q" : "d" ,
	"r" : "e" ,
	"s" : "f" ,
	"t" : "g" ,
	"u" : "h" ,
	"v" : "i" ,
	"w" : "j" ,
	"x" : "k" ,
	"y" : "l" ,
	"z" : "m" ,
}

def transform_to_rot_13(string_to_transform):
	text = ''
	list_to_transform = list(string_to_transform)

	for i, letter in enumerate(list_to_transform):
		for k, v in alphabet_rot_13.items():
			if letter.lower() == k:
				list_to_transform[i] = v
				
	for i, char in enumerate(list_to_transform):
		text += char

	text += '\n'

	return text

print(transform_to_rot_13('URYYB JBEYQ')) # HELLO WORLD
print(transform_to_rot_13('BCRAPYNFFEBBZF')) # OPENCLASSROOMS
print(transform_to_rot_13('PRPV RFG ZBA PBQR FRPERG')) # CECI EST MON CODE SECRET





















# cd /home/jaenne/Documents/alternance/tests_algo
# ./rot_13.py