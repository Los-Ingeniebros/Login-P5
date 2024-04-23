from flask import Blueprint, session, render_template

catalogue = Blueprint('catalogue', __name__, url_prefix='/catalogue')
items = ["item1", "item2", "item3", "item4", "item5", "item6", "item7", "item8", "item9"]
ferfong_items = ["item2", "item4"] #Estos items están simulados.


@catalogue.route('/')
def view_items():
    if session.get('user_id') == None:
        return render_template('catalogue.html', items=items)
    return render_template('catalogue.html', items=ferfong_items)