import altair as alt
import pandas as pd

winedataR = pd.read_csv(r"C:\Users\NathanKrueger\Downloads\winequality-red.csv",sep=";")
winedataW = pd.read_csv(r"C:\Users\NathanKrueger\Downloads\winequality-white.csv",sep=";")

winedataR.columns = winedataR.columns.str.strip()
winedataW.columns = winedataW.columns.str.strip()

from IPython.display import HTML, display

display(HTML("<h3>Red Wine</h3>"))
display(winedataR.head(10))

display(HTML("<h3>White Wine</h3>"))
display(winedataW.head(10))

chart1 = alt.Chart(winedataR).mark_point().encode(
    x = alt.X("alcohol", scale = alt.Scale(domain=[7, 15])), # this is the percentage of alcohol
    y = alt.Y("density", scale = alt.Scale(domain=[.98, 1.040])),
    color = alt.Color("quality:N").scale(scheme = "plasma")
).properties(
    title = "Red Wine: Alcohol Content Compared to its Density",
     width = 500,
    height = 500
)

chart2 = alt.Chart(winedataW).mark_point().encode(
    x = alt.X("alcohol", scale = alt.Scale(domain=[7, 15])), # this is the percentage of alcohol
    y = alt.Y("density", scale = alt.Scale(domain=[.98, 1.040])),
    color = alt.Color("quality:N").scale(scheme = "plasma")
).properties(
    title = "White Wine: Alcohol Content Compared to its Density",
    width = 500,
    height = 500
)

tqochart = alt.hconcat(chart1, chart2)
tqochart

alt.data_transformers.disable_max_rows()

winedataR['type'] = 'red'
winedataW['type'] = 'white'

paired = pd.concat([winedataR, winedataW])

heatmap = alt.Chart(paired).mark_rect().encode(
    alt.X('alcohol:Q', bin=alt.Bin(maxbins=20), title='Alcohol (%)'),
    alt.Y('quality:O', title='Quality'),
    alt.Color('count()', scale=alt.Scale(scheme='purpleblue'), title='Count')
).properties(
    width=300,
    height=300
).facet(
    column=alt.Column('type:N', title='Wine Type')
).properties(
    title='Alcohol vs Quality: Red vs White Wines'
)

heatmap