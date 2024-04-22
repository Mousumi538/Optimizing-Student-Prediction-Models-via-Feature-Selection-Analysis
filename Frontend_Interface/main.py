import pickle
import joblib
import pandas as pd
import numpy as np

from pyscript import document

import warnings
warnings.filterwarnings('ignore')

def predict_result(event):
    # creating variables and entering all the column headers for csv one by one
    name = document.querySelector("#name").value
    if(name == ""):
        name = "Student"
    classificationType = int(document.querySelector("#classificationType").value)
    
    # Link all variables from form to python
    school = int(document.querySelector("#school").value)
    sex = int(document.querySelector("#sex").value)
    age = int(document.querySelector("#age").value)
    address = int(document.querySelector("#address").value)
    famsize = int(document.querySelector("#famsize").value)
    Pstatus = int(document.querySelector("#Pstatus").value)
    Medu = int(document.querySelector("#Medu").value)
    Fedu = int(document.querySelector("#Fedu").value)
    Mjob = int(document.querySelector("#Mjob").value)
    Fjob = int(document.querySelector("#Fjob").value)
    reason = int(document.querySelector("#reason").value)
    guardian = int(document.querySelector("#guardian").value)
    traveltime = int(document.querySelector("#traveltime").value)
    studytime = int(document.querySelector("#studytime").value)
    failures = int(document.querySelector("#failures").value)
    schoolsup = int(document.querySelector("#schoolsup").value)
    famsup = int(document.querySelector("#famsup").value)
    paid = int(document.querySelector("#paid").value)
    activities = int(document.querySelector("#activities").value)
    nursery = int(document.querySelector("#nursery").value)
    higher = int(document.querySelector("#higher").value)
    internet = int(document.querySelector("#internet").value)
    romantic = int(document.querySelector("#romantic").value)
    famrel = int(document.querySelector("#famrel").value)
    freetime = int(document.querySelector("#freetime").value)
    goout = int(document.querySelector("#goout").value)
    Dalc = int(document.querySelector("#Dalc").value)
    Walc = int(document.querySelector("#Walc").value)
    health = int(document.querySelector("#health").value)
    absences = int(document.querySelector("#absences").value)
    G1 = int(document.querySelector("#G1").value)
    G2 = int(document.querySelector("#G2").value)
    
    # Load the trained model from the pickle file
    if(classificationType == 0):
        model1 = joblib.load('Binary_Maths_adaboost_1.pkl')
    elif(classificationType == 1):
        model1 = joblib.load('5class_mat_rfr1.pkl')
    elif(classificationType == 2):
        model1 = joblib.load('pred_mat_rfr1.pkl')

    arr = np.array([[G2 ,G1,  absences, failures,  goout,  age,  health,  Fedu,  Fjob,  Walc,  freetime,  Mjob,  reason,  Medu,  famrel]])
    predict1 = model1.predict(arr)

    if(classificationType == 0):
        if(predict1 == 1):
            result = name + " has Passed"
        else:
            result = name + " has Failed"
    elif(classificationType == 1):
        if (predict1 > 15 and predict1 <= 20):
            result = name + " has grade A"
        elif(predict1 > 10 and predict1 <= 15):
            result = name + " has grade B"
        elif(predict1 > 5 and predict1 <= 10):
            result = name + " has grade C"
        elif(predict1 > 0 and predict1 <= 5):
            result = name + " has grade D"
        else:
            result = name + " has failed with grade F"
    elif(classificationType == 2):
        final = (predict1 / 20) * 100
        result = final

    outputvariable = result
    predi_div = document.querySelector("#predi")
    output_div = document.querySelector("#output")
    output_div.innerText = outputvariable
    predi_div.style = "visibility:visible"