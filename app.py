from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors



app = Flask(__name__)
mysql = MySQL(app)

app.config['SECRET_KEY'] = 'this is secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'




# create
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        _name = request.form['name']
        _age = request.form['age']
        _gender = request.form['gender']
        _address = request.form['address']
        _mobile_number = request.form['mobile_number']
        _email = request.form['email']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute('INSERT INTO crud VALUES (NULL,% s, % s,% s, % s,% s, % s)',(_name,_age,_gender,_address,_mobile_number,_email,))
        mysql.connection.commit()
        cursor.close()

        return redirect('/')

    return render_template("create.html")


# Read
@app.route('/read')
def read():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM crud')
    data = cursor.fetchall()

    return render_template("read.html",data=data)


# Update
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM crud WHERE id = % s', (id,))
    data = cursor.fetchone()


    if request.method == 'POST':
        _name = request.form['name']
        _age = request.form['age']
        _gender = request.form['gender']
        _address = request.form['address']
        _mobile_number = request.form['mobile_number']
        _email = request.form['email']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE crud SET name = %s,age = %s,gender = %s,address = %s,mobile_number = %s,email = %s WHERE id = %s',(_name,_age,_gender,_address,_mobile_number,_email,id))
        mysql.connection.commit()
        return redirect('/read')

    return render_template("update.html",data=data)

# delete
@app.route('/delete/<id>',methods=['GET','POST'])
def delete(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('DELETE FROM crud WHERE id = %s',(id))
    mysql.connection.commit()
    return redirect('/read')


if __name__== "__main__":
    app.run(debug=True)