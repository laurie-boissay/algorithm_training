#!/usr/bin/python3.8
# #coding:u8



"""
I've eared about a problem :

We have 9 balls all weigh the same except one that weigh more.
How find this different ball with only 2 comparative weighings ?

This program is my response to this question.
"""


from generate_9_balls import create_9_balls
from balls_list import *


# We need 9 balls corresponding to the description.
# weights of balls are in all_balls list.
create_9_balls()

# Create 3 groups of 3 balls.
group_1.append(all_balls[0])
group_1.append(all_balls[1])
group_1.append(all_balls[2])

group_2.append(all_balls[3])
group_2.append(all_balls[4])
group_2.append(all_balls[5])

group_3.append(all_balls[6])
group_3.append(all_balls[7])
group_3.append(all_balls[8])

# Weigh group 1.
weight_group_1 = group_1[0] + group_1[1] + group_1[2]

# Weigh group 2.
weight_group_2 = group_2[0] + group_2[1] + group_2[2]

# We need a list to give as argument to the following function.
groups_to_compare = [weight_group_1, weight_group_2]


def comparative_weighings(object_list_to_compare):
	# Compare 2 objects 0 and 1:
	# if weight object 0 > weight object 1:
	if object_list_to_compare[0] > object_list_to_compare[1]:
		# error = object 0
		error = 0

	# if weight object 0 == weight object 1:
	elif object_list_to_compare[0] < object_list_to_compare[1]:
		# error = object 1
		error = 1
	
	else: #object_list_to_compare[0] == object_list_to_compare[1]
		# error = object 2
		error = 2

	return error + 1


error_group_number = comparative_weighings(groups_to_compare)

if error_group_number == 1:
	error_ball = comparative_weighings(group_1)

elif error_group_number == 2:
	error_ball = comparative_weighings(group_2) + 3

else: # error_group_number == 3:
	error_ball = comparative_weighings(group_3) + 6


# Display error :
print(f"\nThe number of the heaviest ball is : {error_ball}.")

print("\nLet's check the weight of each ball :\n")
for i in range(9):
	print(f"Ball n°{i+1} : {all_balls[i]} g.")

print("\n")

