import os 
# import pandas as pd
import uuid

file_path = os.getcwd()

csv_file_path = os.path.join(file_path,'data.csv')

fields = ['name','last_name','email','password']

def create_csv_file():
    if not os.path.exists(csv_file_path):
        with open(csv_file_path,'w') as f:
            f.write(','.join(fields)+'\n')

def write_user(user):
    """
        add id field for each json
    """
    user["id"]=uuid.uuid4()

    """
        if profile.csv file is not exist, create it and write header of csv file
    """
    if os.path.exists(csv_file_name) is not True:
        csv_file = open(csv_file_name,"w")
        csv_file.write(",".join(fields)) #--> write header of csv.
        csv_file.close()
    """
    append json to csv file as new line
    """
    df = pd.read_csv(csv_file_name)
    df = df.append(json,ignore_index=True)
    df.to_csv(csv_file_name,index=False)
    return user

def read_users():
    """
    read csv file and return json

    """
    csv_file = pd.read_csv(csv_file_name, sep = ",", header = 0, index_col = False)
    df = pd.DataFrame(csv_file)
    """
        convert data frame to json
    """
    json=df.to_json(orient = "records")
    return json