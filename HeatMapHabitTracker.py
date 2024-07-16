# 
# Heat Map Habit Tracker
# A tool to help track habits through visual represenation using color gradients.
#

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

habits = ['Exercise', 'Read']

habit_data = np.random.randint(2, size=(len(habits), 30))

# Generate a calendar of dates for the heatmap
base_date = datetime.today() - timedelta(days=30)  # Start date (30 days ago)
dates = [base_date + timedelta(days=i) for i in range(30)]  # List of dates for the last 30 days

# Plotting the heatmap
plt.figure(figsize=(10, 6))
plt.imshow(habit_data, cmap='YlGn', interpolation='nearest', aspect='auto')

# Customize the plot
plt.title('Habit Tracker Heatmap')
plt.xlabel('Days')
plt.ylabel('Habits')
plt.xticks(np.arange(30), [date.day for date in dates])  # Show day numbers as x-axis labels
plt.yticks(np.arange(len(habits)), habits)  # Show habit names as y-axis labels
plt.colorbar(label='Completion')  # Add color bar indicating completion

# Display the plot
plt.tight_layout()
plt.show()

# Example customization
plt.imshow(habit_data, cmap='BuPu', interpolation='nearest', aspect='auto')
plt.title('My Custom Habit Tracker')
# Customize further as needed

plt.savefig('habit_tracker_heatmap.png')