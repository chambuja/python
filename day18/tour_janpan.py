import matplotlib.pyplot as plt
import pandas
import matplotlib.pyplot

df = pandas.read_csv('japan.csv')
print(df[country])

df = pandas.read_csv('japan.csv')
year_2023 = df[(df["Year"] == 2023) & (df['purpose_of_visit_to_Japan'] == 'Tourism')]
data = year_2023.groupby('Country / Area')['visitor Arrivals'].sum()

data = year_2023.groupby('Country / Area')['visitor Arrivals'].value_counts()
data.plot.pie()
plt.show()
print(data)

# 2023에 각 나라별로 방문자수를 알고 싶음
