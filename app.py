import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
#from openai import OpenAI  # ✅ new import

# 🌐 Load API key from .env
load_dotenv()


#client = OpenAI(
   # api_key=os.getenv("OPENAI_API_KEY"),
    #project=os.getenv("OPENAI_PROJECT_ID")
#)


st.set_page_config(page_title="Auto Dashboard Generator", layout="wide")
st.title("📊 Auto Dashboard Generator with AI Insights")
st.write("Welcome! Upload a CSV or Excel file to generate insights.")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("✅ File uploaded successfully!")
        st.subheader("📄 Data Preview")
        st.dataframe(df.head())

        st.subheader("📊 Visualizations")

        columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
        numerics = df.select_dtypes(include=['number']).columns.tolist()

        if columns and numerics:
            selected_cat = st.selectbox("Select a Category (X-axis)", columns)
            selected_num = st.selectbox("Select a Numeric Column (Y-axis)", numerics)

            # Bar chart
            st.markdown("### 📉 Bar Chart")
            bar_data = df.groupby(selected_cat)[selected_num].sum().sort_values(ascending=False)
            st.bar_chart(bar_data)

            # Pie chart
            st.markdown("### 🥧 Pie Chart")
            fig1, ax1 = plt.subplots()
            ax1.pie(bar_data, labels=bar_data.index, autopct='%1.1f%%')
            st.pyplot(fig1)

            # Line chart (if you have a 'Date' column)
            if 'Date' in df.columns:
                try:
                    df['Date'] = pd.to_datetime(df['Date'])
                    time_data = df.groupby('Date')[selected_num].sum()
                    st.markdown("### 📈 Line Chart (Over Time)")
                    st.line_chart(time_data)
                except:
                    st.warning("⚠️ Couldn't parse 'Date' column for line chart.")

        # ✅ AI-Generated Insights (INSIDE try block)
        st.subheader("🤖 AI-Generated Insights")

        if st.button("Generate Insights with AI"):
            with st.spinner("Generating smart summary..."):
                data_text = df.head(50).to_string(index=False)

                prompt = f"""
                You are a data analyst. Based on the following sales data, write a short summary of business insights (sales trends, top-selling products, etc.) in simple language:\n\n{data_text}
                """

                #try:
                 #   response = client.chat.completions.create(
                 #       model="gpt-3.5-turbo",
                  #      messages=[{"role": "user", "content": prompt}],
                   #     max_tokens=300,
                    #    temperature=0.7
                    #)

            insight = ("📊 This is a demo AI summary:\n\n"
                    "- Mouse had the highest sales quantity.\n"
                    "- Sales peaked in the first week of January.\n"
                    "- Laptop generated the most revenue with fewer units sold.\n")
            st.success("✅ Insight generated!")
            st.markdown(insight)

                #except Exception as e:
                 #   st.error(f"❌ Error generating insight: {e}")

    except Exception as e:
        st.error(f"⚠️ Error loading file: {e}")
