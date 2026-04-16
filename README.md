# Geopolitical Vulnerabilities in Global Semiconductor Supply Chains

## Project Overview 

This project analyzes the vulnerability of global semiconductor supply chains to geopolitical shocks, focusing specifically on the impact of Chinese export restrictions. Semiconductor supply chains are highly globalized and increasingly exposed to geopolitical tensions. Understanding how supplier concentration and dependence on specific countries affect supply resilience is therefore critical for policymakers and firms.

The project combines trade data analysis, supply chain concentration metrics, shock simulations, and statistical modelling to assess how different countries would be affected by disruptions in Chinese semiconductor exports.

## Research Question

The project addresses the following core question:

How vulnerable are national semiconductor supply chains to geopolitical disruptions? 

Guiding Questions: 

1. How concentrated are supply chains? 
2. Who are the main suppliers?
3. Are countries with more concentrated supplier networks more vulnerable to semiconductor supply disruptions?
4. Does dependence on China increase vulnerability to export restrictions?
5. Can supplier diversification mitigate geopolitical supply shocks?

## Data

The analysis uses international trade data for semiconductor products (HS code 8541) covering the period 1990–2024. For the analysis two different datasets were used the main dataset "df" where, 

Key variables include:

- year:	Year of trade observation
- importer:	Country importing semiconductors
- exporter:	Country exporting semiconductors
- trade_value:	Value of semiconductor trade
- flow	Trade direction (imports or exports)
- supplier_share	Share of imports from each supplier
- share_squared	Squared supplier share used for HHI calculation
- supply_concentration	Herfindahl–Hirschman Index (HHI) measuring supplier concentration
- concentration_risk	Classification of diversification level
- 


For the shock scenario we created a new dataframe that focused on 136 importing countries in 2024, the most recent year with complete data.

Key variables include:

- importer: Country importing semiconductors
- baseline_supply: Total semiconductor imports from all suppliers
- imports_china: Total semiconductor imports from China only
- after_shock_imports: Total semiconductor imports from China if chinese exports fall by 40% 
- new_baseline_supply: New total imports after the shock
- absolute_loss: absolute loss in trade value 
- loss_percent: percentage of supply loss
- absolute_loss_100m
- supply_concentration: Herfindahl–Hirschman Index (HHI) measuring supplier concentration
- vulnerability_type: Classification of vulnerability level based on supply concentration 
- china_share: How much china supplies based on total imports 
- china_loss: how much supply disappears purely because China reduced exports by 40%.
- replacement
- adjusted_loss
- region name

## Methodology
1. Supply Chain Concentration

Supplier concentration is measured using the Herfindahl–Hirschman Index (HHI):

𝐻𝐻𝐼 = ∑𝑠𝑖^2

Where:

𝑠𝑖 = is the share of imports from supplier i.

Interpretation:

Low	HHI Value = Diversified suppliers
Moderate HHI Value =	Moderate concentration
High HHI Value =	Highly concentrated supply chains

This provides a measure of structural supply chain risk.

## Shock Simulation

To evaluate geopolitical vulnerability, the project simulates a 40% reduction in Chinese semiconductor exports.

Initial loss is calculated as:

- ChinaLoss=ChinaShare×0.40

However, countries may partially replace lost supply from alternative suppliers. The model therefore includes a substitution mechanism based on supplier diversification.

Replacement capacity is defined as:

- Replacement=ChinaLoss×(1−HHI)

The final adjusted loss becomes:

- AdjustedLoss=ChinaLoss−Replacement

This allows more diversified countries to recover a greater share of lost supply.

## Statistical Analysis

The project tests the relationship between supply chain structure and vulnerability using Ordinary Least Squares (OLS) regression.

The estimated model is:

AdjustedLoss=β0 +β1 SupplyConcentration +β2 ChinaShare+ϵ

Where:

- Supply Concentration= Structural diversification risk
- China Share = Geopolitical dependence on China
- Adjusted Loss = Predicted supply loss after substitution

## Key Results

Regression results indicate that both supplier concentration and dependence on China significantly increase vulnerability to semiconductor supply disruptions.

Key findings include:

- Countries with higher supply concentration experience larger supply losses
- Countries more dependent on Chinese semiconductor imports are particularly vulnerable
- Diversified supplier networks reduce the impact of geopolitical disruptions

The model explains approximately 95% of the variation in simulated supply losses across countries.

## Visualizations

The project includes several visual analyses:

- Evolution of global semiconductor supply concentration over time
- Country-level diversification trends
- Scatter plots of supply concentration vs vulnerability
- Quadrant analysis identifying resilient and vulnerable supply chains
- Distribution of supply losses across countries

These visualizations illustrate how supply chain structure shapes geopolitical risk exposure.

## Key Insights

The analysis highlights two distinct sources of supply chain risk:

1. Structural Risk

Countries with high supplier concentration face greater disruption risk because they lack alternative sources of supply.

2. Geopolitical Exposure

Countries highly dependent on Chinese semiconductor imports are particularly vulnerable to export restrictions.

Together, these findings suggest that both diversification and geopolitical dependence play crucial roles in determining supply chain resilience.

## Policy Implications

The results suggest several policy considerations:

Governments should encourage supplier diversification to reduce structural supply chain risks.
Reducing excessive dependence on a single geopolitical partner can mitigate disruption risks.
Strategic stockpiling and domestic semiconductor capacity may help improve resilience.
Technologies Used

The project was implemented in Python using the following libraries:

pandas – data manipulation
numpy – numerical calculations
matplotlib / seaborn – data visualization
statsmodels – statistical regression analysis
Project Structure
project/
│
├── data/
│   trade_data.csv
│
├── notebooks/
│   cleaning_and_supply_concentration.ipynb
│
├── analysis/
│   shock_simulation.py
│   regression_model.py
│
├── figures/
│   concentration_trends.png
│   vulnerability_scatter.png
│
└── README.md
Limitations

Several limitations should be acknowledged:

The shock simulation assumes a fixed reduction in Chinese exports.
The substitution mechanism is simplified and does not model dynamic trade adjustments.
Trade value is used as a proxy for supply flows, as physical quantity data were not available.

Future work could incorporate dynamic supply adjustments or firm-level supply chain data.

Conclusion

This project demonstrates that global semiconductor supply chains remain vulnerable to geopolitical disruptions, particularly where supplier networks are concentrated or heavily dependent on China. Strengthening supply chain resilience will likely require greater diversification and strategic risk management.