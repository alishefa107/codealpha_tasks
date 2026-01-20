
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/sales_data.csv')

plt.figure()
plt.bar(df['Month'], df['Website_Visitors'])
plt.title('Monthly Website Visitors')
plt.xlabel('Month')
plt.ylabel('Visitors')
plt.tight_layout()
plt.savefig('../outputs/website_visitors.png')
plt.close()
