import flask
import os
import markdown

app = flask.Flask(__name__)

app.debug = False




@app.route('/labs/git-getting-started')
def gitlab():
	
	instruction_file = open('labs/git-getting-started.md')
	instruction_text = instruction_file.read()
	instruction_file.close()
	
	return flask.render_template('lab.jinja',instruction_html=markdown.markdown(instruction_text))


if __name__ == "__main__":
	port = int(os.environ.get('PORT',5523))
	app.run(host='0.0.0.0',port=port)