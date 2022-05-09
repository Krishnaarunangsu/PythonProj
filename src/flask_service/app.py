from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    # return 'welcome %s' % name
    return 'Almighty'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = 'Narayan'
        # user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/returnjson', methods=['GET'])
def return_json():
    """
    returns the JSON
    :return:
    """
    if request.method == 'GET':
        data = {
            "Modules": 15,
            "Subject": "Data Structures and Algorithms",
        }

        return jsonify(data)


@app.route('/details$name=<name>$id=<id>', methods=['GET', 'POST'])
def get_details(name, id):
    """
     Get Details of a persons
    :param name:
    :param id:
    :return: JSON Data
    """
    # you can add stuff
    return f"Name: {name}\nId: {id}"


@app.route('/login_details', methods=['GET', 'POST'])
def logins():
    """

    :return:
    """
    username = request.args.get('username')
    password = request.args.get('password')
    return f"Username: {username}\nId: {password}"


@app.route('/user/<string:name>/', methods=['GET', 'POST'])
def user_view(name):
    """

    :param name:
    :return:
    """
    print(name)
    data = {
        "Name": name
    }
    # return f'Name:{name}'
    return jsonify(data)


@app.route('/login_data', methods=['GET'])
def login_data():
    username = request.args.get('username')
    password = request.args.get('password')
    data = {
        "User Name": username,
        "Password": password

    }
    json_data = jsonify(data)
    print(json_data)
    return json_data


if __name__ == '__main__':
    app.run(debug=True)
