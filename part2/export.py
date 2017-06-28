
# Export functions
import reports

text_file = open("output.txt", "w")
text_file.write(str(reports.get_most_played('game_stat.txt')))
text_file.write("\n")
text_file.write(str(reports.sum_sold('game_stat.txt')))
text_file.write("\n")
text_file.write(str(reports.get_selling_avg('game_stat.txt')))
text_file.write("\n")
text_file.write(str(reports.count_longest_title('game_stat.txt')))
text_file.write("\n")
text_file.write(str(reports.get_date_avg('game_stat.txt')))
text_file.write("\n")
text_file.write(str(reports.get_game('game_stat.txt', 'Minecraft')))
text_file.close()
