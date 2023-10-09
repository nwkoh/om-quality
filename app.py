# import necessary libraries
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Define the Streamlit app
def main():
    st.title("Process Yield Impact on Manufacturing Throughput")

    # Input parameters
    st.sidebar.header("Input Parameters")
    yield_rate = st.sidebar.slider("Process Yield (%)", 0.0, 100.0, 90.0, 0.1)
    throughput_per_hour = st.sidebar.number_input("Manufacturing Throughput (units/hour)", 1)

    # Calculate the impact on manufacturing throughput
    throughput_impact = (yield_rate / 100) * throughput_per_hour

    # Display the results
    st.subheader("Impact on Manufacturing Throughput")
    st.write(f"With a process yield of {yield_rate}%, the manufacturing throughput would be:")
    st.write(f"{throughput_impact} units/hour")

    # Create a chart to visualize the impact using Plotly
    yield_range = np.arange(0, 101, 5)
    throughput_impacts = [(y / 100) * throughput_per_hour for y in yield_range]
    df = pd.DataFrame({'Yield (%)': yield_range, 'Throughput (units/hour)': throughput_impacts})

    fig = px.line(df, x='Yield (%)', y='Throughput (units/hour)', labels={'Yield (%)': 'Yield (%)', 'Throughput (units/hour)': 'Throughput (units/hour)'})

    st.subheader("Impact of Yield on Throughput")
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()

