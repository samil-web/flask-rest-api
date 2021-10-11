# POST request /projects -→ create project and save it to csv file
# GET request /projects -→ get all projects
# GET request /projects/:id -→ get specific project with id
# DELETE request /projects/:id -→ delete project by id
# PUT request /projects/:id -→ update project by id
# EXTRA
# POST request / projects/:id -→ update cover picture for project
import os

import uuid

import pandas as pd

import boto3

from botocore.exceptions import ClientError

file_path = os.getcwd()

csv_file_path = os.path.join(file_path,'data.csv')

fields = ['name', 'last_name', 'email','password']

aws_access_key_id = os.environ.get('aws_access_key_id')
aws_secret_access_key = os.environ.get('aws_secret_access_key')
aws_bucket_name = os.environ.get('aws_bucket_name')


s3_client = boto3.client("s3",aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)

def update_profile_picture(file, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file.filename)
    try: 
        extension = os.path.splitext(file.filename)[1]
        Key = f"{object_name}{extension}"
        print(Key)
        response = s3_client.upload_fileobj(Bucket=aws_bucket_name, Fileobj=file,Key=Key)
        print(response)
        return response
    except ClientError as e:
        print(e)
        raise Exception("File upload is failed")


def create_csv_file_if_not_exists():
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, 'w') as f:
            f.write(",".join(fields)+"\n")


def create_user(user):
    user['id'] = str(uuid.uuid4())

   
    # read csv file as data frame
    data_frame = pd.read_csv(csv_file_path)

    # appending only values of user dictionary
    data_frame = data_frame.append(user,ignore_index=True)

    # writing data frame to csv file
    data_frame.to_csv(csv_file_path,index=False)

    return user



def read_users():
    """
    read csv file and return json

    """
    csv_file = pd.read_csv(csv_file_path, sep = ",", header = 0, index_col = False)
    df = pd.DataFrame(csv_file)
    """
        convert data frame to json
    """
    json=df.to_json(orient = "records")
    return json

 

def find_user_by_id(id):
    """
        read csv file 
    """
    csv_file = pd.read_csv(csv_file_path, sep = ",", header = 0, index_col = False)
    df = pd.DataFrame(csv_file)
    """ 
        filter data frame by column match
    """
    df=df.loc[df['id'] == id]
    if df.empty:
        raise Exception(f"Profile with id {id} not found")
    else:
        """
           if found get first row and return json
        """
        row = df.iloc[0]
        json=row.to_json()
        return json




def find_user_by_id_and_delete(id):
    """
        read csv file   
    """
    csv_file = pd.read_csv(csv_file_path, sep = ",", header = 0, index_col = False)
    df = pd.DataFrame(csv_file)
    index=df.index[df['id'] == id]
    if df.loc[df['id'] == id].empty:
        raise Exception(f"Profile with id {id} not found")
    else:
        """
         if its found drop it
        """
        df.drop(index,inplace=True)
        df.to_csv(csv_file_path,index=False)
    return None



def find_user_and_update(id,json):
    csv_file = pd.read_csv(csv_file_path, sep = ",", header = 0, index_col = False)
    df = pd.DataFrame(csv_file)
    index=df.index[df['id'] == id]
    if df.loc[df['id'] == id].empty:
        raise Exception(f"Profile with id {id} not found")
    else:
        json["id"]=id
        df=df.drop(index)
        df = df.append(json,ignore_index=True)
        df.to_csv(csv_file_path,index=False)
    return json