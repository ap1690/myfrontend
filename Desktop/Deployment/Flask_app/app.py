from flask import Flask,render_template,request
import pandas as pd 
import numpy as np 
from sklearn.externals import joblib
app=Flask(__name__)


@app.route('/')
def home():
	return render_template("./home.html")



@app.route('/predict',methods=['GET','POST'])

def predict():
	if request.method=='POST':
		
		try:
			
			name=request.form["name"]
			enrollment_nos=request.form["enrollment_nos"]
			year=request.form["year"]
			sem=request.form["sem"]
			out="Name of the Student :"+name+"\n"+"Enrollment Number: "+enrollment_nos+'\n'+"Result : "+"Bhaag bsdk!!"


		except ValueError:
			return "please check there is some error in output"
	
	return render_template("./predict.html",out=out)









if __name__=="__main__":
	app.run()