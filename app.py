from flask import Flask, redirect, render_template, url_for, request, flash, session

from controller.catalogue import catalogue

app = Flask(__name__)
app.register_blueprint(catalogue)
app.config['SECRET_KEY'] = 'dev'


@app.route('/')
def hello_world():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id') != None:
        return render_template('login.html', user=session['user_id'])
    if request.method == 'GET':
        return render_template('index.html')
    name = request.form.get('username')
    passwd = request.form.get('password')
    if name == 'ferfong' and passwd == 'Developer123!': #Ustedes van a tener que cambiar esto, por una validación con la DB.
        session['user_id'] = name #definición de cookie de sesión.
        return render_template('login.html', user=name)
    flash('Invalid username or password')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['user_id'] = None
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
