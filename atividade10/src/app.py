from datetime import timedelta, datetime, timezone
from flask import Flask, render_template, session, redirect, url_for, request, make_response

app = Flask(__name__)

app.secret_key = 'EXA844'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)

@app.route('/login')
def login():
    session['logged_in'] = True
    session.permanent = True
    session['login_time'] = datetime.utcnow()
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('login_time', None)
    resp = make_response(render_template('home.html'))
    return resp

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def index():
    if 'logged_in' in session and session['logged_in']:
        counter = request.args.get('counter',default=0, type=int) + 1
        time_remaining = app.config['PERMANENT_SESSION_LIFETIME'] - (datetime.now(timezone.utc) - session['login_time'])
        minutes, seconds = divmod(time_remaining.seconds, 60)
        date_log = request.cookies.get('date_log')
        resp = make_response(render_template('index.html', minutes=minutes, seconds=seconds, date_log=date_log, counter=counter))
        
        if(date_log == '' or date_log is None):
            resp.set_cookie('date_log', str(datetime.now(timezone.utc)))
            
        return resp
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


