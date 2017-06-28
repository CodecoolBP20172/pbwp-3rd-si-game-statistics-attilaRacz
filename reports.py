
# Report functions
# ide jönnek a functionok


def count_games(file_name):
    with open(file_name, "r") as f:
        list_games = list(f)
        return len(list_games)


def decide(file_name, year):
    with open(file_name, "r") as f:
        list_games = f.read()
        if str(year) in list_games:
            return True
        else:
            return False


def get_latest(file_name):
    with open(file_name, "r") as f:
        list_games = f.read().strip()
        infos = list_games.split('\n')
        dict_games = {}
        for elements in infos[0:]:
            elements = elements.split('\t')
            dict_games[elements[0]] = elements[2]

        v = list(dict_games.values())
        k = list(dict_games.keys())
        return k[v.index(max(v))]


def count_by_genre(file_name, genre):
        with open(file_name, "r") as f:
            list_games = f.read().strip()
            return list_games.count(genre)


def get_line_number_by_title(file_name, title):
    error_check = True
    with open(file_name, "r") as f:
        for num, line in enumerate(f, 1):
            if line.startswith(title + '\t'):
                error_check = False
                return num
        if error_check:
            raise ValueError
