from flask import Flask, render_template, request , redirect
import MySQLdb
import pandas as pd
import json
from flask_mysqldb import MySQL

app = Flask(__name__)


@app.route("/")
def index():
        return render_template("index22.html")  


@app.route('/getAllBlogs')
def getAllBlogs():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='capstone2' ,use_unicode=True, charset="utf8")
    cursor = conn.cursor()
    df = pd.read_sql_query("select * from Summary_table where category ='Nation';", conn)
    df=df.loc[:,['Headline','URL','Image','Category','Gen_summary']]
    data_dic=df.to_dict(orient='records')
    print(data_dic)
    return json.dumps(data_dic)


@app.route('/Nation.html')
def Nation():
    return render_template("Nation.html")

@app.route('/getAllNews')
def getAllNews():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='capstone2' ,use_unicode=True, charset="utf8")
    cursor = conn.cursor()
    df = pd.read_sql_query("select * from Summary_table where category ='News';", conn)
    df=df.loc[:,['Headline','URL','Image','Category','Gen_summary']]
    data_dic=df.to_dict(orient='records')
    print(data_dic)
    return json.dumps(data_dic)


@app.route('/News.html')
def News():
    return render_template("News.html")
    
@app.route('/getAllEntertainment')
def getAllEntertainment():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='capstone2' ,use_unicode=True, charset="utf8")
    cursor = conn.cursor()
    df = pd.read_sql_query("select * from Summary_table where category ='Entertainment' ;", conn)
    df=df.loc[:,['Headline','URL','Image','Category','Gen_summary']]
    data_dic=df.to_dict(orient='records')
    print(data_dic)
    return json.dumps(data_dic)


@app.route('/Entertainment.html')
def Entertainment():
    return render_template("Entertainment.html")
    
@app.route('/getAllBusiness')
def getAllBusiness():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='capstone2' ,use_unicode=True, charset="utf8")
    cursor = conn.cursor()
    df = pd.read_sql_query("select * from Summary_table where category ='Business' ;", conn)
    df=df.loc[:,['Headline','URL','Image','Category','Gen_summary']]
    data_dic=df.to_dict(orient='records')
    print(data_dic)
    return json.dumps(data_dic)


@app.route('/Business.html')
def Business():
    return render_template("Business.html")
    
@app.route('/getAllSports')
def getAllSports():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='capstone2' ,use_unicode=True, charset="utf8")
    cursor = conn.cursor()
    df = pd.read_sql_query("select * from Summary_table where category ='Sports' ;", conn)
    df=df.loc[:,['Headline','URL','Image','Category','Gen_summary']]
    data_dic=df.to_dict(orient='records')
    print(data_dic)
    return json.dumps(data_dic)


@app.route('/Sports.html')
def Sports():
    return render_template("Sports.html")

@app.route('/getAllOpinion')
def getAllOpinion():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='capstone2' ,use_unicode=True, charset="utf8")
    cursor = conn.cursor()
    df = pd.read_sql_query("select * from Summary_table where category ='Opinion' ;", conn)
    df=df.loc[:,['Headline','URL','Image','Category','Gen_summary']]
    data_dic=df.to_dict(orient='records')
    print(data_dic)
    return json.dumps(data_dic)


@app.route('/Opinion.html')
def Opinion():
    return render_template("Opinion.html")

@app.route('/getAllWorld')
def getAllWorld():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='capstone2' ,use_unicode=True, charset="utf8")
    cursor = conn.cursor()
    df = pd.read_sql_query("select * from Summary_table where category ='World' ;", conn)
    df=df.loc[:,['Headline','URL','Image','Category','Gen_summary']]
    data_dic=df.to_dict(orient='records')
    print(data_dic)
    return json.dumps(data_dic)


@app.route('/World.html')
def World():
    return render_template("World.html")

@app.route('/getAllTechnology')
def getAllTechnology():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='capstone2' ,use_unicode=True, charset="utf8")
    cursor = conn.cursor()
    df = pd.read_sql_query("select * from Summary_table where category ='Technology' ;", conn)
    df=df.loc[:,['Headline','URL','Image','Category','Gen_summary']]
    data_dic=df.to_dict(orient='records')
    print(data_dic)
    return json.dumps(data_dic)


@app.route('/Technology.html')
def Technology():
    return render_template("Technology.html")

@app.route('/getAllLifestyle')
def getAllLifestyle():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='capstone2' ,use_unicode=True, charset="utf8")
    cursor = conn.cursor()
    df = pd.read_sql_query("select * from Summary_table where category ='Lifestyle' ;", conn)
    df=df.loc[:,['Headline','URL','Image','Category','Gen_summary']]
    data_dic=df.to_dict(orient='records')
    print(data_dic)
    return json.dumps(data_dic)


@app.route('/Lifestyle.html')
def Lifestyle():
    return render_template("Lifestyle.html")

    
 
    
                    
if __name__ == '__main__':
       app.run(debug=False)