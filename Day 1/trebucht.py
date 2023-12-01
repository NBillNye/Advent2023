import re

def calibrationValues(line):
    numbers = re.findall(r'\d+', line)
    number = int(str(numbers)[0])*10 + numbers%10
    return number

def calibrationSum(input):
    sum = 0
    for line in input:
        sum += calibrationValues(line)
    return sum
        

def main():
    input = open("trebucht.txt", "r")

    print(calibrationSum(input))
    
if __name__ == "__main__":
    main()