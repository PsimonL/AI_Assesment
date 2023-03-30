import pandas as pd
import matplotlib.pyplot as plt

# Create some sample data
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Create a figure with a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2)

# Add a table to each subplot
for i, ax in enumerate(axs.flatten()):
    # Create a table from the DataFrame
    table_data = df.iloc[i:i+1]
    table = ax.table(cellText=table_data.values, colLabels=table_data.columns, loc='center')
    # Remove the borders from the table
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1, 2)

# Hide the axes labels and ticks
for ax in axs.flatten():
    ax.axis('off')

# Show the plot
plt.show()