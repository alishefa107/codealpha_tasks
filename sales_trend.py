
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/sales_data.csv')

plt.figure()
plt.plot(df['Month'], df['Sales'])
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('../outputs/sales_trend.png')
plt.close()
