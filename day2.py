RED = 12
GREEN = 13
BLUE = 14

def part1(input):
    # split each line create a dictionary
    game_dict = {}
    for x in input:
        y = x.split(':')
        game_dict[y[0].split()[1]] = y[1]
    for key, value in game_dict.items():
        v = value.split(';')
        l = []
        for z in v:
            l.append(tuple(z.split(',')))
        game_dict[key] = l
    impossible_list = []
    for key, value in game_dict.items():
        key_added = False
        for set_of_balls in value:
            if key_added:
                continue
            for balls in set_of_balls:
                key_added = False
                ball = balls.strip()
                if 'blue' in ball:
                    number = ball.split()[0]
                    if int(number) > BLUE:
                        impossible_list.append(key)
                        key_added = True
                elif 'red' in ball:
                    number = ball.split()[0]
                    if int(number) > RED:
                        impossible_list.append(key)
                        key_added = True
                elif 'green' in ball:
                    number = ball.split()[0]
                    if int(number) > GREEN:
                        impossible_list.append(key)
                        key_added = True
    possible_set = set(game_dict.keys() - set(impossible_list))
    possible_list = [int(p) for p in list(possible_set)]
    print(sum(possible_list))

def part2(input):
    # split each line create a dictionary
    game_dict = {}
    for x in input:
        y = x.split(':')
        game_dict[y[0].split()[1]] = y[1]
    for key, value in game_dict.items():
        v = value.split(';')
        l = []
        for z in v:
            l.append(tuple(z.split(',')))
        game_dict[key] = l
    game_results = {}
    for key, value in game_dict.items():
        red_count = 1
        green_count = 1
        blue_count = 1
        for colours_tuple in value:
            # 1 green, 1 red, 2 blue
            for colour in colours_tuple:
                colour = colour.strip()
                if 'red' in colour:
                    r_count = colour.split()[0]
                    if int(r_count) > red_count:
                        red_count = int(r_count)
                elif 'green' in colour:
                    g_count = colour.split()[0]
                    if int(g_count) > green_count:
                        green_count = int(g_count)
                elif 'blue' in colour:
                    b_count = colour.split()[0]
                    if int(b_count) > blue_count:
                        blue_count = int(b_count)
        game_results[key] = (red_count, green_count, blue_count)
    result = []
    for value in game_results.values():
        result.append(value[0]*value[1]*value[2])
    print(sum(result))


if __name__ == '__main__':
    #read input from file
    with open(r'I:\advent_of_code\puzzle2_input.txt') as f:
        input = f.readlines()
        # remove \n from each line
        input = [x.strip() for x in input]
        print(input)
        part1(input)
        part2(input)
