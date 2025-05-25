import pandas as pd
import streamlit as st








st.html("""
    <style>
        .stMainBlockContainer {
            max-width:350rem;
            max-hight:10rem;
        }
    </style>
    """
)

    
data = {
    'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia'],
    'Country': ['USA', 'USA', 'Canada', 'Germany', 'France', 'Japan', 'China'],
    'City': ['New York', 'Los Angeles', 'Toronto', 'Berlin', 'Paris', 'Tokyo', 'Beijing']
    }

df = pd.DataFrame(data)


#df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
st.write(df)