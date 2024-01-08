import csv,os,pandas as pd

 
class Csv_w:
    def csvWrite(head,state_data):
        with open("static/lista.csv", "w", encoding="utf-8",newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(head)
            writer.writerows(state_data)
        state_data_json=pd.read_csv(os.path.join('static', 'lista.csv'))
        return state_data_json
    #state_data_json1=os.path.join('static', 'lista.csv')
    #class DecimalEncoder(json.JSONEncoder):
    #def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
       # if isinstance(obj, Decimal):
           # return str(obj)
        # 👇️ otherwise use the default behavior
       # return json.JSONEncoder.default(self, obj)