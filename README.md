# Google Image Downloader

This Streamlit app allows users to search for images using Google Image Search (via SerpApi) and download them individually or as a ZIP file.

## Features

- Search for images using keywords
- Display search results in a grid layout
- Download individual images
- Download all found images as a ZIP file
- Customizable number of search results (1-50 images)

## Requirements

- Python 3.7+
- Streamlit
- Requests
- Pillow
- python-dotenv
- SerpApi API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/google-image-downloader.git
   cd google-image-downloader
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your SerpApi API key:
   ```
   SERPAPI_API_KEY=your_serpapi_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. In the sidebar, enter a keyword for image search and adjust the number of images to fetch.

4. Click the "Search" button to start the image search.

5. View the results in the grid layout. You can download individual images or all images as a ZIP file.

## Note

This app uses the SerpApi service, which requires an API key. Make sure you have a valid API key and sufficient credits for your searches.

## License

This project is open-source and available under the MIT License.

## Disclaimer

This app is for educational purposes only. Make sure you comply with Google's terms of service and respect copyright laws when using downloaded images.
