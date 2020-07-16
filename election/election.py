#!/usr/bin/python3.8
# #coding:u8

"""
Democratic election.
"""

from generate_vote import *


nbr_of_voters = 10
median = nbr_of_voters/2

generate_vote(nbr_of_voters)
#display_all_votes()
determine_median_score(median)
score = best_score()
nbr_of_votes = votes(score)
finalists(score, nbr_of_votes)
print(do_we_have_a_winner(score, nbr_of_votes))
show_results()





# cd //home/jaenne/Documents/alternance/tests_algo/election
# ./election.py