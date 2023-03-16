import streamlit

streamlit.title('My parents new heathy diner')

streamlit.header('Breakfast menu')
streamlit.text('🥣  Strawberry oat bowl')
streamlit.text('🥗 🥑Green smoothie')
streamlit.text('🐔🍞Chicken pie')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)








