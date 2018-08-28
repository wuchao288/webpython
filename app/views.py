from app  import app
from flask import render_template, flash, redirect, url_for, request,session
from app.we import main
from app.we import countries
from app.forms import LoginForm
import json

@app.route('/')
@app.route('/index')
def index():
    user={"nickname":'wuchao',"age":33}
    user["nickname"]=session.get('name')
    if session.get('name') is None:
        return redirect(url_for('login'))    
    posts=countries()
    dic=json.loads(posts) 
   
    return render_template("index.html", title = 'Home', user = user,posts = dic["data"])

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