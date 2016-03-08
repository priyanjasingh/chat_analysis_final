import csv
import sys
import os

path = './chats_process'
for filename in os.listdir(path):
	
	filename=filename.split("_")
	first=filename[0]
	second=filename[1]

	#print first
	#print second

	#print "b"
	for i in range(0,19):		
		with open('./chats_process/'+str(first)+'_'+str(second)+'/'+'train_graph_'+str(i)+'.csv','w') as ff:
			with open('./chats_process/'+str(first)+'_'+str(second)+'/'+'train.csv','r') as f1:
				with open('test_negative.csv','r') as f2:
					with open('./chats_process/'+str(first)+'_'+str(second)+'/'+'test_negative_'+str(i)+'.csv','w') as f3:
			
						writer = csv.writer(ff)

						for line in f1:
						
							line = line.replace('\n', '').replace('\r', '')
				
							line=line.split(",")
							line.pop(i)

							writer.writerow(line)
					
						writer = csv.writer(f3)

						for line in f2:
						
							line = line.replace('\n', '').replace('\r', '')
							line=line.split(",")
							line.pop(i)
							writer.writerow(line)
					f3.close()
				f2.close()
			f1.close()
		ff.close()


#def combine_train():

	
