from flask import Flask, request

app = Flask('__main__')

"""Codigo de prueba"""
device = {
    "Name":"Salvador",
    "Last_Name":"Perez",
    
}

@app.route('/devices', methods=['GET'])
def go_home():
    return device

@app.route('/users', methods=['POST'])
def save_user():
    user = request.json
    print(user)
    return user

@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    print(device)
    return device, 201


if __name__=='__main__':
    app.run(debug=True, port=5000)