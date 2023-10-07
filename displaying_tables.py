import streamlit
import pandas as pd

streamlit.title("Displaying Tables")

# We're creating a dataframe
person_df = pd.DataFrame({
  "Name": ["Alex", "Bob", "Mike"],
  "Age": [20, 21, 22]
})

# Then, we're displaying the dataframe in our web page.
# It will be rendered as an interactive table.
streamlit.dataframe(person_df, width=300, height=200)
