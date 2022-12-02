

def max_calories():
    lines = read_file()

    current_max = -10000
    current_elf = 0
    for line in lines:
        line= line.rstrip()
        if not line:
            if current_elf > current_max:
                current_max = current_elf
            current_elf=0
        else:
            current_elf = current_elf+int(line)
    return current_max


def read_file():
    input_file = open('../input.txt','r')
    lines = input_file.readlines()
    return lines

def top_three_elves_sum():
    lines = read_file()
    elves= []
    current_elf = 0
    for line in lines:
        line = line.rstrip()
        if not line:
            elves.append(current_elf)
            current_elf = 0
        else:
            current_elf = current_elf + int(line)

    elves.sort(reverse=True)
    return elves[0]+elves[1]+elves[2]

def main():
    print("Solution to part one: " +str(max_calories()))
    print("Solution to part 2: "+ str(top_three_elves_sum()))

if __name__ == "__main__":
    main()