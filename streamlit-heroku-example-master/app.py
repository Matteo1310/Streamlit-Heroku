import streamlit as st



#from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
#import torch 

# Sentiment analysis pipeline

import requests

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": "Bearer api_vdALMftqIDxYValjDAeTLCIUUgYHZiEuBn"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()



form = st.form(key='my_form')
text = form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')






# Named entity recognition pipeline, passing in a specific model and tokenizer
st.title('Hello World!')



if submit_button:
    output = query({"inputs": text})
    st.subheader('Data')
    st.write({"emotion": output})


















# Question answering pipeline, specifying the checkpoint identifier
#model = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english', tokenizer='distilbert-base-uncased-finetuned-sst-2-english')

# Named entity recognition pipeline, passing in a specific model and tokenizer
#st.title('Hello World!')


#form = st.form(key='my_form')
#text = form.text_input(label='Enter some text')
#submit_button = form.form_submit_button(label='Submit')

#if submit_button:
 #   st.subheader('Data')
  #  outputs = model(text)
   # st.write({"emotion": outputs})
