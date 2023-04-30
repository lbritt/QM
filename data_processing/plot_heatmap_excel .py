import pandas as pd
import matplotlib.pyplot as plt

# read data from Excel file
df = pd.read_csv('data2.csv', skiprows=1, nrows=638)

# extract columns as lists
distance = df.iloc[:, 0].tolist() # extract first column (index 0)
angle = df.iloc[:, 1].tolist() # extract second column (index 1)
energy = df.iloc[:, 2].tolist() # extract third column (index 2)

# convert units
distance = [x/1 for x in distance] # divide by 10 to convert to nm
energy = [x*627 for x in energy] # multiply by 627 to convert to kcal/mol

# create contour plot
plt.tricontourf(distance, angle, energy, cmap='coolwarm')

# add labels and title
plt.xlabel('Distance (A)')
plt.ylabel('Angle (degree)')
plt.title('Energy Surface')

# add colorbar
plt.colorbar(label='Energy (kcal/mol)')

# show plot
plt.show()
