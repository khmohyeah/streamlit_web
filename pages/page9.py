import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff
from bokeh.plotting import figure

#st.line_chart
st.subheader("st.line_chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

#st.area_chart
st.subheader("st.area_chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.area_chart(chart_data)

#st.bar_chart
st.subheader("st.bar_chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])
st.bar_chart(chart_data)

#st.pyplot
st.subheader("st.pyplot")
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

#st.altair_chart
st.subheader("st.altair_chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.altair_chart(c, use_container_width=True)

#st.vega_lite_chart
st.subheader("st.vega_lite_chart")
chart_data = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
st.vega_lite_chart(chart_data, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})

#st.plotly_chart
st.subheader("st.plotly_chart")
# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)


#st.bokeh_chart
st.subheader("st.bokeh_chart")
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')
p.line(x, y, legend_label='Trend', line_width=2)
st.bokeh_chart(p, use_container_width=True)

st.subheader("st.latex")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.text('This is some text.')