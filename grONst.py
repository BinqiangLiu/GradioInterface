import gradio as gr
import streamlit as st
st.write("---")
def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    
demo.launch()   
st.write("---")
st.audio(TrackNo56.mp3)
st.write("---")
st.audio(TrackNo56.mp3)

