import os
from urllib.request import urlretrieve

cwd = os.getcwd()

os.makedirs(cwd + '\data',exist_ok=True)

url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'

urlretrieve(url1,'.\data\loan1.txt')
urlretrieve(url2,'.\data\loan2.txt')
urlretrieve(url3,'.\data\loan3.txt')

print(os.listdir('.\data'))