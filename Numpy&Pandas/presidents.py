# import sys
# import numpy as np
# import pandas as pd
# def presidents():
#     df = pd.read_csv("president_heights.csv")
#     x = int(sys.argv[1])
#     y = int(sys.argv[2])
#     heights = df['height(cm)'].iloc[(x):(y)]
#     print(f"The average height of presidents number {x} to {y} is {np.mean(heights):.2f}")
# presidents()

import pandas as pd
import statsmodels.api as sm

# Load the data
df = pd.read_csv("fastfood.csv")

# Define independent variables (X) and dependent variable (y)
X = df[['total_fat', 'sat_fat', 'cholesterol', 'sodium']]
y = df['calories']

# Add a constant
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the results
print(model.mse_total.round(2))  # Mean squared error
print(model.rsquared.round(2))  # R-squared
print(model.params.round(2))    # Coefficients
print(model.pvalues.round(2))   # P-values