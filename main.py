import streamlit as st
import pickle
import numpy as np
import pandas as pd

pipe = pickle.load(open("pipepkl", "rb"))
df = pickle.load(open("dfplk", "rb"))

st.title("Laptop_Price_Evaluator")

company = st.selectbox("brand", df["Company"].unique())
type = st.selectbox("Type", df["TypeName"].unique())
RAM = st.selectbox("RAM", [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.number_input("laptop_weight")
touch = st.selectbox("Touchscreen", ["No", "Yes"])
IPS = st.selectbox("IPS", ["No", "Yes"])
screensize = st.number_input("Laptop Screensize")
resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
cpu = st.selectbox('CPU', df["cpu_brand"].unique())
hdd = st.selectbox('HDD', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD', [0, 8, 128, 256, 512, 1024])
gpu = st.selectbox('GPU', df["Gpu"].unique())
os = st.selectbox('OS', df["os"].unique())

if st.button("Predict"):
    x_res = int(resolution.split("x")[0])
    y_res = int(resolution.split("x")[1])
    ppf = (x_res**2) + (y_res**2)**0.5 / screensize
    touch = 1 if touch == "Yes" else 0
    IPS = 1 if IPS == "Yes" else 0

    input_data = np.array([company, type, RAM, gpu, weight, touch, IPS, ppf, cpu, hdd, ssd, os])
    input_data = input_data.reshape(1, 12)
    input_df = pd.DataFrame(input_data, columns=["Company", "TypeName", "RAM", "Gpu", "Weight", "Touchscreen", "IPS", "ppf", "cpu_brand", "HDD", "SSD", "os"])
    st.write("Input Data:")
    st.write(input_df)

    prediction = pipe.predict(input_data)
    st.title(prediction)





