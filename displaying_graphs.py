import streamlit
import pandas as pd

streamlit.title("Displaying Graphs")

# We will take the power as input
power = streamlit.slider("Power Value:", min_value=0, max_value=10)

x = range(1, 11, 1)
y = [i ** power for i in x] # We're generating an array that contains the powers of all elemnts in 'x'

# To display a chart, we have to put our data in a dataframe
df = pd.DataFrame({"x": x, "y": y})

# Now, we're ready to display our line chart. We have to specify which columns of the dataframe should be uesd by x and y axis
streamlit.line_chart(data=df, x="x", y="y")
