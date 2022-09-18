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

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
