###### Player Inputs ######


class Player:

    def __init__(self, name,score):
        self.name = name
        self.score = score
        
Player1 = Player('Player1',100)
Player2 = Player('Player2',80)


###### Player Inputs ######

###### Team Set Up ######


class Teamlist:

    def __init__(self, name):
        self.name = name
        self.playernum = 0
        self.players = []    # creates a new empty list for each dog

    def add_playernum(self):
        self.playernum += 1

    def add_players(self, players):
        self.players.append(players)

Teams = 4
Num_Players = int(input('How many players are there?: '))

# This generates 4 teams
Team = {}
for n in range(1, Teams + 1):
    Team["Team {0}".format(n)] = Teamlist('Team '+str(n))

while Num_Players > 0:
    for n in Team.keys():
        Team[n].add_playernum()
        Num_Players -= 1
        if Num_Players == 0:
            break

print('')

for i in Team.keys():
    print("Team: {}, Players: {}".format(i, Team[i].playernum))

###### Team Set Up ######

###### Team Selection ######

for player in player:
    print(player.name())
###### Team Selection ######
