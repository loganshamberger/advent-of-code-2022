import heapq

def make_heap():
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
    heapq.heapify(elves)
    return elves

def read_file():
    input_file = open('../input.txt','r')
    lines = input_file.readlines()
    return lines

def main():
    elves = make_heap()
    print("Solution to part one: " +str(heapq.nlargest(1,elves).pop()))
    print("Solution to part 2: "+ str(sum(heapq.nlargest(3,elves))))

if __name__ == "__main__":
    main()