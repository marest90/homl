import pandas as pd
import os
#print(pd.__version__)

HOUSING_PATH = 'datasets/'

def load_housing_data(ruta):
	#csv_path = os.path.join(housing_path, "housing.csv")
	datos = pd.read_csv(ruta + 'housing.csv')
	return datos

print('version: 1.00')

print(os.getcwd())
dirlist = os.listdir('./')
print(dirlist)
housing = load_housing_data(HOUSING_PATH)
print(housing.head())
