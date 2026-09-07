import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/titanic.csv')

describe_ = df.describe(include="all")
# print(describe_)

# print(df.columns)

gt_30 = df[df['Age'] > 30]
# print(gt_30)

# print(df.sort_values('Age', ascending=False))

bar_chart = df.groupby('Pclass')['Survived'].sum().plot(kind='bar')
# print(bar_chart)
# plt.show()

is_null = df.isnull().sum()
# age, cabin and embarked have nulls
# print(is_null)

# df['Age'] = df['Age'].fillna(df['Age'].mean())

df = df.dropna(subset=['Age'])
is_null = df.isnull().sum()
print(is_null)
# print(fill_null_age)