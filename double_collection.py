import csv
import os
os.chdir("/home/am-it/Desktop/TalkPython/CSV_Prac")


def find_dulicate():
    unique_record = []
    with open("collection.csv") as fin:
        csv_reader = csv.reader(fin)
        header = next(csv_reader)
        rows = list(csv_reader)
        

        loan_ids = set([loan[3] for loan in rows])
        loan_id_count = {}
        for loan_id in loan_ids:
            count = 0
            for row in rows:
                
                if loan_id == row[3]:
                    count += 1
                    
                    loan_id_count[loan_id] = count
                    
        
        
    with open("collection2.csv","w") as fout:
        csv_writer = csv.writer(fout)
        unique_record=[]
        for row in rows:
            flag = True
            for existing in unique_record:
                if existing[3] == row[3]:
                    flag = False
                    break
            if flag and loan_id_count[row[3]] == 2:
                unique_record.append(row)

                
                
        csv_writer.writerow(header)
        csv_writer.writerows(unique_record)    


       
    
    


       
    

        
            
            


find_dulicate()