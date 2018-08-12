from app  import app
from flask import render_template, flash, redirect, url_for, request,session
from app.we import main
from app.forms import LoginForm

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
    user["nickname"]=session.get('name')
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

@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit() :
        session['name'] = main(form.email.data,form.pwd.data)
        return redirect(url_for('index'))
         #flash('Login requested for OpenID="' + form.email.data + '", remember_me=' + str(form.pwd.data))
    return render_template("login.html",title='sign in',form=form)