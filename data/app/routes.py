from . import app
from flask import jsonify
import requests
import os

@app.route('/', methods=['GET'])
def home():
    print('try : /api/getdata/<int:user_id>')
    return ('try : /api/getdata/<int:user_id>')

@app.route('/api/getdata/<int:user_id>', methods=['GET'])
def fetch_user_data(user_id):
    user_svc_dns = os.getenv('USER_SVC_DNS')
    user_service_url = f'http://{user_svc_dns}:8082/api/users/{user_id}'
    try:
        res = requests.get(user_service_url)
        print(res)
        return jsonify({'Data : ': res.json()}), 200
    except Exception as e:
        return jsonify({'error : ': str(e)}), 404
