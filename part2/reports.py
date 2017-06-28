
# Report functions


def get_most_played(file_name):
    with open(file_name, "r") as f:
        all_games = f.read().strip()
        lines = all_games.split('\n')
        game_infos = []
        for elements in lines:
            elements = elements.split('\t')
            game_infos.append(elements[1])
        list_keys = []
        for elements in lines:
            elements = elements.split('\t')
            list_keys.append(elements[0])
        list_values = []
        for item in game_infos:
            list_values.append(float(item))
        games_sold_dict = dict(zip(list_keys, list_values))
        values = list(games_sold_dict.values())
        keys = list(games_sold_dict.keys())
        return keys[values.index(max(values))]


def sum_sold(file_name):
    with open(file_name, "r") as f:
        all_games = f.read().strip()
        lines = all_games.split('\n')
        game_infos = []
        for elements in lines:
            elements = elements.split('\t')
            game_infos.append(elements[1])
        numbers_sold = []
        for item in game_infos:
            numbers_sold.append(float(item))
        return sum(numbers_sold)


def get_selling_avg(file_name):
    with open(file_name, "r") as f:
        all_games = f.read().strip()
        lines = all_games.split('\n')
        game_infos = []
        for elements in lines:
            elements = elements.split('\t')
            game_infos.append(elements[1])
        numbers_sold = []
        for item in game_infos:
            numbers_sold.append(float(item))
        return (sum(numbers_sold) / len(lines))


def count_longest_title(file_name):
    with open(file_name, "r") as f:
        all_games = f.read().strip()
        lines = all_games.split('\n')
        game_titles = []
        for elements in lines:
            elements = elements.split('\t')
            game_titles.append(elements[0])
        return len(max(game_titles, key=len))


def get_date_avg(file_name):
    with open(file_name, "r") as f:
        all_games = f.read().strip()
        lines = all_games.split('\n')
        game_infos = []
        for elements in lines:
            elements = elements.split('\t')
            game_infos.append(elements[2])
        numbers_sold = []
        for item in game_infos:
            numbers_sold.append(int(item))
        return round(sum(numbers_sold) / len(lines))


def get_game(file_name, title):
    error_check = True
    with open(file_name, "r") as f:
        all_games = f.read().strip()
        lines = all_games.split('\n')
        for num, line in enumerate(lines, 1):
            if line.startswith(title + '\t'):  # +\tavoids picking wrong ones
                error_check = False
                for elements in line:
                    elements = elements.split('\t')
                line_list = line.split('\t')
                line_list[1] = float(line_list[1])
                line_list[2] = int(line_list[2])
                return line_list
        if error_check:
            print("The game is not in the list.")
