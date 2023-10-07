import streamlit
from PIL import Image

# We're adding a page title. It will be rendered as html heading tag.
streamlit.title("Adding Images")

# We're opening an image file using PIL
cat_image = Image.open("cat.jpg")

# Now, we're ready to display the image in our web page!
streamlit.image(image=cat_image, caption="An image of a cat.")
