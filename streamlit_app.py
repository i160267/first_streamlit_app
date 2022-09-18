import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('Egg Sandwich')
streamlit.text('Cheese Omlette')


streamlit.header('Breakfast Menu New')

streamlit.text('🍞 Pancakes')
streamlit.text('🥑 Cheese Omlette, toasts')

streamlit.header('🍞 Build your own Fruit Smoothies 🥑')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
