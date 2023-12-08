import re

def calibrationValues(line):
    #numbers = re.findall(r'\d+', line)
    num = ""
    for c in line:
        if c.isdigit():
            num = num + c
    print(num)
    number = num[0] + str(int(num)%10)
    return number

def calibrationSum(input):
    sum = 0
    for line in input:
        sum += int(calibrationValues(line))
    return sum
        

def main():
    input = open("trebucht.txt", "r")

    print(calibrationSum(input))
    
if __name__ == "__main__":
    main()