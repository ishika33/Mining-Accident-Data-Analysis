# Mining Accident Data Analysis using Python

## 📌 Project Overview
This project analyses real-world mining accident data from the MSHA dataset to identify accident patterns, injury severity trends, and underground risk zones.

The objective was to perform data cleaning, exploratory data analysis (EDA), and extract meaningful safety insights using Python.

---

## 📊 Dataset
- Source: MSHA (Mine Safety and Health Administration)
- Format: Pipe-separated raw text dataset
- Records: ~270,000+ accident entries
- Key fields used:
  - ACCIDENT_TYPE
  - DEGREE_INJURY
  - UG_LOCATION
  - DAYS_LOST
  - ACCIDENT_DT

---

## 🛠 Tools & Technologies
- Python
- Pandas
- Matplotlib
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)

---

## 🔎 Key Analysis Performed
- Cleaned raw pipe-separated industrial dataset
- Converted accident date to datetime format
- Extracted year-wise trends
- Identified top accident categories
- Analysed underground accident locations
- Visualized injury severity distribution

---

## 📈 Key Insights
- Majority of accidents occur in active underground production zones.
- Few accident types contribute to most incidents (Pareto pattern).
- Long-term trend indicates gradual improvement in safety performance.
- Minor injuries are more common than fatal injuries.

---

## 📂 Project Structure
## 📂 Project Structure

Mining_Accident_Data_Analysis  
│  
├── mining_accident_data_analysis.py  # Main analysis script  
├── cleaned_msha_mining_data.csv      # Processed dataset  
├── README.md                         # Project documentation  
├── graphs/                           # Output visualizations  
│   ├── accident_types.png  
│   ├── ug_location.png  
│   ├── year_trend.png  
