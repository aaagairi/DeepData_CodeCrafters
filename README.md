# 🌍 ESG & Financial Performance Analysis

## 📘 Project Overview

This project explores the intricate relationship between **Financial Performance** and **Environmental, Social, and Governance (ESG) metrics** across various companies, industries, and regions over a decade.

The core objective is to move beyond correlation and provide **actionable insights** and **strategic recommendations** that guide corporate leaders toward better sustainability practices—specifically focusing on how to cut emissions and manage resource usage to simultaneously **boost ESG scores and enhance financial valuation**.

### Key Areas of Analysis:

* **Financial Metrics:** Revenue, MarketCap, GrowthRate, Profit.
* **Sustainability Indicators:** Carbon Emissions, Energy Consumption, Water Usage, Emissions per Revenue.
* **ESG Performance:** ESG\_Overall, ESG\_Environmental, ESG\_Social, ESG\_Governance.


## 📂 Repository Structure

```

├── code.py                           \# Main Python analysis code  
├── company\_esg\_financial\_dataset.csv   \# Dataset used in analysis  
├── plots/                            \# Generated visualizations  
│   └── plots/                        \# Subfolder with saved plots  
├── CodeCrafters\_Round1.pptx          \# Presentation of insights & recommendations  
├── requirements.txt                  \# Project dependencies  
└── README.md                         \# Project documentation

````

### 📄 Dataset Details

Source: Company-level dataset (financial + ESG metrics + sustainability usage). Granularity: Records by company, industry, region, and year. Variables included:

* **📊 Financial:** Revenue, Profit, GrowthRate, MarketCap
* **🌱 ESG:** ESG\_Overall, ESG\_Environmental, ESG\_Social, ESG\_Governance
* **🔋 Sustainability:** CarbonEmissions, EnergyConsumption, WaterUsage, Emissions per Revenue

---

## 🛠️ Project Execution

* ✅ Performed data cleaning, feature engineering (**Profit**, **Emissions per Revenue**).
* ✅ Conducted 11 key EDA questions covering multivariate and time-series analysis.
* ✅ Built stream-structured, stakeholder-friendly plots (line charts, bar charts, scatter plots, heatmaps).
* ✅ Extracted 7 key insights with real-world sustainability implications.
* ✅ Proposed 3 policy recommendations for companies & regions.

---

## 🚀 How to Run

1.  **Clone the repository:**

    git clone [https://github.com/aaagairi/esg-financial-analysis.git](https://github.com/aaagairi/esg-financial-analysis.git)
    cd esg-financial-analysis

2.  **Install dependencies:**

    pip install -r requirements.txt
    

3.  **Run the analysis:**

    python code.py

4.  **View results:**

    * 📈 **Plots:** Saved inside the `plots/` directory.
    * 🖼️ **Presentation:** Open `CodeCrafters_Round1.pptx`.
    * 📄 **Dataset:** Available at `company_esg_financial_dataset.csv`.
