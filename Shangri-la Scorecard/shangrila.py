
def main():
	numberOfRounds = 7
	while(True):
		numberOfPlayers = input("Input number of players: ")

		numberOfPlayers = int(numberOfPlayers)
		players = [["",0] for x in range(numberOfPlayers)]

		for i in range(numberOfPlayers):
			players[i] = [raw_input("Name of player {0}: ".format(i+1)),0]


		for i in range(numberOfRounds):
			playRound(players, i+1)
			print("*******CURRENT SCORES*********")
			printPlayerScores(players)


		printWinner(players)

def playRound(players, roundNum):
	switcher = {
		1: "Round 1: 11 cards, 2 sets of 3 of a kind to go down. Good luck!",
		2: "Round 2: 11 cards, 1 set of 3 of a kind and 1 run of 4 to go down. Good luck!",
		3: "Round 3: 11 cards, 2 runs of 4 to go down. Good luck!",
		4: "Round 4: 11 cards, 3 sets of 3 of a kind to go down. Good luck!",
		5: "Round 5: 11 cards, 2 sets of 3 of a kind and a run of 4 to go down. Good luck!",
		6: "Round 6: 11 cards, 1 set of 3 of a kind and 2 runs of 4 to go down. Good luck!",
		7: "Round 7: 12 cards, 3 runs of 4 to go down. Good luck!"
	}
	print(switcher.get(roundNum, "nothing"))

	for i in range(len(players)):
		playerScore = int(raw_input("Enter " + players[i][0] + "'s score: "))
		players[i][1] += playerScore

def printPlayerScores(players):
	for i in range(len(players)):
		print(players[i][0] + " score: " + str(players[i][1]))
	
def printWinner(players):
	lowest = players[0]
	for y in range(1,len(players)):
		if players[y][1] < lowest[1]:
			lowest = players[y]

	print("The winner is " + lowest[0] + " with " + str(lowest[1]) + " points!")

main()


