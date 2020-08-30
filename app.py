from flask import Flask,render_template,request

import pickle

model = pickle.load(open('loan1.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction',methods=['POST'])
def prediction():
    '''    #
    For rendering results on HTML GUI
    '''
    #x_test = [[str(x) for x in request.form.values()]]
    a = request.form['Gender']
    if (a == "Male"):
        a = 1
    if (a == "Female"):
        a = 0
    
    b = request.form['Married']
    if (b == "Yes"):
        b = 1
    if (b == "No"):
        b = 0

    c = request.form['Dependents']
    
        
    d = request.form['Education']
    if (d == "educated"):
        d = 0
    if (d == "uneducated"):
        d = 1
        
    e = request.form['Self_Employed']
    if (e == "yes"):
        e = 1
    if (e == "no"):
        e = 0
    
    f = request.form['ApplicantIncome']
    g = request.form['CoapplicantIncome']
    h = request.form['LoanAmount']
    i = request.form['Loan_Amount_Term']
    
    j = request.form['Credit_History']
    if (j == "yes"):
        j = 1
    if (j == "no"):
        j = 0
        
    k = request.form['Property_Area']
    if (k == "urban"):
        k = 2
    if (k == "semiurban"):
        k = 1
    if (k == "rural"):
        k = 0
    
    total = [[int(a),int(b),int(c),int(d),int(e),float(f),float(g),float(h),int(i),int(j),int(k)]]
    prediction_1 = model.predict(total)
    print(prediction_1)
    output=prediction_1[0]
    if(output==1):
        pred="congratulations Loan Granted"
    else:
        pred="sorry! Loan rejected"
    return render_template('index.html', y=str(pred))

'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    For direct API calls trought request
    
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
    '''

if __name__ == "__main__":
    app.run(debug=True)