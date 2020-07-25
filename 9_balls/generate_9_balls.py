#!/usr/bin/python3.8
# #coding:u8



"""
Functions used to generate 9 balls.
8 balls weigh the same.
1 ball has an error with an other weight.

Create a list with 9 balls corresponding to the description.
"""

from random import randrange


from balls_list import all_balls


def create_9_balls():
	weight_error = weight = randrange(1,11)
	
	error_ball = randrange(0,9)
	
	for i in range(9):
		all_balls.append(weight)

	while weight_error == weight:
		weight_error = randrange(1,11)
	
	all_balls[error_ball] = weight_error
