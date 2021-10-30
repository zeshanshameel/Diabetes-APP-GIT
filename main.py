import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing

st.title("Diabetes Prediction")
df = pd.read_csv('diabetes processed.csv')
x = df[['Glucose','BloodPressure','Age','BMI','Pregnancies','SkinThickness']]
y = df['Outcome']
#Age = st.sidebar.slider("Age",21,100)
Age = 0
Age = st.sidebar.slider("Age")
#st.write(type(Age))
Glucose = st.sidebar.number_input("Glucose")
BloodPreassure = st.sidebar.number_input("BloodPreasure")
BMI = st.sidebar.number_input("BMI")
Pregnancies = st.sidebar.number_input("Pregnancies")
SkinThickness = st.sidebar.number_input("SkinThickness")
st.subheader("Your Sugar level Report")
if(Glucose == 0):
    st.write("enter Your Sugar level for your report")
if (Glucose < 140 and Glucose >0):
    st.write("Your Blood sugar report: Normal")
if(Glucose >=140) :
    st.write("Your Blood sugar report: Higer than the normal Blood sugar level,",
    "for knowing more about blood sugar levels refer https://www.medicalnewstoday.com/articles/249413") 

st.subheader("Your Blood Preasure Report")
if(Age == 0 or BloodPreassure == 0 ):
    st.write("Enter your Age and Blood preasure detail")
if(Age < 50 and BloodPreassure <= 120 and Age >0 and BloodPreassure > 0 ):
    st.write("your Blood Preasure is normal")
if(Age < 50 and BloodPreassure > 120 and Age >0 and BloodPreassure > 0 ):
    st.write("your Blood Preasure is high,", 
    "for knowing more about blood Preasure levels refer https://www.medicalnewstoday.com/articles/249413")
if(Age >50 and BloodPreassure <= 140 and Age >0 and BloodPreassure > 0):
    st.write("your Blood Preasure is normal")
if(Age > 50 and BloodPreassure > 140 and BloodPreassure > 0 and Age >0):
    st.write("your Blood Preasure is high,", 
    "for knowing more about blood Preasure levels refer https://www.medicalnewstoday.com/articles/249413")

st.subheader("Your Weight Group:")
if(BMI == 0):
    st.write("enter your BMI details for you report")
if(BMI <= 18.5 and BMI > 0):
    st.write("Under Weight")
if(BMI <= 24.9 and BMI > 18.5):
    st.write("Normal Weight")
if(BMI >24.9 and BMI <= 29.9):
    st.write("Over Weight")
if(BMI >= 30):
    st.write("Obese")

from sklearn.model_selection import train_test_split
# preprocessing the data and splitting
x = pd.DataFrame(x, index=x.index, columns=x.columns)
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
#fitting the RandomForestClassifier model
rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(x_train, y_train)

def pred (Glucose,BloodPressure,Age,BMI,Pregnancies,SkinThickness):
    a = rfc.predict([[Glucose,BloodPressure,Age,BMI,Pregnancies,SkinThickness]])
    return a
result = ''
fin =''

st.subheader("Diabetes Predictor:")
st.write("Enter All the details and know your diabetes report")
if st.button("Predict"):
    result = pred(Glucose,BloodPreassure,Age,BMI,Pregnancies,SkinThickness)
    if result == [1]:
        fin = "Diabetic"
    if result == [0]:
        fin = "Not Diabetic"
st.success('The Person is {}'.format(fin))





