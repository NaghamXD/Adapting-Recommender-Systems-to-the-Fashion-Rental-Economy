import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Prepare the full dataset
data = {
    'Method': [
        'Pop', 'Pop', 'Rep', 'Rep', 'Rep + Pop', 'Rep + Pop', 
        'BPR', 'BPR', 'ALS', 'ALS', 
        'Img Embed', 'Img Embed', 'Tag Embed', 'Tag Embed'
    ],
    'User Type': [
        'Ind', 'Groups', 'Ind', 'Groups', 'Ind', 'Groups', 
        'Ind', 'Groups', 'Ind', 'Groups', 
        'Ind', 'Groups', 'Ind', 'Groups'
    ],
    'HR@10': [0.0220, 0.0451, 0.0546, 0.0756, 0.0607, 0.0776, 0.0371, 0.0479, 0.0379, 0.0551, 0.0355, 0.0386, 0.0541, 0.0634],
    'HR@100': [0.1158, 0.2088, 0.1255, 0.1532, 0.1957, 0.2633, 0.1949, 0.2223, 0.1755, 0.2398, 0.1334, 0.1443, 0.2324, 0.2378],
    'HR@10-new': [0.0267, 0.0532, 0.0000, 0.0000, 0.0113, 0.0059, 0.0437, 0.0545, 0.0378, 0.0625, 0.0341, 0.0365, 0.0447, 0.0496],
    'HR@100-new': [0.1141, 0.2013, 0.0000, 0.0000, 0.1270, 0.1933, 0.2193, 0.2429, 0.1602, 0.2226, 0.1531, 0.1608, 0.2135, 0.2141]
}

df = pd.DataFrame(data)

# 2. Reshape data to "Long Format" (Required for complex seaborn plots)
# This stacks all metric columns into one 'Value' column and creates a 'Metric' identifier column
df_melted = df.melt(
    id_vars=['Method', 'User Type'], 
    value_vars=['HR@10', 'HR@100', 'HR@10-new', 'HR@100-new'],
    var_name='Metric', 
    value_name='Hit Rate'
)

# 3. Create the Faceted Chart
# col_wrap=2 creates a 2x2 grid
# sharey=False allows each chart to scale to its own data range (crucial here!)
g = sns.catplot(
    data=df_melted, 
    x='Method', 
    y='Hit Rate', 
    hue='User Type', 
    col='Metric', 
    kind='bar', 
    col_wrap=2, 
    height=4, 
    aspect=1.5,
    palette='muted',
    sharey=False 
)

# 4. Polish the Layout
g.fig.suptitle('Performance Overview Across All Metrics', y=1.02, fontsize=16, fontweight='bold')

# Rotate x-axis labels to prevent overlapping
for ax in g.axes.flat:
    for label in ax.get_xticklabels():
        label.set_rotation(45)

# Add numeric labels on top of the bars
for ax in g.axes.flat:
    for container in ax.containers:
        ax.bar_label(container, fmt='%.3f', padding=2, fontsize=8, rotation=90)

plt.tight_layout()
plt.show()