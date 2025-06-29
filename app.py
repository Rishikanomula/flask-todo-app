from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = '123456789'  # Replace with a secure key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Flask-Login setup
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

# Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Home / Task List
@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        content = request.form['content']
        new_task = Task(content=content, completed=False, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks)

# Delete Task
@app.route('/delete/<int:id>')
@login_required
def delete(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        return "Unauthorized", 403

    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return 'Error deleting task.'

# Complete/Uncomplete Task
@app.route('/complete/<int:id>')
@login_required
def complete(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        return "Unauthorized", 403

    task.completed = not task.completed

    try:
        db.session.commit()
        return redirect('/')
    except:
        return 'Error updating task.'

# Edit Task
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        return "Unauthorized", 403

    if request.method == 'POST':
        task.content = request.form['content']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', task=task)

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please log in.', 'warning')
            return redirect('/login')

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect('/')
    return render_template('register.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect('/')
        else:
            flash('Invalid credentials. Try again.', 'danger')
            return redirect('/login')
    return render_template('login.html')

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
