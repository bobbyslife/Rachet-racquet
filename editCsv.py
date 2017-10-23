'''to encode strings in binary, etc'''
import csv
import pandas

fileRead = input('enter file to read: ')
'''encode ioc, tourney level, hand, score,round'''

atp_data = pandas.read_csv(fileRead,header=0)

toDrop=['tourney_id','surface','tourney_level','match_num','winner_id','winner_seed','winner_entry','loser_id','loser_seed','loser_entry','best_of']
for item in toDrop:
	atp_data.drop(item, axis=1)

atp_data.replace(['if_l','lala'],[0,3]) #replace strings

fileWrite= input('enter new file to write. end in .csv: ')

'''
with open(fileRead, 'w', newline='') as csvfile:
	wrote = csv.writer(csvfile)
	wrote.writerow(['draw_size','tourney_level','winner_entry','winner_hand','winner_height','winner_ioc','winner_age','winner_rank','winner_rank_points','loser_entry','loser_height','loser_ioc','loser_age','loser_rank','loser_rank_points','score','best_of','round','minutes','w_ace','w_df','w_svpt','w_1stIn','w_1stWon','w_2ndWon','w_SvGms','w_bpSaved','w_bpFaced','l_ace','l_df','l_svpt','l_1stIn','l_1stWon','l_2ndWon','l_SvGms','l_bpSaved','l_bpFaced'])
'''


