import streamlit as st
import pandas as pd
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

import streamlit as st
import pickle
import pandas as pd
import numpy as np
import openpyxl
import string
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
import string
from nltk import PorterStemmer
from io import BytesIO
# from Cat_code import dotask
ps =PorterStemmer()
from icici1 import dotask
#from Quadrant import quad
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'})
    worksheet.set_column('A:A', None, format1)
    writer.save()
    processed_data = output.getvalue()
    return processed_data
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)




# importing pickle file for model based approach
# tfidf = pickle.load(open('vectorizer_new.pkl','rb'))
# model_new = pickle.load(open('model_new.pkl','rb'))
st.title('ICICI')
st.header('You can upload free text column with "Remarks" name')


# st.button('Upload excel/csv file')
# uploaded_file = st.file_uploader("Choose a file")
# df1 =pd.DataFrame({})
#
# if uploaded_file is not None:
#     df =pd.read_excel(uploaded_file)
#     df_ = df.astype(str)
#     df1.append(df_)
#     st.write(df_)
# else:
#     pass
#
# st.write(df1)
uploaded_file = st.file_uploader("Choose a file")
df =pd.read_excel(uploaded_file)
df= df.astype(str)
col = ['Journey Name', 'Team Name', 'Form Number', 'NPS Rating', 'Remarks', 'Sub Categories', 'Sentiment']
df_final =pd.DataFrame(columns=col)


# st.write(df)



if st.button('transformed_data'):
    df['transformed_text']=df['Remarks'].apply(transform_text)
    df['transformed_text']=df['transformed_text'].replace('',np.NaN)
    df.dropna(subset =['transformed_text'],how ='any',inplace=True)
    st.write(df)

else:
    pass

if st.button('Categories'):                    #CATEGORIZATION and NPS_cal
    a = dotask(df)
    df_xlsx = to_excel(a)
    st.download_button(
        label="Download data as CSV",
        data=df_xlsx,
        file_name='large_df.csv',
        mime='text/csv',
    )
    # st.write(a)
    # st.write(dotask(df))
    # df_final.append(dotask(df))
    # st.download_button()

#elif st.button('NPS Rating	'):                                     #NPS graph data
    # a = dotask(df)
    # b = quad(a)
    #df_xlsx1 = to_excel(b)
    #st.download_button(
        #label="Download excel sheet for Quadrant graph",
        #data=df_xlsx1,
        #file_name='Quadrant graph.csv',
        #mime='text/csv',
    #)



#
# df_xlsx = to_excel(a)
#
# st.download_button(
#     label="Download data as CSV",
#     data=df_xlsx,
#     file_name='large_df.csv',
#     mime='text/csv',
# )
# if st.button('Data of NPS Quadrant graph'):
#     b =quad(a)
#     st.write(b)
#
# else:
#     pass
# df_xlsx1 = to_excel(b)
#
# st.download_button(
#     label="Download excel sheet for Quadrant graph",
#     data=df_xlsx1,
#     file_name='Quadrant graph.csv',
#     mime='text/csv',
# )




