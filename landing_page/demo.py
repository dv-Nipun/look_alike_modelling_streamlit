import streamlit as st

# Create a dictionary to store image data 
images = {
    "Image 1": {
        "path": "healthcare.png",
        "title": "Wellness Hub: Navigating Your Health Journey",
        "description": "This image represents our Wellness Hub project aimed at providing guidance and resources for individuals on their health journey.",
        "url": "http://localhost:8503/"
    },
    "Image 2": {
        "path": "shopping.png",
        "title": "Digital Marketplace: Shopping Simplified",
        "description": "Here's a glimpse of our Digital Marketplace project which aims to simplify the shopping experience for users.",
        "url": "https://huggingface.co/cross-encoder"
    },
    "Image 3": {
        "path": "transportations.png",
        "title": "Transit Tech: Transforming the Way We Move",
        "description": "Transit Tech project is all about revolutionizing the transportation sector to make commuting easier and more efficient.",
        "url": "https://www.freepik.com/"
    },
    "Image 4": {
        "path": "bank.png",
        "title": "Financial Frontiers: Banking Beyond Boundaries",
        "description": "This image showcases our initiative in exploring financial frontiers to extend banking services beyond conventional boundaries.",
        "url": "https://example.com/"
    }
}

# Center align the title
st.markdown("<h1 style='text-align: center;'>HEADING</h1>", unsafe_allow_html=True)

# Function to display images with detailed descriptions on separate pages
def display_image_details(image_name, chosen_tab):
    selected_image_data = images[image_name]

    if chosen_tab == "details":
        st.subheader(selected_image_data["title"])
        st.image(selected_image_data["path"], width=300)  # Adjusted width for better presentation
        st.write(selected_image_data["description"])  # Display description

# Create a container to center the image gallery
center_container = st.container()

# Create a 2x2 grid of columns within the centered container
with center_container:
    col1, col2 = st.columns(2)

    # Function to display images with boundary boxes and hover effects
    def display_image_with_title(image_col, image_name):
        with image_col:
            st.image(images[image_name]["path"], use_column_width=True, output_format='auto')
            button_clicked = st.button(images[image_name]["title"])
            if button_clicked:
                url = images[image_name]["url"]
                if url:
                    st.markdown(f'<meta http-equiv="refresh" content="0;URL={url}">', unsafe_allow_html=True)

    # Display images and titles in the grid with boundary boxes and hover effects
    display_image_with_title(col1, "Image 1")
    st.write("")
    display_image_with_title(col2, "Image 2")

# Create a new row for the second row of images
col3, col4 = st.columns(2)

# Display the remaining images and titles in the grid
display_image_with_title(col3, "Image 3")
st.write("")
display_image_with_title(col4, "Image 4")

# Add shadow boxes around images
st.markdown("<style>img {box-shadow: 5px 5px 5px grey;}</style>", unsafe_allow_html=True)
