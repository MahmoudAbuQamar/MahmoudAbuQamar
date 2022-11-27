import pandas as pd
import numpy as np

date_dict = {'2021': 
{'04': {'30': '21915.70'},
 '05': {'06': '7615.70','07': '7596.82','31': '8771.82'},
'06': {'10': '77311.82', '11': '57222.14', '12': '37222.14' ,'13': '37204.44', '14': '17086.44' ,'15':
'7039.24' ,'16': '7015.64' ,'28': '11956.64' ,'30': '3130.64'} ,
'07': {'01': '3107.04' ,'31': '4282.04'},
'08': {'31': '5456.04'}, 
'09': {'12': '5438.34' ,'27': '6612.34'},
'10': {'12': '2612.34', '13': '2579,30',
'25': '66947.30' ,'26': '6900.10', '27': '6852.90', '28': '2852.90' ,'31': '4067.90'},
'11': {'01': '67.90','10': '2067.90', '30': '3242.90'} ,
'12': {'02': '2763.90' ,'10': '2616,40' ,'11': '2598.70', '31':
'3773.70'}} ,
'2022': {'01': {'03': '1473.70' ,'31': '2647.70'} ,
'02': {'08': '6648.70' ,'10': '2648,70',
'14': '648,70', '23': '3691069.70', '24': '421010.70','25': '21010.70', '26': '5010.70', '28':
'6143.70'} ,
'03': {'07': '18343.70' ,'10': '8343.70', '13': '8326.00' ,'26': '9502.00'}}}

date_dict_1 =list(date_dict.keys())
years = []
months = []
for i in date_dict_1:
    date_dict_2 = list(date_dict[i].keys())
    x = len(date_dict_2)
    for j in range(x):
        years.append(i)
    for j in date_dict_2:
        months.append(j)
headers = years + months
headers = np.array(headers).reshape(2,len(headers)//2)

headers = list(map(lambda n : list(n),headers))

indexs = ['BALANCE AS ON 10TH','BALANCE AS ON 20TH','BALANCE AS ON LAST DAY']

#Data :
mIndex = ['10','20']
data = []
for key,year in enumerate(headers[0]):
    x = date_dict[year][headers[1][key]]
    date_dict_3 = x.keys()
    for i in mIndex:
        try:
            data.append(x[i])
        except:
            try:
                data.append(x['07'])
            except:
                data.append('00')
    try:
        data.append(x['30'])
    except:
        try:
            data.append(x['31'])
        except:
            data.append('00')
data = list(map(lambda n :float(n.replace(',','')),data))
data = np.array(data).reshape(12,3)
data = data.T

data = pd.DataFrame(data,index=indexs,columns=headers)
print(data)
