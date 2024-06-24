import streamlit as st
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
url = f'https://pokeapi.co/api/v2/pokemon/5/'
response = requests.get(url)
pokemon = response.json()
name = pokemon['name']
height = pokemon['height']
weight = pokemon['weight']

url = f'https://pokeapi.co/api/v2/pokemon/6/'
response = requests.get(url)
pokemon2 = response.json()
name2 = pokemon2['name']
height2 = pokemon2['height']
weight2 = pokemon2['weight']

url = f'https://pokeapi.co/api/v2/pokemon/7/'
response = requests.get(url)
pokemon3 = response.json()
name3 = pokemon3['name']
height3 = pokemon3['height']
weight3 = pokemon3['weight']



name = pokemon['name']
st.title(name.capitalize())

col1, col2 = st.columns(2)
with col1:
    sprites = pokemon['sprites']
    picture = sprites.get("front_default")
    st.image(picture, width = 300)
with col2:
    st.write(f"**Height** - {pokemon['height']}")
    st.write(f"**Weight** - {pokemon['weight']}")
    st.write(f"**Base Experience** - {pokemon['base_experience']}")
    abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
    st.write("**Abilities**:")
    for ability in abilities:
        st.write(f"- {ability.capitalize()}")
    

st.subheader('Cries')
cries_url = 'https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/5.ogg'
st.audio(cries_url)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))


ax1.bar([name.capitalize(), name2.capitalize(), name3.capitalize()], [height, height2, height3], color=['grey', 'darkkhaki', 'darksalmon'])
ax1.set_xlabel('Pokémon')
ax1.set_ylabel('Height')



ax2.bar([name.capitalize(), name2.capitalize(), name3.capitalize()], [weight, weight2, weight3], color=['grey', 'darkkhaki', 'darksalmon'])
ax2.set_xlabel('Pokémon')
ax2.set_ylabel('Weight')
ax2.set_title('Weight')

st.pyplot(fig)
st.write('Height and Wight Comparison')











