import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic.csv')

# Display the first few rows of the dataset
print(data.head())

# Perform some data analysis
survival_rate = data['Survived'].mean()
print(f"Survival Rate: {survival_rate * 100:.2f}%")

# Plot the age distribution of passengers
plt.hist(data['Age'].dropna(), bins=30, edgecolor='black')
plt.title('Age Distribution of Titanic Passengers')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.show()
