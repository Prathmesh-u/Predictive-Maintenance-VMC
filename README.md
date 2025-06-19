# 🛠️ Predictive Maintenance for VMC Machines (Industry 4.0 Application)

This is a real-world, data-driven application I built after working with actual shop-floor data from a VMC (Vertical Machining Center) and bending machine in an Industry 4.0-enabled manufacturing setup.

The goal was to:
- Analyze machine behavior*
- **Detect early signs of tool failure
- **Improve part quality**
- **Minimize downtime**

> This project is part of my long-term technical journey – Blueprint 2025 – to build impactful, real-use AI products from scratch.

---

## 🔍 Project Overview

✅ This project takes in key machine parameters like:
- Spindle speed
- Feed rate
- Tool wear
- Vibration level
- Spindle temperature
- Power consumption

Using **threshold-based logic and parameter relationships**, it predicts:

- **Part Status** (OK / Faulty)
- **Machine Status** (Running / Warning / Fail)
- **Likely Defect Type** (Wear, Misalignment, Heat Stress, etc.)

It also logs every evaluation for traceability, and includes a batch mode for uploading multiple records at once.

---

## 🚀 Live Demo

👉 [Click here to try the deployed app](https://your-username.streamlit.app)  
*(Replace this with your actual Streamlit URL)*

---

## 🧠 How It Works (Rule-based ML-like Logic)

Instead of relying on traditional ML models trained on synthetic data (which was inconsistent), I built a **smart rule-based engine** using actual domain knowledge and industry insights.

### Logic Behind the Predictions:
Each input parameter is evaluated against a well-defined operational range:
- If **any one parameter exceeds its threshold**, it triggers a warning or part failure.
- Certain combinations of high vibration, temperature, and tool wear lead to **specific defect types**.

The app dynamically shows:
- **Prediction status**
- **Confidence levels**
- **Triggering parameters**
- **Likely defect causes**

This makes the system explainable and ready for industrial use where decisions must be backed by logic.

---

## 🧩 Features

- 📊 **Manual Mode** with sliders for real-time testing
- 📂 **Batch Mode** via CSV file upload
- 🧾 **Evaluation Log** stored locally for future audit
- 🎛️ **Professional UI** with metrics and defect diagnosis
- 🧠 **Explainable outputs** (no black-box ML here)
- ⚙️ Built in **Python + Streamlit**, deployable on any platform

---

## 📁 Tech Stack

- Python 3.11+
- Streamlit
- Pandas
- Joblib
- VS Code for development
- GitHub + Streamlit Cloud for deployment

---

## 🏭 Real-World Application

This project is based on real industrial data from a plant I visited. I personally collected, cleaned, and analyzed over 3,000 entries from VMC and bending machine logs.

It was also used to:
- Design insightful Power BI dashboards
- Understand root causes behind part rejections
- Guide predictive maintenance practices

---

## 📈 Sample Screenshots

*(Add these manually in GitHub if needed)*

---

## 📚 How to Run Locally

```bash
git clone https://github.com/Prathmesh-u/Predictive-Maintenance-VMC.git
cd Predictive-Maintenance-VMC
pip install -r requirements.txt
streamlit run app.py
