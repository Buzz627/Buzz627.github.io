from flask import Flask
from flask import jsonify
import json
import datetime
from flask_selfdoc import Autodoc


resume={}

with open("resume/resume.json", "r") as f:
	resume=json.load(f)

print resume.keys()

app = Flask(__name__)
auto = Autodoc(app)

@app.route('/api/resume/', methods=['GET'])
@auto.doc()
def getAll():
	"""Get full resume"""
	return jsonify(resume)

@app.route('/api/resume/work/<int:num>', methods=['GET'])
@auto.doc()
def getHistory(num = None):
	"""Get last <num> items from work history"""
	history=[]
	if num != None:
		history=resume["work"][:int(num)]
	else:
		history=resume["work"]
	return jsonify(history)

@app.route('/api/resume/work/years/<int:num>/', methods=['GET'])
@auto.doc()
def getHistoryYear(num = 0):
	"""Get work history for the last <num> years"""
	result=[]
	currentTime=datetime.datetime.now()
	limit=datetime.datetime(currentTime.year-num, currentTime.month, currentTime.day)
	for job in resume["work"]:
		if "endDate" not in job:
			end=currentTime
		else:
			try: 
				end=datetime.datetime.strptime(job['endDate'], "%Y-%m-%d")
			except:
				end=datetime.datetime.strptime(job['endDate'], "%Y-%m")
		if limit <= end:
			result.append(job)

	return jsonify(result)



@app.route("/api/resume/<item>/", methods=['GET'])
@auto.doc()
def getItem(item):
	"""Get a specific <item> from resume. (['interests', 'basics', 'skills', 'work', 'languages', 'awards', 'education', 'volunteer']"""
	print item
	return jsonify(resume[item])


@app.route("/api/docs", methods=['GET'])
def geDocs():
	return auto.html(title='API Resume Documentation ',
	author='Buzz Lakata')