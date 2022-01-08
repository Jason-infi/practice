import os
from urllib.request import urlretrieve
from math import ceil
import pandas as pd

cwd = os.getcwd()

os.makedirs(cwd + '\data',exist_ok=True)

url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'

urlretrieve(url1,'.\data\loan1.txt')
urlretrieve(url2,'.\data\loan2.txt')
urlretrieve(url3,'.\data\loan3.txt')

def get_headers(data):
    headers = data.strip().split(',')
    return headers

def get_values(data):
    values = []

    for value in data.strip().split(','):
        if value == '':
            values.append(0.0)
        else:
            try:
                values.append(float(value))
            except ValueError:
                values.append(value)
    return values

def create_dict(headers,values):
    data_dict = {}
    for head,value in zip(headers,values):
        data_dict[head] = value
    
    return data_dict


def read_csv(file_path):

    with open(file_path,'r') as file_txt:
        file_txt_data = file_txt.readlines()
        headers = get_headers(file_txt_data[0])
        data_list = []

        for data in file_txt_data[1:]:
            values = get_values(data)
            data_dict = create_dict(headers,values)
            data_list.append(data_dict)
    
    return data_list


def loan_emi(amount, duration, rate, down_payment=0):
    loan_amount = amount - down_payment
    try:
        emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount / duration
    emi = ceil(emi)
    return emi

def compute_emi(loans):

    for loan in loans:
        loan['emi'] = loan_emi(loan['amount'],loan['duration'],loan['rate'],loan['down_payment'])


loan1_data = read_csv('.\data\loan1.txt')
compute_emi(loan1_data)

loan1_df = pd.DataFrame(loan1_data)

loan1_df.to_csv('loan1_data.csv',index = None)

data = pd.read_csv('loan1_data.csv')

data_dict = data.to_dict('records')

print(data_dict)
            
