from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rishi@hi1'
app.config['MYSQL_DB'] = 'assignment'

mysql = MySQL(app)
purchase=False
@app.route('/', methods = ["POST", "GET"])
def main_page():
    return render_template("front.html")

@app.route('/search', methods = ["POST", "GET"])
def search():
    purchase=False
    if request.method == "POST":
        print(request.method)
        print(request.form["box"]) 
        value = request.form["box"] 
        field = request.form["search"]
        print(field)
        print("TEST")
        encashed=["Date of Encashment", "Encahsed Bond Number","Name of the Political Party", "Bond Holder Name", "Denominations", "Pay Branch Code", "Pay Teller"]
        purchased= ["Reference No (URN)","Journal Date","Date of Purchase","Date of Expiry","Name of the Purchaser","Prefix","Purchased Bond Number","Purchased Denominations","Issue Branch Code","Issue Teller","Status"]
        if field in purchased:
            for i in purchased:
                if field == i:
                    print("TEST")
                    cursor = mysql.connection.cursor()
                    cursor.execute(f"select * from purchased where `{i}`= %s", (value,))
                    # print(f"select * from encash where `{i}`= %s", (value,))
                    data = cursor.fetchall()
                    purchase=True
                    cursor.close()
                    return render_template("search.html", purchased_data = data) 
        elif field in encashed:
            for i in encashed:
                if field == i:
                    print("TEST")
                    cursor = mysql.connection.cursor()
                    cursor.execute(f"select * from encash where `{i}`= %s", (value,))
                    print(f"select * from encash where `{i}`= %s", (value,))
                    data = cursor.fetchall()
                    cursor.close()
                    return render_template("search.html", encash_data = data)       
        else:
             return render_template("search.html",no_data = "No data found")
                
    return render_template("search.html")
        
    
    
@app.route('/Voter_name', methods = ["POST", "GET"])
def Voter_name():
        if request.method == "POST":
            print("hi")
            value = request.form["box"] 
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT YEAR(`date of purchase`) AS purchase_year, COUNT(*),sum(`Purchased Denominations`) AS total_purchases FROM purchased where `Name of the Purchaser`= %s GROUP BY YEAR(`date of purchase`)",(value,))
            
            data = cursor.fetchall()
            cursor.close()
            return render_template("Voter_name.html", voter_data = data)
        return render_template("Voter_name.html")


@app.route('/party', methods = ["POST", "GET"])
def party():
        if request.method == "POST":
            print("hi")
            value = request.form["box"] 
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT YEAR(`Date of Encashment`) AS encash_year, COUNT(*),sum(`Denominations`) AS total_encash FROM encash where `Name of the Political Party`= %s GROUP BY YEAR(`Date of Encashment`)",(value,))
            
            data = cursor.fetchall()
            cursor.close()
            return render_template("party.html", voter_data = data)
        return render_template("party.html")

@app.route('/four', methods = ["POST", "GET"])
def four():
        if request.method == "POST":
            print("hi")
            value = request.form["boxes"] 
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT `Name of the Political Party` as party, `Name of the Purchaser`, sum(Denominations) as purchase FROM encash JOIN purchased on `Encahsed Bond Number`=`Purchased Bond Number` where `Name of the Political Party`= %s group by(`Name of the Purchaser`)",(value,))
            
            data = cursor.fetchall()
            cursor.close()
            return render_template("four.html", voter_data = data)
        return render_template("four.html")

@app.route('/five', methods = ["POST", "GET"])
def five():
        if request.method == "POST":
            print("hi")
            value = request.form["boxes"] 
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT `Name of the Political Party` as party, `Name of the Purchaser`, sum(Denominations) as purchase FROM encash JOIN purchased on `Encahsed Bond Number`=`Purchased Bond Number`  where `Name of the Purchaser`= %s group by(`Name of the Political Party`)",(value,))
            
            data = cursor.fetchall()
            cursor.close()
            return render_template("five.html", voter_data = data)
        return render_template("five.html")

@app.route('/pie', methods = ["POST", "GET"])
def pie():
        cursor = mysql.connection.cursor()
        cursor.execute("select `Name of the Political Party`, sum(Denominations) from encash group by `Name of the Political Party`")
        data = cursor.fetchall()
        cursor.close()
        return render_template("pie.html", voter_data = data)

@app.route('/extra', methods = ["POST", "GET"])
def extra():
        if request.method == "POST":
            print("hi")
            value = request.form["boxes"] 
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT `Name of the Political Party` as party, `Name of the Purchaser`, sum(Denominations) as purchase FROM encash JOIN purchased on `Encahsed Bond Number`=`Purchased Bond Number`  where `Name of the Purchaser`= %s group by(`Name of the Political Party`)",(value,))
            
            data = cursor.fetchall()
            cursor.close()
            return render_template("extra.html", voter_data = data)
        return render_template("extra.html")


if __name__ == '__main__':
   app.run(host="0.0.0.0", port="8000", debug = True) 
