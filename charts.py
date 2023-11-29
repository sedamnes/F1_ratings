import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('F1 - aux.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Year'] = df['Date'].dt.year

fig, ax = plt.subplots(figsize=(15, 5))
sns.scatterplot(data=df, x='Date', y='Bard Wikipedia eventfulness', hue='Circuit')
plt.subplots_adjust(right=0.45, bottom=0.05, left=0.05, top=0.95)
plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0, title='Circuit', ncol=2)
plt.savefig('scatter_eventfulness_by_year.pdf')
plt.savefig('scatter_eventfulness_by_year.png', dpi=300)
plt.show()

fig2, ax2 = plt.subplots(figsize=(15, 7))
sns.stripplot(data=df, x='Circuit', y='Bard Wikipedia eventfulness', hue='Year')
plt.subplots_adjust(right=0.92, bottom=0.5, left=0.05, top=0.95)
plt.legend(bbox_to_anchor=(1.08, 1), borderaxespad=0, title='Year')
plt.xticks(rotation=90)
plt.savefig('scatter_eventfulness_by_circuit.pdf')
plt.savefig('scatter_eventfulness_by_circuit.png', dpi=300)
plt.show()
