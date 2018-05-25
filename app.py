from flask import Flask, render_template, request
from flask_cors import CORS
from models import get_posts, create_post

#create your flask server object
app = Flask(__name__)

CORS(app)

#this is decorator route function that happens when we go to index page
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		name = request.form.get('name')
		post = request.form.get('post')

		create_post(name, post)

	posts = get_posts()

	return render_template('index.html', posts=posts)

if __name__ == '__main__':
	app.run(debug=True)