def make_list():
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
    return elves

def read_file():
    input_file = open('../input.txt','r')
    lines = input_file.readlines()
    return lines

def main():
    elves = make_list()
    print("Solution to part one: " +str(elves[0]))
    print("Solution to part 2: "+ str(sum(elves[:3])))

if __name__ == "__main__":
    main()