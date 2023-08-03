import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

from utils.csv.load_csv import df_from_csv
from utils.plot.common import PlotNames
from utils.plot.histogram import histogram
from utils.plot.scatter import scatter

aps = df_from_csv(name="aps_2019", separator=";")
aps_variables = df_from_csv(name="aps_2019_variables", separator=";")

aps_variables = aps_variables["Label"]
print(aps_variables)

tea_identifier: str = "TEA19"
perceived_skill_identifier: str = "Suskil19"
fear_of_failure_identifier: str = "Frfail19"

data = aps[[tea_identifier, perceived_skill_identifier, fear_of_failure_identifier]]
for col in data.columns:
    data[col] = data[col].apply(lambda x: float(x.replace(",", ".")) / 100)

def expit(x: float) -> float:
    exp_x = np.exp(x)
    return exp_x / (exp_x + 1.0)

def logit(x: float) -> float:
    return np.log(x) - np.log(1.0 - x)


data_logit = data.apply(logit)
corr = data_logit.corr()

X = data_logit[[perceived_skill_identifier]].to_numpy()
X = sm.add_constant(X)
y = data_logit[[tea_identifier]].to_numpy()[:, 0]

results = sm.OLS(y, X).fit()

skills = X[:, 1]



prediction = X @ results.params

plt.scatter(skills, y)
plt.plot(skills, prediction, "r")
plt.title("fit")

errors = y - prediction
scatter(x=skills, y=errors, names=PlotNames(title="errors~skills"))
scatter(x=y, y=errors, names=PlotNames(title="errors~tea"))
histogram(x=errors, bins=8, names=PlotNames(title="errors dist"))

plt.show()

print(corr)
print(results.summary())