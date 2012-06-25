import flask
import os
import markdown

app = flask.Flask(__name__)

app.debug = False



	
@app.route('/labs/<slug>')
def lab_instructions(slug):
	
	try:
		instruction_file = open('labs/%s.md'%slug)
		instruction_text = instruction_file.read()
		instruction_file.close()
		return flask.render_template('lab.jinja',instruction_html=markdown.markdown(instruction_text))

	except IOError:
		return flask.abort(404)
		
@app.route('/getting-solutions')
def solution_instructions():
	
	instruction_file = open('getting-solutions.md')
	instruction_text = instruction_file.read()
	instruction_file.close()
	
	return flask.render_template('lab.jinja',instruction_html=markdown.markdown(instruction_text))

if __name__ == "__main__":
	port = int(os.environ.get('PORT',5523))
	app.run(host='0.0.0.0',port=port)