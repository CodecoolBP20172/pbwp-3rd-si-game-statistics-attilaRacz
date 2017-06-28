
# Printing functions
# ez printeli ki a konzolra
import reports
import pprint


def pprinter(file_name):
    pp = pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None)
    pp.pprint(reports.count_games('game_stat.txt'))
    pp.pprint(reports.decide('game_stat.txt', 2000))
    pp.pprint(reports.get_latest('game_stat.txt'))
    pp.pprint(reports.count_by_genre('game_stat.txt', 'RPG'))
    pp.pprint(reports.get_line_number_by_title('game_stat.txt', 'Minecraft'))


pprinter('game_stat.txt')
