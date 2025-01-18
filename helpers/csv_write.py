import csv,os,pandas as pd

 
class Csv_w:
    def csvWrite(head,state_data):
        with open("static/lista.csv", "w", encoding="utf-8",newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(head)
            writer.writerows(state_data)
        state_data_json=pd.read_csv(os.path.join('static', 'lista.csv'))
        return state_data_json
