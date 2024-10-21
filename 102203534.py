import streamlit as st
import requests
import os
from io import BytesIO
from zipfile import ZipFile
from PIL import Image
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your SerpApi API key from the .env file
api_key = os.getenv('SERPAPI_API_KEY')  # Replace with your actual SerpApi key in .env

def get_image_urls(query, num_results=10):
    # Set up the search parameters
    params = {
        "engine": "google_images",
        "q": query,  # Search query
        "num": num_results,  # Number of image results to fetch
        "api_key": api_key  # SerpApi key
    }

    try:
        # Send the request to the SerpApi endpoint with a timeout
        response = requests.get("https://serpapi.com/search", params=params, timeout=10)

        # Check for successful request
        if response.status_code == 200:
            results = response.json()  # Parse JSON response
            image_urls = []

            if "images_results" in results:
                for image in results["images_results"]:
                    image_urls.append(image["original"])

            return image_urls
        else:
            st.error(f"Error: Unable to fetch data (Status code: {response.status_code})")
            return []
    except requests.exceptions.Timeout:
        st.error("Error: The request timed out. Please try again later.")
        return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error: An error occurred while fetching data: {e}")
        return []

def download_images_as_zip(image_urls):
    zip_buffer = BytesIO()
    with ZipFile(zip_buffer, 'w') as zip_file:
        for idx, url in enumerate(image_urls):
            response = requests.get(url)
            if response.status_code == 200:
                img_data = response.content
                img_name = f'image_{idx + 1}.jpg'
                zip_file.writestr(img_name, img_data)
    zip_buffer.seek(0)
    return zip_buffer

# Streamlit App UI
st.title("Google Image Downloader")
st.write("Search and download images using the SerpApi.")

# Sidebar for user input
st.sidebar.header("Search Settings")
query = st.sidebar.text_input("Enter the keyword for image search:", "")
num_images = st.sidebar.slider("Number of images to fetch:", min_value=1, max_value=50, value=10, step=1)

if st.sidebar.button("Search"):
    if query:
        with st.spinner("Fetching images..."):
            image_urls = get_image_urls(query, num_images)

        if image_urls:
            st.success(f"Found {len(image_urls)} images for '{query}'")
            
            # Display images in a grid layout
            cols = st.columns(4)
            for i, url in enumerate(image_urls):
                with cols[i % 4]:
                    try:
                        image = Image.open(BytesIO(requests.get(url).content))
                        st.image(image, caption=f"Image {i + 1}", use_column_width=True)
                        st.download_button(label="Download Image", data=requests.get(url).content, file_name=f"image_{i + 1}.jpg", mime="image/jpeg")
                    except Exception as e:
                        st.warning(f"Could not display image {i + 1}")
            
            # Option to download all images as a zip file
            if st.button("Download All Images as ZIP"):
                zip_file = download_images_as_zip(image_urls)
                st.download_button(label="Download ZIP", data=zip_file, file_name="images.zip", mime="application/zip")
        else:
            st.error("No images found. Please try a different search term.")
    else:
        st.warning("Please enter a keyword to search for images.")
