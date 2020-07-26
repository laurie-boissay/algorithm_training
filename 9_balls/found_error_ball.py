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


def weigh_balls(group):
	# Weigh 2 balls 0 and 1:
	# if weight ball 0 > weight ball 1:
	if group[0] > group[1]:
		# error = ball 0
		error = 0

	# if weight ball 0 == weight ball 1:
	elif group[0] < group[1]:
		# error = ball 1
		error = 1
	
	else: #group[0] == group[1]
		# error = ball 2
		error = 2

	return error + 1


# Weigh group 1.
weight_group_1 = group_1[0] + group_1[1] + group_1[2]

# Weigh group 2.
weight_group_2 = group_2[0] + group_2[1] + group_2[2]

# else if (weight group 1 > weight group 2):
if weight_group_1 > weight_group_2:
		# the error is in the group 1.
		# weigh 2 balls in group 1:
		error_ball = weigh_balls(group_1)

# else (weight group 1 < weight group 2):
elif weight_group_1 < weight_group_2:
		# the error is in the group 2.
		# weigh 2 balls in group 2:
		error_ball = weigh_balls(group_2) + 3

else: # weight_group_1 == weight_group_2
	# the error is in the group 3.
	# weigh 2 balls in group 3:
	error_ball = weigh_balls(group_3) + 6


# Display error :
print(f"\nThe number of the different ball is : {error_ball}.")

print("\nLet's check the weight of each ball :\n")
for i in range(9):
	print(f"Ball n°{i+1} : {all_balls[i]} g.")

print("\n")

