
# Export functions
# ezzel exportáljuk ki egy külső fájlba az összes kérdésre a választ
import reports

text_file = open("output.txt", "w")
text_file.write(str(reports.count_games('game_stat.txt')))
text_file.write("\n")
text_file.write(str(reports.decide('game_stat.txt', 2000)))
text_file.write("\n")
text_file.write(str(reports.get_latest('game_stat.txt')))
text_file.write("\n")
text_file.write(str(reports.count_by_genre('game_stat.txt', 'RPG')))
text_file.write("\n")
text_file.write(str(reports.get_line_number_by_title('game_stat.txt', 'Minecraft')))
text_file.close()
