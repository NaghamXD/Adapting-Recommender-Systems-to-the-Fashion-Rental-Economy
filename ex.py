import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Data & Melt (Same as before)
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
    'HR@10': [0.010502, 0.008965, 0.015881, 0.021004, 0.021260, 0.022797, 0.011783, 0.017674, 0.009734, 0.017418, 0.024987, 0.025760, 0.024214, 0.027563],
    'HR@100': [0.046875, 0.064037, 0.034580, 0.046875, 0.075051, 0.098617, 0.084016, 0.083760, 0.060195, 0.089395, 0.073673, 0.077280, 0.100206, 0.100979],
    'HR@10-new': [0.004627, 0.003342, 0.0000, 0.0000, 0.006427, 0.003599, 0.007455, 0.013882, 0.010026, 0.015424, 0.022751, 0.023268, 0.026629, 0.028180],
    'HR@100-new': [0.027506, 0.047815, 0.0000, 0.0000, 0.050129, 0.066581, 0.064267, 0.075835, 0.061954, 0.082262, 0.082213, 0.085832, 0.102637, 0.104188]
}
df = pd.DataFrame(data)
df_melted = df.melt(id_vars=['Method', 'User Type'], value_vars=['HR@10', 'HR@100', 'HR@10-new', 'HR@100-new'], var_name='Metric', value_name='Hit Rate')

# 2. Plot
g = sns.catplot(
    data=df_melted, 
    x='Method', y='Hit Rate', hue='User Type', col='Metric', 
    kind='bar', col_wrap=2, height=4, aspect=1.5, palette='muted', sharey=False 
)

# --- NEW STEP: MOVE LEGEND TO UPPER LEFT ---
sns.move_legend(
    g, "upper left",
    bbox_to_anchor=(0, 1),  # (0,1) is the absolute top-left corner of the figure
    title='User Type',
    frameon=True, # Adds a white box behind the legend so it's readable
)
# -------------------------------------------

g.fig.suptitle('Performance Overview', y=1.05, fontsize=16, fontweight='bold')

for ax in g.axes.flat:
    for label in ax.get_xticklabels(): label.set_rotation(45)
    for container in ax.containers: ax.bar_label(container, fmt='%.3f', padding=2, fontsize=8, rotation=90)

plt.show()
