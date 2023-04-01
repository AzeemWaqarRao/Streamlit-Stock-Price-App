import pandas as pd 
import streamlit as st 
import yfinance as yf
from datetime import date


def main():
    

    st.write("""
    # Stock Price 
    Choose a stock and duration to see graph
    """)

    options = ["AAPL", "GOOGL", "META", "AMZN","TSLA","JNJ","XOM"]
    symbol = st.selectbox("Select an option", options)
    startdate = str(st.date_input("Select a start date", date.today()))
    endtdate = str(st.date_input("Select an end date", date.today()))

    if symbol:
        tickerData = yf.Ticker(symbol)
        tickerDf = tickerData.history(period='1d', start=startdate,end=endtdate)
        st.write("""
        ### Close Price
        """)
        st.line_chart(tickerDf.Close)
        st.write("""
        ### Volume
        """)
        st.line_chart(tickerDf.Volume)
    st.markdown("Developed By Azeem Waqar")
    st.write("""
                [Click here](https://github.com/AzeemWaqarRao/Streamlit-Stock-Price-App) to visit Github Repository.
                """)



if __name__ == "__main__":
    main()