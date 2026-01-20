
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/sales_data.csv')

plt.figure()
plt.scatter(df['Marketing_Spend'], df['Sales'])
plt.title('Marketing Spend vs Sales')
plt.xlabel('Marketing Spend')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('../outputs/marketing_vs_sales.png')
plt.close()
