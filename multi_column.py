import streamlit
import pandas as pd

streamlit.title("Multi Column Web Pages")

# We're creating two columns and assigning their references to variables
left_column, right_column = streamlit.columns(2)

# To put the slider in a column, use <column_name>.slider method
power = left_column.slider("Power Value:", min_value=0, max_value=10)

x = range(1, 11, 1)
y = [i ** power for i in x]

df = pd.DataFrame({"x": x, "y": y})

# To put the line chart in a column, use <column_name>.line_chart method
right_column.line_chart(data=df, x="x", y="y")
