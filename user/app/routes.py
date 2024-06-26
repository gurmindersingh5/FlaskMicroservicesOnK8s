from .models import User
from . import app, db
from flask import jsonify, request


@app.route('/', methods=['GET'])
def home():
    print('Go to : /api/users/all or /api/users/add or /api/users/<int:user_id>')
    return ('Go to : /api/users/all or /api/users/add or /api/users/<int:user_id>')

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return jsonify({'error : user not found'})
    res = {
        'name' : user.name,
        'email' : user.email,
        'data' : user.data
    }
    return jsonify(res), 200

@app.route('/api/users/all', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{'id : ': user.id, 'name : ': user.name, 'email : ': user.email} for user in users]
    print(users_list)
    return jsonify(users_list), 200

@app.route('/api/users/add', methods=['GET','POST'])
def set_user():
    data = request.get_json()
    if data:
        try:
            name = data.get('name')
            email = data.get('email')
            data = User(
                name=name,
                email=email
            )
            db.session.add(data)
            db.session.commit()
            return jsonify({'suceessfully created user : ': name})
        except Exception as e:
            return jsonify({'error: ': str(e)})
    else:
        return jsonify({'error':'json type header missing'})

