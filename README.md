# PRODIGY_GA_02


AI Image Generation API with Flask


![image](https://github.com/princegajera1/PRODIGY_GA_02/blob/d4c26da62a65dbd3367946a3089836d8a7c6265c/Screenshot%202025-07-11%20092630.png)
This project is a simple Flask application that serves as a backend for generating images from text prompts using the Hugging Face Inference API for Stable Diffusion.

Features

Image Generation: Takes a text prompt and generates a corresponding image.

Hugging Face Integration: Utilizes the stabilityai/stable-diffusion-2 model hosted on the Hugging Face Hub.

Simple API Endpoint: Provides a single POST endpoint /generate-image for easy integration.

Prerequisites

Before you begin, ensure you have the following installed:

Python 3.x

pip (Python package installer)

Installation

Clone the repository (or download the script):

Generated bash
git clone <your-repository-url>
cd <your-repository-directory>


Install the required Python libraries:

Generated bash
pip install Flask requests
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END
Configuration

Get a Hugging Face API Token:
You will need an API token from Hugging Face to use their Inference API. You can get one from your Hugging Face account settings.

Replace the placeholder token:
Open the app.py file and replace the placeholder API_TOKEN with your actual Hugging Face API token:

Generated python
API_TOKEN = "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"  # 🔁 Replace with your real token
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Python
IGNORE_WHEN_COPYING_END
Usage

Run the Flask application:

Generated bash
python app.py
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

The application will start in debug mode on http://127.0.0.1:5000.

Send a request to the API:
You can use any tool that can send HTTP requests (like curl, Postman, or a simple Python script) to interact with the API.

Example using curl:

Generated bash
curl -X POST \
  http://127.0.0.1:5000/generate-image \
  -H 'Content-Type: application/json' \
  -d '{"prompt": "A futuristic cityscape with flying cars"}'
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END
Expected Response

Success:
If the image is generated successfully, you will receive a JSON response with a URL to the generated image:

Generated json
{
  "url": "URL_to_your_generated_image"
}
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Json
IGNORE_WHEN_COPYING_END

Error:
If there is an error (e.g., the model is loading or there's an issue with your request), you will receive a JSON error message:

Generated json
{
  "error": "Description of the error"
}
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Json
IGNORE_WHEN_COPYING_END
