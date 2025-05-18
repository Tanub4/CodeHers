from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration (update with your own MySQL credentials)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'newuser'
app.config['MYSQL_PASSWORD'] = 'Aishu123$$$'
app.config['MYSQL_DB'] = 'shevolve'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('semi(2).html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Data inserted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
