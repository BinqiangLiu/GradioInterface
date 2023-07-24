#OpenAI对于VPN的要求很高！坚果Nuts不行，Windscribe才可以！
import gradio as gr
import openai
from gtts import gTTS
from io import BytesIO

from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#openai.api_key = ""

#   Global variable to hold the chat history, initialise with system role
conversation = [
        {"role": "system", "content": "You are an intelligent professor."}
        ]

#   transcribe function to record the audio input

def transcribe(audio):
    print(audio)

#   Whisper API

    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    print(transcript)

#   ChatGPT API

#   append user's inut to conversation
    conversation.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation
    )
    
    print(response)

#   system_message is the response from ChatGPT API
    system_message = response["choices"][0]["message"]["content"]

#   append ChatGPT response (assistant role) back to conversation
    conversation.append({"role": "assistant", "content": system_message})

    tts = gTTS(system_message)
#    try:
#        my_file_name = text[0:20]
#    except:
#        my_file_name = "audio"
    tts.save(f"micaudio.mp3")
#    audio_file = open(f"micaudio.mp3", "rb")
#    audio_bytes = audio_file.read()
#    return audio_bytes
    return "micaudio.mp3"

#   Text to speech
#    engine = pyttsx3.init()
#    engine.setProperty("rate", 150)
#    engine.setProperty("voice", "english-us")
#    engine.save_to_file(system_message, "response.mp3")
#    engine.runAndWait()
#    return "response.mp3"

#   Gradio output

bot = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath"), outputs="audio")
#这里，inputs中的filepath，表示的是，通过麦克风录音后直接存储在运行程序的设备本地
#例如：C:\Users\lenovo\AppData\Local\Temp\gradio\eec7427c8cf8fe8058c18255820b4e9e0260ca5d\audio-0-100.wav
#这个被存储的语音文件随后可以作为其他函数或功能模块的输入，例如Whisper用于将该语音转文本时候的audio_file = open(audio, "rb")，其中的audio就是这个audio-0-100.wav
#audio_file则是一个（临时）变量，被用作transcribe的参数：transcript = openai.Audio.transcribe("whisper-1", audio_file)

bot.launch(share=False)

iface.share()
