#!/usr/bin/python3.8
# #coding:u8

# Generate votes for candidates.

from random import randrange


from data import *


def generate_vote(nbr_of_voters):
	for i in range(nbr_of_voters):
		for k, v in all_candidates.items():
			vote = randrange(len(mentions))
			v[vote] += 1

	
def display_all_votes():
	for k, v in all_candidates.items():
		print(k, " : ", v)


def determine_median_score(median):
	for k, v in all_candidates.items():
		nbr_of_votes = 0
		for i in range(len(mentions)):
			nbr_of_votes += v[i]
			if nbr_of_votes >= median:
				scoreboard[k] = [i, nbr_of_votes]
				break


def show_results():
	for k, v in scoreboard.items():
		print(k, ' : ', mentions[v[0]], " for ", v[1], " voters.")


def best_score():
	score = 7
	for k, v in scoreboard.items():
		if v[0] < score:
			score = v[0]
	return score


def votes(score):
	votes = 0
	for k, v in scoreboard.items():
		if v[0] == score and v[1] > votes:
			votes = v[1]
	return votes


def finalists(score, nbr_of_votes):
	for k, v in scoreboard.items():
		if v[0] == score and v[1] == nbr_of_votes:
			final_list.append(k)


def do_we_have_a_winner(score, nbr_of_votes):
	if len(final_list) == 1:
		text = "\nThe winner is : " + final_list[0] + "."
		text += "\nWith the mention " + mentions[score]
		text += " for " + str(nbr_of_votes) + " voters."
	else:
		text = "\nThere will be a second round with :"
		for name in final_list:
			text += "\n- " + name
	return text + "\n"






















# cd //home/jaenne/Documents/alternance/tests_algo/election
# ./generate_vote.py