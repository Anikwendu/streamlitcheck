import streamlit as st
import pandas as pd
from PIL import Image
import pickle
import sklearn
my_model = pickle.load(open("C:\\Users\\Amarachi Uzochukwu\\Desktop\\rfc_model.pkl", "rb"))
st.title('CHURN FOR TELECOMMUNICATION')
img = Image.open("C:\\Users\\Amarachi Uzochukwu\\Downloads\\pexels-lucas-pezeta-2352277 (3).jpg")
st.image(img, width=350)
def user_report():
    MONTANT = st.sidebar.slider('MONTANT', 1.0, 700.0, 1.0 )
    FREQUENCE_RECH = st.sidebar.slider('FREQUENCE_RECH', 1.0, 700.0, 1.0)
    REVENUE = st.sidebar.slider('REVENUE', 1.0, 800.0, 5.0)
    ARPU_SEGMENT = st.sidebar.slider('ARPU_SEGMENT', 1.0, 700.0, 1.0)
    FREQUENCE = st.sidebar.slider('FREQUENCE',  1.0, 700.0, 1.0 )
    ON_NET = st.sidebar.slider('ON_NET',  1.0, 700.0, 1.0 )
    ORANGE = st.sidebar.slider('ORANGE',  1.0, 700.0, 1.0 )
    REGULARITY = st.sidebar.slider('REGULARITY',  1.0, 700.0, 1.0 )
    FREQ_TOP_PACK = st.sidebar.slider('FREQ_TOP_PACK',  1.0, 700.0, 1. )

    input_data = {
        'MONTANT': MONTANT,
        'FREQUENCE_RECH': FREQUENCE_RECH,
        'REVENUE': REVENUE,
        'ARPU_SEGMENT': ARPU_SEGMENT,
        'FREQUENCE': FREQUENCE,
        'ON_NET': ON_NET,
        'ORANGE': ORANGE,
        'REGULARITY': REGULARITY,
        'FREQ_TOP_PACK': FREQ_TOP_PACK
    }
    data = pd.DataFrame(input_data, index=[0])
    return data
user_data = user_report()
st.write(user_data)
prediction  = my_model.predict(user_data)
if (prediction==0):
    st.success('high churn rate')
else:
    st.success('low churn rate')



