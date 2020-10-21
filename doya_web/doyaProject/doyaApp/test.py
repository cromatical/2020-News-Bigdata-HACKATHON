import pandas as pd
import numpy as np
import os


# major_lst2 = os.listdir()

# print(os.listdir())

# current_path = os.getcwd()
# print(current_path)

# # C:\Users\MyLaptop\Desktop\개발\2020_News_Bigdata_HACKATHON\doya_web\doyaProject
# os.chdir(r'doyaProject\doyaApp\data')

# print(os.listdir())


data_path = r'doyaProject\doyaApp\data'
major_fold = os.listdir(data_path)
print(major_fold)


path = os.path.join(data_path + '\전산학&컴퓨터', '2020', '2020_news_data.csv')
print(path)
news_data = pd.read_csv(path, encoding='cp949')
print(news_data)