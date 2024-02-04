from flask import Flask, render_template
from post import Post
import requests

API = 'https://mocki.io/v1/00d0cad2-2454-49a6-9ca8-32073f256366'
response_body = requests.get(API).json()
post_objects = []
for post in response_body:
    object_ = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(object_)


app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html", articles=post_objects)

@app.route('/post/<int:id>')
def read_post(id):
    response_body = None
    for blog in post_objects:
        if blog.post_id == id:
            response_body = blog
            print(id)

    return render_template('post.html', article=response_body)

if __name__ == "__main__":
    app.run(debug=True)
