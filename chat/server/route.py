from flask import (
                   render_template,
                    url_for,
                    session,
                    request,
                    redirect,
                   )

from .import main
@main.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form.get('name','')
        return redirect(url_for('.chat'))
    else:
        return  render_template('index.html')
@main.route('/chat',methods=['GET'])
def chat():
    name = session.get('name','')
    if name == '':
        return redirect(url_for('.index'))
    else:
        return render_template('chat.html')