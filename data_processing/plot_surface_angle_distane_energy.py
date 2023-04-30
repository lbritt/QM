import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# read data from Excel file
df = pd.read_csv('data2.csv', skiprows=1, nrows=629)




 # extract columns as lists
distance = df.iloc[:, 0].tolist() # extract first column (index 0)
angle = df.iloc[:, 1].tolist() # extract second column (index 1)
energy = df.iloc[:, 2].tolist() # extract third column (index 2)

#distance = df.iloc[0:572, 1] # df["Title"].iloc[:] #extracts the column titled "Title"
#angle = df.iloc[572:1144, 1]
#energy = df.iloc[1144:1716, 1]



# convert units
distance = [x/1 for x in distance] # divide by 10 to convert to nm
energy = [x*627 for x in energy] # multiply by 627 to convert to kcal/mol

# create 3D plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_trisurf(distance, angle, energy, cmap='viridis', edgecolor='none')

# add labels and title
ax.set_xlabel('Angle (degree)')
ax.set_ylabel('Distance (A)')
ax.set_zlabel('Energy (kCal/mol)')
plt.title('Energy Surface')

# show plot
plt.show()
