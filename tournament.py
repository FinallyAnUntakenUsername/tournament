# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensures the user enters one of the csv files
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # Reads teams into memory from file
    f = open(sys.argv[1]) 
    reader = csv.DictReader(f)
    i = 0
    for pie in reader:
        pie['rating'] = int(pie['rating']) 
        teams.append(pie['team'])
        teams[i] = {"team": teams[i], "rating": pie['rating']}
        i += 1;
       
    counts = {}
    i = 0
    # Simulates N tournaments and keep track of win counts
    while i < N:
        x = simulate_tournament(teams)
        if f"{x}" in counts:
            counts[f"{x}"] += 1
        else:
            counts[f"{x}"] = 1
        i += 1
    
    # Prints each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    # Simulates a game and returns True if team1 wins, False otherwise
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability

    
def simulate_round(teams):
    # Simulates games for all pairs of teams and return the winners
    winners = []

    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])
    return winners


def simulate_tournament(teams):
    # Simulates the whole tournament and returns the name of winning team
    while True:
        if len(teams) == 1:
            return teams[0]['team']
        else:
            teams = simulate_round(teams)
        

if __name__ == "__main__":
    main()
