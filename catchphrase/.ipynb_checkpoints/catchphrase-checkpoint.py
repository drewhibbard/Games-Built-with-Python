import streamlit as st
import pandas as pd
import pygame
import pickle
import time

with open('phrases.pickle','rb') as rf:
    data = pickle.load(rf)
    
df = pd.DataFrame(data,columns=['category','term'])

pygame.mixer.init()

st.write('# Welcome to CatchPhrase!')



category = st.sidebar.selectbox('Choose Category',['Everything'] + list(df.category.unique()))

def get_phrase():
    if category == 'Everything': 
        return df['term'].sample(1).values[0]
    else:
        return df[df.category==category]['term'].sample(1).values[0]

if st.sidebar.button('Start Game'):
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play()
    st.write(get_phrase())

if st.button('Next Phrase'):
    st.write(get_phrase())

