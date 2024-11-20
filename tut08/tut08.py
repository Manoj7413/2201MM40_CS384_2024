import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt

my_df=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Csv_data/Diwali Sales Data.csv',encoding='unicode_escape')

my_df.head()

my_df.info()

my_df.isnull().sum()

my_df.shape

my_df = my_df.iloc[:,:13]
my_df.dropna(inplace=True)

my_df.info()

my_df['Amount'] = my_df['Amount'].astype('int')
my_df['Amount'].dtype

my_df.columns

my_df.describe()

plot=sns.countplot(x='Gender',data=my_df)

for cnt in plot.containers:
  plot.bar_label(cnt)

my_df_AFM=my_df.groupby(['Gender'])[['Amount']].sum().sort_values('Amount',ascending=False)
my_df_AFM

sns.barplot(x='Gender',y='Amount',data=my_df_AFM)
sns.set(rc={'figure.figsize':(5,5)})

nam=sns.countplot(x='Age Group',hue='Gender',data=my_df)
for cnt in nam.containers:
  nam.bar_label(cnt)

my_df.columns

data_M_UM_A=my_df.groupby(['Marital_Status','Gender'])[['Amount']].sum().sort_values('Amount',ascending=False)
sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(x='Marital_Status',y='Amount',hue='Gender',data=data_M_UM_A)

state_data=my_df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(18,5)})
sns.barplot(x='State',y='Orders',data=state_data)

sector_data=my_df.groupby(['Occupation'],as_index=False)['Orders'].sum()

sns.set(rc={'figure.figsize':(18,5)})
sns.barplot(x='Occupation',y='Orders',data=sector_data)

sector_amount=my_df.groupby(['Occupation','Gender'])['Amount'].sum().reset_index()
sns.barplot(x='Occupation',y='Amount',hue='Gender',data=sector_amount)

product_data=my_df.groupby(['Product_Category'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x='Product_Category',y='Orders',data=product_data)

product_data_amnt=my_df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='Product_Category',y='Amount',data=product_data_amnt)