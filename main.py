import streamlit as st
import functions

response = functions.get_apod_data()
img_info = response["explanation"]
img_url = response["url"]
img_title = response["title"]
if "copyright" in response.keys():
    copyright_info = response["copyright"]
else:
    copyright_info = None

image_get = functions.get_image_data(img_url)

# Begin building web page.
st.set_page_config(layout="wide")

# col1 = st.columns(1)

st.title("NASA's Astronomy Picture of the Day")
st.title(img_title)
if image_get:
    st.image("images/today.jpg")
else:
    st.write("Image could not be retrieved today.")
st.info(img_info)
if copyright_info:
    st.write(f"Image Copyright: {copyright_info}")
