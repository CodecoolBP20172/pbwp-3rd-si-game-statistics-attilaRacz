
# Printing functions
import reports
import pprint


def pprinter(file_name):
    pp = pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None)
    pp.pprint(reports.get_most_played('game_stat.txt'))
    pp.pprint(reports.sum_sold('game_stat.txt'))
    pp.pprint(reports.get_selling_avg('game_stat.txt'))
    pp.pprint(reports.count_longest_title('game_stat.txt'))
    pp.pprint(reports.get_date_avg('game_stat.txt'))
    pp.pprint(reports.get_game('game_stat.txt', 'Minecraft'))


pprinter('game_stat.txt')
