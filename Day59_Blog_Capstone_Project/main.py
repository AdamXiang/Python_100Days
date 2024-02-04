from flask import Flask, render_template, url_for
import requests
from post import Post

API = 'https://api.npoint.io/2765297d32c0a7edab68'

app = Flask(__name__)

posts = requests.get(url=API).json()
all_posts = []

for post in posts:
    object_ = Post(post['id'], post['title'], post['subtitle'], post['body'], post['author'], post['date'])
    all_posts.append(object_)


@app.route('/')
def index():
  return render_template('index.html', posts=all_posts)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):
  response_body = None
  for blog in all_posts:
      if blog.id == id:
          response_body = blog
          print(id)

  return render_template('post.html', posts=response_body)

if __name__ == '__main__':
  app.run(debug=True)