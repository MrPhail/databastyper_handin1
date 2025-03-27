import json
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st

PWD = st.text_input("Enter password.", type="password")

if PWD:
    st.write("Password entered.")

uri = f"mongodb+srv://carljepsen:{PWD}@school.dw3w8.mongodb.net/?retryWrites=true&w=majority&appName=school"

client = MongoClient(uri, server_api=ServerApi('1'))
    
database = client["handins"]
collection = database["handin1"]

products_to_order = [
    {
        '$match': {
            '$expr': {
                '$gt': [
                    '$ReorderLevel',
                    { '$add': ['$UnitsInStock', '$UnitsOnOrder'] }
                ]
            }
        }
    }
]

results = collection.aggregate(products_to_order)

st.write("Products to order")
for i in results:
    st.write(i)