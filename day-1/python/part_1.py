def max_calories():
    input_file = open('../input.txt','r')
    lines = input_file.readlines()

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


def main():
    print(max_calories())

if __name__ == "__main__":
    main()