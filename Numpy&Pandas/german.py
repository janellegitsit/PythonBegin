import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("german_credit_data.csv")
df = df.rename(columns={'Credit amount': 'Credit_amount'})

x = df[['Age', 'Duration']]
y = df['Credit_amount']

x = sm.add_constant(x)
model = sm.OLS(y, x).fit()

print(model.params.round(2)) 
print(model.rsquared.round(2))