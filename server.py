from flask import Flask, render_template, redirect, request, session
from user import User

app = Flask(__name__)


@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users=users)


# CREATE
@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        "user_name": request.form["user_name"],
        "email": request.form["email"],
    }
    User.create(data)
    return redirect('/')

# READ


@app.route('/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template('show.html', user=user)

# UPDATE


@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template('edit.html', user=user)


@app.route('/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/')

# DELETE


@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
