from flask import Flask, redirect, render_template, url_for, request, flash, session, Blueprint

from controller.catalogue import catalogue
from modelo import usuario
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ferfong:Develooper123!@localhost:3306/ing_soft'
app.config.from_mapping(
    SECRET_KEY='dev'
)

@app.route('/')
def hello_world():
    print("weaos")
    return redirect(url_for('login'))


@app.route('/tonto', methods=['GET', 'POST'])
def login():
    if session.get('user_id') != None:
        return render_template('login.html', user=session['user_id'])
    if request.method == 'GET':
        return render_template('index.html')
    
    name = request.form.get('username')
    passwd = request.form.get('password')
    
    for registro in usuario.query.all():
            id += 1
            if name == registro.nombre and passwd == registro.password:
                flash("ERROR: Pon otro correo!")
            else:
                session['user_id'] = name #definición de cookie de sesión.
                return render_template('login.html', user=name)
                #break
    

    # if name == 'ferfong' and passwd == 'Developer123!': #Ustedes van a tener que cambiar esto, por una validación con la DB.
    #     session['user_id'] = name #definición de cookie de sesión.
    #     return render_template('login.html', user=name)
    # flash('Invalid username or password')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['user_id'] = None
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()

# -----------------
# from flask import Flask, render_template

# from modelo import db
# # from contollers.MenuControlador import menu_blueprint
# # from contollers.UsuarioControlador import usuario_blueprint
# # from contollers.PeliculaControlador import pelicula_blueprint
# # from contollers.RentarControlador import rentar_blueprint

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:XUHVFImTtBMFHrDjhqcAlMOXLgLhPCAD@roundhouse.proxy.rlwy.net:29472/railway'
# app.config.from_mapping(
#     SECRET_KEY='dev'
# )



# if __name__ == '__main__':
#     app.run()

# ----------------------------------{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}


# from flask import Flask, render_template

# from modelo import db
# # from contollers.MenuControlador import menu_blueprint
# # from contollers.UsuarioControlador import usuario_blueprint
# # from contollers.PeliculaControlador import pelicula_blueprint
# # from contollers.RentarControlador import rentar_blueprint

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:XUHVFImTtBMFHrDjhqcAlMOXLgLhPCAD@roundhouse.proxy.rlwy.net:29472/railway'
# app.config.from_mapping(
#     SECRET_KEY='dev'
# )
# db.init_app(app)
# # app.register_blueprint(menu_blueprint)
# # app.register_blueprint(usuario_blueprint)
# # app.register_blueprint(pelicula_blueprint)
# # app.register_blueprint(rentar_blueprint)

# @app.route('/')
# def hello_world():  # put application's code here
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()