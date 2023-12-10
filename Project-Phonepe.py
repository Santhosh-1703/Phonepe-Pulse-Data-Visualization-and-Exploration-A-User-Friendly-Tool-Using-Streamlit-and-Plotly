import pandas as pd
import mysql.connector as sql
import pymysql 
import sqlalchemy
from sqlalchemy import create_engine
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
from sqlalchemy import text

#******* Establishing connection with MySQL workbench *********
# CONNECTING WITH MYSQL DATABASE
 
user="root"
password="1234"
host="127.0.0.1"
database= "phonepe_project"
port = "3306"

engine = create_engine("mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database))
con = engine.connect()

st.title("***Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly***")
st.subheader("  Hello Connections!:raised_hand_with_fingers_splayed: Welcome to My Project Presentation :pray: ")
st.info("**(Note)**:-This data between **2018** to **2022** in **INDIA**")