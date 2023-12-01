num_dict = {'one': 'one1one', 'two': 'two2two', 'three': 'three3three', 'four': 'four4four', 'five': 'five5five', 'six': 'six6six', 'seven':'seven7seven', 'eight': 'eight8eight', 'nine':'nine9nine'}

def part2(input):
    new_input = []
    for string in input:
        for num in num_dict.keys():
            string = string.replace(num, num_dict[num])
        new_input.append(string)
    print(new_input)
    input = new_input
    input = [re.findall(r'\d+', s) for s in input]
    # extract first and last items in list
    input = [[x[0], x[-1] if len(x) > 1 else x[0]] for x in input]
    input = [''.join([x[0], x[-1]] if len(x) > 1 else [x[0], x[0]]) for x in input]
    input = [''.join([x[0], x[-1]] if len(x) > 1 else [x[0]]) for x in input]
    input = [int(x) for x in input]
    print(input)
    # add all the values together
    total = sum(input)
    print(total)


if __name__ == '__main__':
    #read input from file
    with open(r'I:\advent_of_code\puzzle1_input.txt') as f:
        input = f.readlines()
        # remove \n from each line
        input = [x.strip() for x in input]
        print(input)
        part2(input)
