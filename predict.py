from flask import Flask
from flask import request
import pandas as pd
import numpy as np
import pickle
app = Flask(__name__)
def enter_here(mileage, year, make_model, years, original_price, Type):
	pl = pickle.load(open( "pl", "rb" ))
	df_ex = pd.DataFrame({'Mileage':float(mileage), 'Year':float(year),'Make_Model':make_model, 'Years': float(years),'Original Price':float(original_price), 'Type':Type},index=[0])
	return 'After %d years and %d mileage, your %s will be worth $%d' % (years, mileage, make_model, pl.predict(df_ex).tolist()[0])
 
@app.route("/predict")
def hello():
	mileage = request.args.get('mileage')
	year = request.args.get('year')
	make_model = request.args.get('make_model').replace('%20', ' ')
	years = request.args.get('years')
	original_price = request.args.get('original_price')
	Type = request.args.get('Type').replace('%20', ' ')
	# print(mileage, year, make_model, years, original_price, Type)
	result = enter_here(int(mileage), int(year), make_model, int(years), int(original_price), Type)
	return result