#!/usr/bin/python3.8
# #coding:u8



"""
I've eared about a problem :

We have 9 balls all weigh the same except one.
How find this different ball ?

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


def weigh_balls(group, normal_weight):
	# Check all balls weight untill to find the error:
	for ball in range(3):
		# if ball weight != normal_weight:
		if group[ball] != normal_weight :
			# return error
			return ball+1

# Weigh group 1.
weight_group_1 = group_1[0] + group_1[1] + group_1[2]

# Weigh group 2.
weight_group_2 = group_2[0] + group_2[1] + group_2[2]

# If weight group 1 = weight group 2:
if weight_group_1 == weight_group_2:
	# the error is in the group 3.
	# normal_weight of a ball = weight group 1 /3.
	normal_weight = weight_group_1 / 3
	
	# weigh each ball in group 3:
	error_ball = weigh_balls(group_3, normal_weight) + 6

	
# else (weight group 1 != weight group 2):
else:
	# the error is not in the group 3.
	# Weigh group 3.
	weight_group_3 = group_3[0] + group_3[1] + group_3[2]

	# normal weight of a ball = weight group 3 /3.
	normal_weight = weight_group_3 / 3

	# if weight group 1 != weight group 3:
	if weight_group_1 != weight_group_3:
		# the error is in the group 1.
		# weigh each ball in group 1:
		error_ball = weigh_balls(group_1, normal_weight)

	# else (weight_group_2 != weight group 3):
	else:
		# the error is in the group 2.
		# weigh each ball in group 2 :
		error_ball = weigh_balls(group_2, normal_weight) + 3


# Display error :
print(f"\nThe number of the different ball is : {error_ball}.")


print("\nLet's check the weight of each ball :\n")
for i in range(9):
	print(f"Ball n°{i+1} : {all_balls[i]} g.")

print("\n")


