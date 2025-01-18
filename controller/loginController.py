from flask import render_template,request,redirect,url_for,session
from app import app
from models.login import NameForm
from models.user import get_user,users,names
from flask_login import logout_user, LoginManager,login_user,current_user

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@app.route('/login2',methods=['GET', 'POST'])
def login2():
    if current_user.is_authenticated:
        return redirect(url_for('index'))   
    form=NameForm()
    if form.validate_on_submit():
        user= get_user(form.name.data)
        if user is not None and user.check_password(form.password.data):
            login_user(names,form.remember_me.data)
            return redirect('home')
        return render_template('login2.html', form=form)  
    return render_template('login2.html', form=form)

@app.route('/logout')    
def logout():
    logout_user()
    return redirect(url_for("login2"))

@app.route('/login2/login2',methods=['POST'])
def login_in2():
    return redirect(url_for("login")) 


@app.route('/login')
def login():
    return render_template("login.html") 


@app.route('/login/login',methods=['POST'])
def login_in():
    nMail = "aa@aa.com"
    npassword = "1234"
    if request.method == "POST":
        mail = request.form['f_mail']
        password= request.form['f_password']
        if mail == nMail and password==npassword:
            return redirect(url_for("countries")) 
        else:
            return redirect(url_for("login")) 

    
    


