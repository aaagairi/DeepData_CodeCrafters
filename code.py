# =============================
# IMPORT LIBRARIES
# =============================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =============================
# LOAD DATA
# =============================
df = pd.read_csv('company_esg_financial_dataset.csv')

# =============================
# FEATURE ENGINEERING
# =============================
df['Profit'] = df['Revenue'] * df['ProfitMargin'] / 100.0
df['Carbon_per_Revenue'] = df['CarbonEmissions'] / (df['Revenue'] + 1e-6)
df['Emissions_per_Revenue'] = df['CarbonEmissions'] / df['Revenue']

# Create output folder for plots
output_dir = 'plots'
os.makedirs(output_dir, exist_ok=True)

# =============================
# 1. Regional Financials
# =============================
region_financials = df.groupby('Region').agg(
    avg_revenue=('Revenue','mean'),
    avg_profit=('Profit','mean'),
    avg_profit_margin=('ProfitMargin','mean'),
    avg_marketcap=('MarketCap','mean')
).reset_index()

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
axes = axes.flatten()
metrics = ['avg_revenue', 'avg_profit', 'avg_profit_margin', 'avg_marketcap']
titles = [
    'Average Revenue by Region',
    'Average Profit by Region',
    'Average Profit Margin by Region',
    'Average Market Cap by Region'
]

for ax, metric, title in zip(axes, metrics, titles):
    sns.barplot(data=region_financials, x='Region', y=metric, palette='Set2', ax=ax)
    ax.set_title(title, fontsize=14)
    ax.set_ylabel(metric.replace('_',' ').title())
    ax.set_xlabel('Region')
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'regional_financials.png'))
plt.close()

# =============================
# 2. Regional ESG
# =============================
esg_cols = ['ESG_Overall', 'ESG_Environmental', 'ESG_Social', 'ESG_Governance']
region_esg = df.groupby('Region')[esg_cols].mean().reset_index()

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
axes = axes.flatten()

for ax, col in zip(axes, esg_cols):
    sns.barplot(data=region_esg, x='Region', y=col, palette='Set3', ax=ax)
    ax.set_title(f'Average {col} by Region', fontsize=14)
    ax.set_ylabel('Average Score')
    ax.set_xlabel('Region')
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.suptitle('Regional ESG Performance', fontsize=18, y=1.02)
plt.savefig(os.path.join(output_dir, 'regional_esg.png'))
plt.close()

# =============================
# 3. Company Metrics over Time by Industry
# =============================
metrics = ['Revenue', 'MarketCap', 'GrowthRate', 'Profit']
fig, axes = plt.subplots(2, 2, figsize=(16, 10), sharex=True)

for ax, metric in zip(axes.flatten(), metrics):
    sns.lineplot(data=df, x='Year', y=metric, hue='Industry', marker="o", ax=ax)
    ax.set_title(f'{metric} Over Time by Industry', fontsize=14)
    ax.set_ylabel(metric)
    ax.set_xlabel("Year")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(title="Industry", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'company_metrics_over_time.png'))
plt.close()

# =============================
# 4. ESG Scores Across Industries
# =============================
df_melt = df.melt(
    id_vars=['Industry'],
    value_vars=['ESG_Overall', 'ESG_Environmental', 'ESG_Social', 'ESG_Governance'],
    var_name='ESG_Component',
    value_name='Score'
)

industry_order = df.groupby('Industry')['ESG_Overall'].mean().sort_values().index
palette_dict = {
    'ESG_Overall': 'darkgreen',
    'ESG_Environmental': 'lightgreen',
    'ESG_Social': 'mediumseagreen',
    'ESG_Governance': 'yellowgreen'
}

plt.figure(figsize=(14, 6))
sns.barplot(
    data=df_melt,
    x='Industry',
    y='Score',
    hue='ESG_Component',
    hue_order=['ESG_Overall','ESG_Environmental','ESG_Social','ESG_Governance'],
    ci=None,
    order=industry_order,
    palette=palette_dict
)
plt.title('ESG Scores Across Industries (Overall & Subcomponents)')
plt.ylabel('Average ESG Score')
plt.xticks(rotation=45)
plt.legend(title='ESG Component')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'esg_scores_by_industry.png'))
plt.close()

# =============================
# 5. Yearly Trends: Growth, Emissions, ESG
# =============================
yearly = df.groupby('Year').agg(
    avg_growth=('GrowthRate','mean'),
    avg_emissions_per_rev=('Carbon_per_Revenue','mean'),
    avg_ESG_env=('ESG_Environmental','mean')
).reset_index()

yearly.plot(
    x='Year',
    y=['avg_growth','avg_emissions_per_rev','avg_ESG_env'],
    subplots=True, figsize=(6, 5), marker='o'
)
plt.suptitle('Yearly Trends: Growth, Emissions Intensity, ESG_env')
plt.savefig(os.path.join(output_dir, 'yearly_trends.png'))
plt.close()

