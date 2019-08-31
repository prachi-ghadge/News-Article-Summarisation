from flask import Flask, render_template, request , redirect


app = Flask(__name__)

@app.route("/")
def index():
        return render_template("indexx.html")  

@app.route('/decann.html')
def decann():
    return render_template('decann.html')

                    
if __name__ == '__main__':
       app.run(debug=False)