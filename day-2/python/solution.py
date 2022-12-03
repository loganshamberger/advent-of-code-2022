game_matrix = [[3,6,0],[0,3,6],[6,0,3]]
moves = {'A':[0,1],'B':[1,2],'C':[2,3],'X':[0,1],'Y':[1,2],'Z':[2,3]}

def read_file():
    input_file = open('../input.txt','r')
    lines = input_file.readlines()
    return lines

def score(game):
    play = game.split()
    return moves[play[1]][1]+game_matrix[moves[play[0]][0]][moves[play[1]][0]]    

def solution():
    lines = read_file()
    total_score = 0
    for line in lines:
        total_score += score(line)
    print(total_score)

def main():
    solution()

if __name__ == '__main__':
    main()