import streamlit as st
import requests
import os

st.set_page_config(page_title="Weather App ☁️", page_icon="🌤️")
st.subheader("Check the current weather in any city around the world")


city = st.text_input("Enter city name")
if city:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        st.error("API key not set.")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            try:
                temp_c = data['main']['temp']
                country = data['sys']['country']
                humidity = data['main']['humidity']
                icon_code = data['weather'][0]['icon']
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
                temp_f = (temp_c * 9/5) + 32

                st.image(icon_url)
                st.subheader(f"{city.title()}, {country}")
                st.metric("Temperature", f"{temp_f:.1f} °F")

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Temperature (°F)", f"{temp_f:.1f}°")

                with col2:
                    st.metric("Humidity", f"{humidity}%")


            except KeyError:
                st.error("Weather data is incomplete or malformed.")

        else:
            st.error("City not found or API error.")