# =============================
# 6. ESG vs Resource Usage Over Years
# =============================
yearly_res = df.groupby('Year').agg(
    avg_ESG_env=('ESG_Environmental','mean'),
    avg_CarbonEmissions=('CarbonEmissions','mean'),
    avg_WaterUsage=('WaterUsage','mean'),
    avg_EnergyConsumption=('EnergyConsumption','mean')
).reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_res, x='Year', y='avg_ESG_env', color='darkgreen', label='ESG_Environmental')
sns.lineplot(data=yearly_res, x='Year', y='avg_CarbonEmissions', color='red', label='Carbon Emissions')
sns.lineplot(data=yearly_res, x='Year', y='avg_WaterUsage', color='blue', label='Water Usage')
sns.lineplot(data=yearly_res, x='Year', y='avg_EnergyConsumption', color='orange', label='Energy Consumption')

plt.title('ESG Environmental vs Resource Usage Over Years')
plt.ylabel('Average Value')
plt.xlabel('Year')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'esg_vs_resources.png'))
plt.close()

# =============================
# 7. Correlation Heatmaps
# =============================
financial_metrics = ['Revenue', 'Profit', 'ProfitMargin', 'MarketCap']
esg_scores = ['ESG_Overall', 'ESG_Environmental', 'ESG_Social', 'ESG_Governance']
resource_metrics = ['CarbonEmissions', 'WaterUsage', 'EnergyConsumption']

financial_vs_esg_corr = df[financial_metrics + esg_scores].corr().loc[financial_metrics, esg_scores]
corr_res_esg = df[resource_metrics + esg_scores].corr().loc[resource_metrics, esg_scores]

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

sns.heatmap(financial_vs_esg_corr, annot=True, fmt=".2f", cmap="Greens", ax=axes[0])
axes[0].set_title('Financial Metrics vs ESG Scores')

sns.heatmap(corr_res_esg, annot=True, fmt=".2f", cmap="YlGnBu", ax=axes[1])
axes[1].set_title("Resource Metrics vs ESG Scores")

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'correlation_heatmaps.png'))
plt.close()

# =============================
# 8. ESG vs Market Cap
# =============================
df_sorted = df.sort_values('MarketCap')
df_sorted['MarketCap_bin'] = pd.qcut(df_sorted['MarketCap'], q=20)

avg_df = df_sorted.groupby('MarketCap_bin').agg({
    'MarketCap':'mean',
    'ESG_Overall':'mean',
    'ESG_Environmental':'mean',
    'ESG_Social':'mean',
    'ESG_Governance':'mean'
}).reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=avg_df, x='MarketCap', y='ESG_Overall', label='ESG_Overall')
sns.lineplot(data=avg_df, x='MarketCap', y='ESG_Environmental', label='ESG_Environmental')
sns.lineplot(data=avg_df, x='MarketCap', y='ESG_Social', label='ESG_Social')
sns.lineplot(data=avg_df, x='MarketCap', y='ESG_Governance', label='ESG_Governance')

plt.xscale('log')
plt.xlabel('Market Capitalization (log scale)')
plt.ylabel('Average ESG Score')
plt.title('Average ESG Scores vs MarketCap')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='ESG Component')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'esg_vs_marketcap.png'))
plt.close()

# =============================
# 9. Scatter + Regression: ESG vs MarketCap
# =============================
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='MarketCap', y='ESG_Overall', alpha=0.5, color='grey', s=50)
sns.regplot(data=df, x='MarketCap', y='ESG_Overall', scatter=False, color='green', line_kws={'linewidth':2})

plt.xscale('log')
plt.xlabel('Market Capitalization (log scale)')
plt.ylabel('ESG Overall Score')
plt.title('Are Larger Companies Investing More in ESG?')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'scatter_regression_marketcap_esg.png'))
plt.close()

# =============================
# 10. Regional Comparisons
# =============================
# Emissions per revenue by region
region_emissions = df.groupby('Region').agg(
    avg_emissions_per_rev=('Emissions_per_Revenue','mean')
).sort_values('avg_emissions_per_rev', ascending=False).reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(data=region_emissions, x='Region', y='avg_emissions_per_rev', palette='Reds_r')
plt.xticks(rotation=45)
plt.ylabel('Average Emissions per Revenue')
plt.title('Regions by Emissions Intensity per Revenue')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'region_emissions.png'))
plt.close()

# ESG environmental trend by region
region_esg_trend = df.groupby(['Region','Year']).agg(
    avg_ESG_env=('ESG_Environmental','mean')
).reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=region_esg_trend, x='Year', y='avg_ESG_env', hue='Region', marker='o')
plt.title('ESG Environmental Improvement Over Years by Region')
plt.ylabel('Average ESG Environmental Score')
plt.xlabel('Year')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Region')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'region_esg_trend.png'))
plt.close()

print(f"All plots saved in folder: {output_dir}")
