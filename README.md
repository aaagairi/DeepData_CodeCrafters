# 🌍 ESG & Financial Performance Analysis

## 📘 Project Overview

This project explores the intricate relationship between **Financial Performance** and **Environmental, Social, and Governance (ESG) metrics** across various companies, industries, and regions over a decade.

The core objective is to move beyond correlation and provide **actionable insights** and **strategic recommendations** that guide corporate leaders toward better sustainability practices—specifically focusing on how to cut emissions and manage resource usage to simultaneously **boost ESG scores and enhance financial valuation**.

### Key Areas of Analysis:

* **Financial Metrics:** Revenue, MarketCap, GrowthRate, Profit.
* **Sustainability Indicators:** Carbon Emissions, Energy Consumption, Water Usage, Emissions per Revenue.
* **ESG Performance:** ESG\_Overall, ESG\_Environmental, ESG\_Social, ESG\_Governance.

---

## 🎯 Key Insights for Company Leaders (Derived from 12 Plots)

Our analysis confirms that **ESG is a positive driver of financial success**, with the greatest opportunity found in the environmental component.

1.  **ESG Environmental Score Drives Market Value:** The **ESG\_Environmental** score exhibits the most dramatic rise for the largest companies (**MarketCap**), indicating that the market disproportionately rewards superior, verifiable environmental performance.
2.  **Positive Financial Correlation:** A consistent **positive correlation** exists between key financial metrics (**Revenue**, **Profit**, **MarketCap**) and both **ESG\_Overall** and **ESG\_Environmental** scores (up to **0.22**). Sustainability is a business driver.
3.  **Energy Consumption is the Crisis Metric:** **Energy Consumption** is the single most significant and rapidly rising resource metric, dwarfing other usage. Long-term ESG improvement is impossible without aggressive action here.
4.  **Resource Usage vs. ESG:** There is a clear negative correlation (around **-0.15** to **-0.17**) between absolute **Carbon Emissions**, **Water Usage**, and **Energy Consumption** and the **ESG\_Environmental** score. Reduction is the direct path to improvement.
5.  **Industry Gap:** Finance and Technology lead in overall ESG. Low-performing sectors like Transportation and Energy must urgently commit to deep decarbonization to align with market and regulatory expectations.
6.  **Regional Intensity:** Africa and North America have the highest average **Emissions per Revenue** intensity, highlighting an urgent need for energy efficiency improvements in their regional economies.
7.  **Global Progress:** All regions show a consistent, linear improvement in **ESG\_Environmental** scores over the decade, proving that global improvement is achievable.

---

## 📈 Policy Recommendations for a Greener Business World

These proposals are targeted at encouraging capital investment and enforcing strategic accountability.

1.  **The "Green Cap-Ex" Tax Credit Program:** Introduce a capital expenditure tax credit (e.g., 15-25%) specifically for investments in energy-efficient technology and verified **Carbon Emissions** reduction projects. Prioritize higher proportional benefits for mid-sized companies to close the ESG investment gap.
2.  **Mandatory Sector-Specific Resource Reduction Targets (MSRT):** Institute regulated 5-year reduction targets for the most material resource metric (e.g., **Carbon Emissions** for Transportation, **Water Usage** for Manufacturing). This moves low-performing sectors beyond voluntary compliance.
3.  **"ESG Governance Linkage" Disclosure Standard:** Mandate public disclosure detailing how **ESG\_Environmental** performance metrics are explicitly linked to executive and senior management compensation. This ensures sustainability is a core strategic and personal accountability metric for leadership.

---

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
* ✅ Conducted 12 key EDA questions covering multivariate and time-series analysis.
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
````
