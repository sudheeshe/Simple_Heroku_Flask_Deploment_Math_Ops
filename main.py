from flask import Flask, render_template, request
from Operations import mathOps

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home_page.html')

@app.route('/submit',methods=['POST'])
def result():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    oper = request.form.get('maths_operation')

    obj = mathOps()
    output = ""
    if oper == 'Addition':
        output = str(obj.addition(num1,num2))
    elif oper == 'Subtraction':
        output = str(obj.subtraction(num1,num2))
    elif oper == 'Multiplication':
        output = str(obj.multiplication(num1,num2))
    elif oper == 'Division':
        output = str(obj.division(num1,num2))
    elif oper == 'Floor_Division':
        output = str(obj.floor_division(num1,num2))

    return render_template('result.html',result=output)





if __name__ == "__main__":
    app.run(debug=True)