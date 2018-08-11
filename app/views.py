from flask import render_template
from app  import app
@app.route('/')
@app.route('/index')
def index():
    user={"nickname":'wuchao',"age":33}
    posts=[
       {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title = 'Home', user = user,posts = posts)

@app.route('/about')
def about():
    user={"name":'about'}
    return '''<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['name'] + '''</h1>
  </body>
</html>
'''