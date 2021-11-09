from flask import Blueprint, render_template


donate = Blueprint('donate',__name__, template_folder='donate_templates')


@donate.route('/donate',methods = ['GET','POST'])

def plzdonate():
    return render_template('donate.html')

