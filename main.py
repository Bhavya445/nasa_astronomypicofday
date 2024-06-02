
import requests
import streamlit as st


api_key= "1uWjwAzKbalVmld597hI9n117SCQCVcW5fE6tSVF"
url= f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
content = request.json()
#print(content)
txt = content["explanation"]

st.title(content["title"])
st.write(content["date"])
media = content["url"]
if content["media_type"]=="image":
    image_filepath ="img.png"
    ir = requests.get(media)
    with open(image_filepath, "wb") as file:
        file.write(ir.content)
    st.image(image_filepath)
elif content["media_type"]=="video":
    st.video(media)
st.write(txt)