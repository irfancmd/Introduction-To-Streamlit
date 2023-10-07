import streamlit
import pandas as pd

streamlit.title("Multi Column Web Pages")

left_column, right_column = streamlit.columns(2)

power = left_column.slider("Power Value:", min_value=0, max_value=10)

x = range(1, 11, 1)
y = [i ** power for i in x]

df = pd.DataFrame({"x": x, "y": y})

right_column.line_chart(data=df, x="x", y="y")
