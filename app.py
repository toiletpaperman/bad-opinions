from flask import Flask, render_template
from forms import RegistrationForm, LogInForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '1a140434f825e64c129469c12f1246bc'

posts = [
    {
        'author' : 'Johna',
        'title' : 'Blog post', 
        'content' : 'yeet beats mageets',
        'date' : '2 Dec'
    },
    {
        'author' : 'Bob',
        'title' : 'Blog post', 
        'content' : 'yeet beats mageets',
        'date' : '5 Dec'
    }
]

app.config['FLASK_APP'] = 'app.py'
app.config['FLASK_DEBUG']=1

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)
    
@app.route('/about')
def about():
    return 'About'

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LogInForm()
    return render_template('login.html', title='Log In', form=form)

if __name__ == '__main__':
    app.run(debug=True)