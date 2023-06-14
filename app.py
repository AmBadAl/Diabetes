# !pip install pysimplegui
# Imports
import PySimpleGUI as sg
import os.path
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

import sys
import os

os.chdir(sys._MEIPASS)
data_path = 'data\\rf_model.sav'

# Laoding model
rf_model = pickle.load(open(data_path, "rb"))

selected_features = ['HeartDiseaseorAttack', 'PhysActivity', 'Age', 'HvyAlcoholConsump', 
                     'Veggies', 'Sex', 'CholCheck', 'GenHlth', 'HighChol', 'HighBP']

age_ranges = ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49'
              , '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older']
gen_health = ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']
yes_no = ['No', 'Yes']
sex = ['Female', 'Male']

font = ('Helvetica Rounded', 13, '')
sg.set_options(font=font)
sg.theme('Lightgreen2')

layout = [
    [
        sg.Text('Diabetes Check Application', font=('Helvetica Rounded', 30, 'bold'), pad=5
                , justification="center", expand_x='true', text_color='DodgerBlue4'),
    ],
    [
#         sg.Text("Please fill all empty fields, then use the green button to see the result."
#                 , font=('Helvetica Rounded', 15, 'bold underline'), pad=5),
        sg.Text("Please answer all the questions."
                , font=('Helvetica Rounded', 15, 'bold underline'), pad=5),
    ],
    [
        sg.Text("What is you age range?", size=(45, 1), key='-Age Label-'),
        sg.Combo(values=age_ranges, readonly=True, size=(10, 1), enable_events=True, key="-Age-"),
#         sg.Text('', font=('Helvetica Rounded', 12, '')),
    ],
    [
        sg.Text('* All ranges are closed intervals', font=('Helvetica Rounded', 10, ''), pad=(0, 0)),
    ],
    [
        sg.Text("How do you describe your general health?", size=(45, 1), key='-General Health Label-'),
        sg.Combo(values=gen_health, readonly=True, size=(10, 1), enable_events=True, key="-General Health-"),
#         sg.Text('', font=('Helvetica Rounded', 12, '')),
    ],
    [
        sg.Text('', font=('Helvetica Rounded', 10, ''), pad=(0, 0)),
    ],
    [
        sg.Text("Have you had physical activity in past 30 days?", size=(45, 1), key='-Physical Activity Label-'),
        sg.Combo(values=yes_no, readonly=True, size=(10, 1), enable_events=True, key="-Physical Activity-"),
#         sg.Text('* Not including job', font=('Helvetica Rounded', 12, '')),
    ],
    [
        sg.Text('', font=('Helvetica Rounded', 10, ''), pad=(0, 0)),
    ],
    [
        sg.Text("Have you ever had a heart diseaseor attack?", size=(45, 1), key='-Heart Diseaseor Attack Label-'),
        sg.Combo(values=yes_no, readonly=True, size=(10, 1), enable_events=True, key="-Heart Diseaseor Attack-"),
#         sg.Text('* Coronary Heart Disease (CHD) or Myocardial Infarction (MI)', font=('Helvetica Rounded', 12, '')),
    ],
    [
        sg.Text('* Coronary Heart Disease (CHD) or Myocardial Infarction (MI)', font=('Helvetica Rounded', 10, ''), pad=(0, 0)),
    ],
    [
        sg.Text("Do you have high cholesterol?", size=(45, 1), key='-High Chol Label-'),
        sg.Combo(values=yes_no, readonly=True, size=(10, 1), enable_events=True, key="-High Chol-"),
#         sg.Text('', font=('Helvetica Rounded', 12, '')),
    ],
    [
        sg.Text('', font=('Helvetica Rounded', 10, ''), pad=(0, 0)),
    ],
    [
        sg.Text("Have you had a cholesterol check in past 5 years?", size=(45, 1), key='-Chol Check Label-'),
        sg.Combo(values=yes_no, readonly=True, size=(10, 1), enable_events=True, key="-Chol Check-"),
#         sg.Text('', font=('Helvetica Rounded', 12, '')),
    ],
    [
        sg.Text('', font=('Helvetica Rounded', 10, ''), pad=(0, 0)),
    ],
    [
        sg.Text("Do you have heavy alcohol consumption habit?", size=(45, 1), key='-Heavy Alcohol Consumption Label-'),
        sg.Combo(values=yes_no, readonly=True, size=(10, 1), enable_events=True, key="-Heavy Alcohol Consumption-"),
#         sg.Text('* For adult men >=14 drinks and for adult women >=7 drinks per week', font=('Helvetica Rounded', 12, '')),
    ],
    [
        sg.Text('* For adult men >=14 drinks and for adult women >=7 drinks per week', font=('Helvetica Rounded', 10, ''), pad=(0, 0)),
    ],
    [
        sg.Text("Do you consume vegetables 1 or more times per day?", size=(45, 1), key='-Veggies Label-'),
        sg.Combo(values=yes_no, readonly=True, size=(10, 1), enable_events=True, key="-Veggies-"),
#         sg.Text('', font=('Helvetica Rounded', 12, '')),
    ],
    [
        sg.Text('', font=('Helvetica Rounded', 10, ''), pad=(0, 0)),
    ],
    [
        sg.Text("What is your sex?", size=(45, 1), key='-Sex Label-'),
        sg.Combo(values=sex, readonly=True, size=(10, 1), enable_events=True, key="-Sex-"),
#         sg.Text('', font=('Helvetica Rounded', 12, '')),
    ],
    [
        sg.Text('', font=('Helvetica Rounded', 10, ''), pad=(0, 0)),
    ],
    [
        sg.Text("Do you have high blood pressure?", size=(45, 1), key='-High Blood Pressure Label-'),
        sg.Combo(values=yes_no, readonly=True, size=(10, 1), enable_events=True, key="-High Blood Pressure-"),
#         sg.Text('', font=('Helvetica Rounded', 12, '')),
    ],
    [
        sg.Text('', font=('Helvetica Rounded', 10, ''), pad=(0, 0)),
    ],
    [
        sg.Button("Show result", border_width=2, font=('Helvetica Rounded', 12, 'bold'), button_color='green', pad=5),
        sg.Text(key="-Error-", text='', text_color='IndianRed3', font=('Helvetica Rounded', 12, 'bold')),
    ],
    [
        sg.HSeparator(),
    ],
    [
        sg.Text('Prone to Diabetes:', size=(14, 1), font=('Helvetica', 18, 'bold')),
        sg.Text(size=(10, 1), key="-Result-", text='-', font=('Helvetica Rounded', 18, 'bold')),
        sg.Text('Confidence:', size=(10, 1), font=('Helvetica', 15, 'bold')),
        sg.Text(size=(5, 1), key="-Confidence-", text='-', font=('Helvetica Rounded', 15, 'bold')),
    ],
]


