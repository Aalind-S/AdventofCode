
static = {
    'red': 12,
    'green': 13,
    'blue': 14
}
with open('day2.txt', 'r') as file:
    list2 = file.read().splitlines()

result = [0 for _ in range(len(list2)+1)]

#game_set = {}

total = 0
def evaluate(games):
    global total
    for game in games:
        id_ =  game.split(":")
        #game_id = int(id_[0][5:])
        game = id_[1].split(";")
        game_set = [1,1,1] #R G B
        for set in game:
            #print(set)
            balls = set.split(',') #[ 4 blue, 5 red]
            for ball in balls:
                _, num, color = ball.split(" ")
                num = int(num)
                if color == 'green' and num > game_set[1]:
                    game_set[1] =  num
                elif color == 'red' and num > game_set[0]:
                    game_set[0] =  num
                elif color == 'blue' and num > game_set[2]:
                    game_set[2] =  num
    
        r, g, b = game_set
        # game_set = r*g*b
        total += r*g*b



# { 1:[   ] }
evaluate(list2)
print(total)
# for set in game_set:
#     r,g,b = 
# print(sum(result))