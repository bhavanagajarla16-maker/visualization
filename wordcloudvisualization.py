import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic

# 🎯 App Title
st.title("📊 Data Visualization Dashboard")

# 📤 Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📄 Preview of Data", df.head())

    # 📌 Select Visualization Type
    chart_type = st.selectbox("Choose visualization type", [
        "Line Chart (1D)", 
        "Scatter Plot (1D)", 
        "Bar Chart (2D)", 
        "Pie Chart (2D)", 
        "Mosaic Plot (Multi-Dimensional)"
    ])

    if chart_type == "Line Chart (1D)":
        column = st.selectbox("Select numeric column", df.select_dtypes(include='number').columns)
        st.line_chart(df[column])

    elif chart_type == "Scatter Plot (1D)":
        x = st.selectbox("X-axis", df.select_dtypes(include='number').columns)
        y = st.selectbox("Y-axis", df.select_dtypes(include='number').columns)
        fig, ax = plt.subplots()
        ax.scatter(df[x], df[y])
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        st.pyplot(fig)

    elif chart_type == "Bar Chart (2D)":
        category = st.selectbox("Category column", df.select_dtypes(include='object').columns)
        value = st.selectbox("Value column", df.select_dtypes(include='number').columns)
        bar_data = df.groupby(category)[value].sum().sort_values()
        st.bar_chart(bar_data)

    elif chart_type == "Pie Chart (2D)":
        category = st.selectbox("Category column", df.select_dtypes(include='object').columns)
        value = st.selectbox("Value column", df.select_dtypes(include='number').columns)
        pie_data = df.groupby(category)[value].sum()
        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
        ax.set_title(f"Pie Chart of {value} by {category}")
        st.pyplot(fig)

    elif chart_type == "Mosaic Plot (Multi-Dimensional)":
        cols = st.multiselect("Select 2 or more categorical columns", df.select_dtypes(include='object').columns)
        if len(cols) >= 2:
            fig, _ = mosaic(df, index=cols)
            st.pyplot(fig)
        else:
            st.warning("Please select at least two categorical columns.")