window = sg.Window("Diabetes Detector!", layout)
information_labels_keys = [
    "-Heart Diseaseor Attack Label-",
    "-Physical Activity Label-",
    "-Age Label-",
    "-Heavy Alcohol Consumption Label-",
    "-Veggies Label-",
    "-Sex Label-",
    "-Chol Check Label-",
    "-General Health Label-",
    "-High Chol Label-",
    "-High Blood Pressure Label-",
]
information_keys = [
    "-Heart Diseaseor Attack-",
    "-Physical Activity-",
    "-Age-",
    "-Heavy Alcohol Consumption-",
    "-Veggies-",
    "-Sex-",
    "-Chol Check-",
    "-General Health-",
    "-High Chol-",
    "-High Blood Pressure-",
]
empty_error = 'Please fill all the fields above!'
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Show result":
        window['-Result-'].update('-')
        window['-Error-'].update('')
        is_ready = True
        errors = set([])
        for i in range(len(information_keys)):
            window[information_labels_keys[i]].update(text_color='black')
            if values[information_keys[i]] == '':
                is_ready = False
                errors.add(empty_error)
                window[information_labels_keys[i]].update(text_color='IndianRed3')
        if is_ready:
            input_data = []
            for key in information_keys:
                if key == '-Age-':
                    input_data.append(age_ranges.index(values[key]) + 1)
                elif key == '-General Health-':
                    input_data.append(gen_health.index(values[key]) + 1)
                elif key == '-Sex-':
                    input_data.append(sex.index(values[key]))
                else:
                    input_data.append(yes_no.index(values[key]))
            input_df = pd.DataFrame([input_data], columns=selected_features)
            result = int(rf_model.predict(input_df)[0])
            confs = rf_model.predict_proba(input_df)[0]
            print(result)
            print(confs)
            if result == 1:
                window['-Result-'].update('POSITIVE')
                window['-Result-'].update(text_color='red')
                window['-Confidence-'].update(str(int(confs[1] * 100)) + ' %')
                window['-Confidence-'].update(text_color='red')
            else:
                window['-Result-'].update('NEGATIVE')
                window['-Result-'].update(text_color='green')
                window['-Confidence-'].update(str(int(confs[0] * 100)) + ' %')
                window['-Confidence-'].update(text_color='green')
        else:
            error = ''
            for s in errors:
                error += ' ' + s
            window['-Error-'].update(error)
                
window.close()