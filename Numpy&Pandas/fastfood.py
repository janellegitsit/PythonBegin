import pandas as pd
import statsmodels.api as sm
df = pd.read_csv("fastfood.csv")
x = df[['total_fat', 'sat_fat', 'cholesterol', 'sodium']]
y = df['calories']
x = sm.add_constant(x)
mod = sm.OLS(y, x).fit()
print(mod.mse_total.round(2))
print(mod.rsquared.round(2))
print(mod.params.round(2))
print(mod.pvalues.round(2))
