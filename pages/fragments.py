import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta
import string
import time


def fragments():

    # Wide layout
    st.set_page_config(layout="wide")

    # Add a link back to app.py
    # Add a link to fragments.py
    container = st.container(border=True)
    container.write("""
                    This container has the link to the main app. 
                 """)
    container.page_link("app.py", label="Go to main app page")

    st.write("This is the Fragments page, demonstrating the use of fragments in Streamlit.")


    st.write("## Fragment 1: Displaying a DataFrame")
    @st.cache_data # 👈 This is the new decorator
    def get_data():
        """
        Function to generate random sales data for multiple products.
        """
        product_names = ["Widget " + letter for letter in string.ascii_uppercase]
        average_daily_sales = np.random.normal(1_000, 300, len(product_names))
        products = dict(zip(product_names, average_daily_sales))

        data = pd.DataFrame({})
        sales_dates = np.arange(date(2023, 1, 1), date(2024, 1, 1), timedelta(days=1))
        for product, sales in products.items():
            data[product] = np.random.normal(sales, 300, len(sales_dates)).round(2)
        data.index = sales_dates
        data.index = data.index.date
        return data

    data = get_data()
    data

    # Function to display the daily sales data

    @st.experimental_fragment
    def show_daily_sales(data):
        time.sleep(1)
        selected_date = st.date_input(
            "Pick a day ",
            value=date(2023, 1, 1),
            min_value=date(2023, 1, 1),
            max_value=date(2023, 12, 31),
            key="selected_date",
        )

        if "previous_date" not in st.session_state:
            st.session_state.previous_date = selected_date
        previous_date = st.session_state.previous_date
        st.session_state.previous_date = selected_date
        is_new_month = selected_date.replace(day=1) != previous_date.replace(day=1)
        if is_new_month:
            st.rerun()

        st.header(f"Best sellers, {selected_date:%m/%d/%y}")
        top_ten = data.loc[selected_date].sort_values(ascending=False)[0:10]
        cols = st.columns([1, 4])
        cols[0].dataframe(top_ten)
        cols[1].bar_chart(top_ten)

        st.header(f"Worst sellers, {selected_date:%m/%d/%y}")
        bottom_ten = data.loc[selected_date].sort_values()[0:10]
        cols = st.columns([1, 4])
        cols[0].dataframe(bottom_ten)
        cols[1].bar_chart(bottom_ten)

    
    # Function to display monthly sales data
    # def 
# Render the fragment
fragments()