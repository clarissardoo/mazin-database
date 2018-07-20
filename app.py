import os
from flask import Flask, send_file, render_template
import json

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def homepage():
	return render_template('meme.html')
	#return send_file(os.path.join(app.config['/'], 'database.html'))


@app.route('/finder')
def finder():
	runs = ['2016B', '2017A', '2017B', '2018A']
	file =[]
	for file in runs:
		for i in range(0, len(runs)):
			file[i].append(runs[i])
		return(file)
		#with open(file +'J.json') as datarunner:
		#	data = json.load(datarunner)
		#	return (json.dumps(data[1]))
				#return redirect(url_for('meme')
				#return(json.dumps(data1[0]))
				#print(data1)
				#return('\n'.join('{}{}'.format(key, val) for key, val in data1[3].items()))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 3000)