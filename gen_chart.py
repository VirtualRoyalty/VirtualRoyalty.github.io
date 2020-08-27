import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

df = pd.read_excel('standup.xlsx')
print(type(df))
fig = px.scatter(df, x="Классика", y="Перформанс", color="Комик", size="size")
fig.show()
pio.write_html(fig, file='_includes/figure.html', auto_open=True)

fig = go.Figure(data=[go.Table(header=dict(values=["Комик", "Выступление", "Год"], align='center'),
                cells=dict(values=[df["Комик"], df["Стендап"], df["Год"]], align='center'))])
pio.write_html(fig, file='_includes/table.html', auto_open=True)
