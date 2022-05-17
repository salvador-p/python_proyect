from flask import Flask, request

app = Flask('__main__')

"""Codigo de prueba"""
device = {
    "Name":"1122334455",
    "Last_Name":"Temp.Sensor",
    "Nickname": "Packito_67"
    
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
    return device


if __name__=='__main__':
    app.run(debug=True, port=5000)