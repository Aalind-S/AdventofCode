# Game 2:   1 green, 7 red
        #   1 green, 9 red, 3 blue
#           4 blue, 5 red


# class Game:
#     def __init__(self, game):
#         #self.game = game
#         id_ = game.split(":")
#         self.id = id_[0][-1]
#         self.games = id_[1].split(";")

#     def evaluate(self):
#         for set in self.games:
#             balls = set.split(',') #[4 blue, 5 red]
#             flag = True
#             for ball in balls:
#                 num, color = ball.split(" ")
#                 if int(num) > static[color]:
#                     flag = False
#                     break
#         pass


static = {
    'red': 12,
    'green': 13,
    'blue': 14
}
with open('day2.txt', 'r') as file:
    list2 = file.read().splitlines()

result = [0 for _ in range(len(list2)+1)]

def evaluate(games):
    for game in games:
        id_ =  game.split(":")
        game_id = int(id_[0][5:])
        game = id_[1].split(";")
        result[game_id] = game_id
        for set in game:
            balls = set.split(',') #[4 blue, 5 red]
            for ball in balls:
                _, num, color = ball.split(" ")
                if int(num) > static[color]:
                    result[game_id] = 0
                    #print(" it exceeds", game_id)
                    break
            

evaluate(list2)
print(sum(result))