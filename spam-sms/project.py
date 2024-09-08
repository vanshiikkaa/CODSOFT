import streamlit as st
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    # convert each character in lower case
    text = text.lower()

    # tokenize each word
    text = word_tokenize(text)

    # remove specials characters, stop words and punctuation
    new_text = []
    for word in text:
        if word.isalnum() and word not in stopwords.words('english') and word not in string.punctuation:
            new_text.append(word)

    # remove stemming
    text = new_text[:]
    new_text.clear()
    for word in text:
        new_text.append(ps.stem(word))
    return " ".join(new_text)


vect = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Check'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = vect.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Ham (Not Spam)")