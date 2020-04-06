from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

file = open('model.pkl','rb')
clf = pickle.load(file)
file.close()

@app.route('/', methods=["GET","POST"])
def hello_world():

	if request.method=="POST":
		myDict = request.form
		fever = int(myDict['fever'])
		age = int(myDict['age'])
		pain = int(myDict['pain'])
		runnyNose = int(myDict['runnyNose'])
		diffBreadth = int(myDict['diffBreadth'])


		inputfeatures = [fever,pain,age,runnyNose,diffBreadth]

		#infProbint = clf.predict([inputfeatures])
		infProb = clf.predict_proba([inputfeatures])[0][1]
		print(infProb)
		return render_template('show.html',inf = round(infProb*100))
	return render_template('index.html')
	#return 'hello, world ...!! ' + str(infProb[0][1])

if __name__ == '__main__':
	app.run(debug=True)