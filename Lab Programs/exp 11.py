import numpy as np
fuel_efficiency = np.array([22, 25, 28, 30, 26, 24, 29])
average_efficiency = np.mean(fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency, "mpg")
model1 = fuel_efficiency[0]
model2 = fuel_efficiency[3]
percentage_improvement = ((model2 - model1) / model1) * 100
print("Percentage Improvement from Model1 to Model2:", percentage_improvement, "%")