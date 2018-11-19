# ------------------------- INPUTS ---------------------------

# These will be inputted from a spreadsheet

Team_List = ['Team 1', 'Team 2', 'Team 3', 'Team 5', 'Team 6', 'Team 7', 'Team 8']
Group_Size = 4

# --------------------- Group Sorting ------------------------

# This assigns the number of groups needed for your group stage, ensuring there is one non full group if needs be

if len(Team_List)/Group_Size % 2 > 0.5:
    Groups = round(len(Team_List)/Group_Size)
else:
    Groups = round(len(Team_List)/Group_Size) + 1

# This function checks if there is an odd number of teams and adds a fill if needed
def odd(teams):
    if len(teams) % 2:
        teams.append('NO TEAM')  # if team number is odd - use 'day off' as fake team

odd(Team_List)

# This sorts the teams into seperate groups in a dictionary called group

Group = {}
min = 0

for i in range(0, Groups):
    max = min + Group_Size
    Group["Group {0}".format(i)] = [Team_List[min:max]]
    min = max

# ----------------------- Fixtures ---------------------------

# This function will permutate the teams in a group and make games from these, so each team plays each other once

def fixtures(teams):
    rotation = list(teams)       # copy the list

    fixtures = []
    games = []

    for i in range(0, len(teams)-1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

        for n in range(0, int((len(teams)/2))):
            low = 2*n
            high = low + 1
            games.append(rotation[low] + ', ' + rotation[high])

    return games

print("Fixtures")
print(Groups, int((Group_Size * (Group_Size - 1))/2))

# Here, print it out for each group in sequence with another for loop
for i in range(0, int((Group_Size * (Group_Size - 1))/2)):
    for n in range(0, Groups):
        if "NO TEAM" not in fixtures(Group["Group " + str(n)][0])[i]:
            print("Group " + str(n) + ": " + fixtures(Group["Group " + str(n)][0])[i])