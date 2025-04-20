import streamlit as st
import openai
from pydantic import BaseModel
from factory.prompt_generation import PromptGenerator
from factory.credentials import openapi_key

client = openai.OpenAI(
    api_key = openapi_key
)

class PromptConfig(BaseModel):
    party_name: str
    age: str
    channel : str
    length: int
    concert_hall_area: str

st.title("Concert Hall Marketing Text Generator")
st.subheader("This app generates marketing texts for concert halls.")
st.write("Please fill in the following details:")
party_name = st.text_input("Party Name")
age = st.selectbox("Target Audience Age",
                   ["0-12", "13-19", "20-35", "36-50", "51+"]
                   )
length = st.slider("Length of the text (number of sentences)", 1, 10, 3)
channel = st.selectbox("Channel used for marketing",
                       ["Social Media", "Email", "Website", "Print", "WhatsApp"]
                       )
concert_hall_area = st.text_input("Concert Hall Area")

if st.button("Generate Marketing Text"):
    prompt_config = PromptConfig(
        party_name = party_name,
        age = age,
        channel = channel,
        length = length,
        concert_hall_area = concert_hall_area
    )

    prompt_generator = PromptGenerator(client, prompt_config)
    marketing_text = prompt_generator.get_most_recent_answer()

    st.write("Generated Marketing Text:")
    st.write(marketing_text)