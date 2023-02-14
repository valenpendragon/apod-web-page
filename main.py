import streamlit as st
import functions

response = functions.get_apod_data()
img_info = response["explanation"]
img_url = response["url"]
if "copyright" in response.keys():
    copyright_info = response["copyright"]
else:
    copyright_info = None

