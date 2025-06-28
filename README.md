# 📊 Auto Dashboard Generator with AI Insights

A simple and powerful Streamlit app that allows users to upload CSV or Excel files and automatically generates dashboards with bar, pie, and line charts. Includes mock AI-generated business insights for demo purposes.

---

## 🔗 Live App

👉 [Click to Launch the App](https://auto-dashboard-ai-2insfhkvycvpk5ebk5tboy.streamlit.app/)

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- OpenPyXL (for Excel support)
- Python-Dotenv (for environment variable loading)

---

## ⚙️ Features

- 📂 Upload CSV or Excel file
- 📄 Data preview (first 5 rows)
- 📊 Auto Bar Chart by category and value
- 🥧 Auto Pie Chart for proportions
- 📈 Line Chart for Date-based trends
- 🤖 Mock AI Insights section (simulated GPT summary)

---

## 📦 How to Run Locally

```bash
git clone https://github.com/ValliAkhila/auto-dashboard-ai.git
cd auto-dashboard-ai

# Optional: create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install required libraries
pip install -r requirements.txt

# Run the app
streamlit run app.py

