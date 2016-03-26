from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/topic_results', methods=['POST'])
def get_results():
	topic = request.form["topic"].encode('utf-8')
	stuff = top_results(topic)
	print stuff
	return jsonify({"topic":topic, "stuff":stuff})

if __name__ == '__main__':
    app.run()
