# FastAPI Image Generation API

This FastAPI application interacts with Replicate's API to generate images based on user-provided prompts.

## Requirements
- Python 3.8+
- FastAPI
- Uvicorn
- Requests
- dotenv

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the dependencies.
    ```bash
    pip install -r requirements.txt
4. Create a .env file in the root directory and add your Replicate API key:
    ```bash
    REPLICATE_API_TOKEN=your_replicate_api_key_here
5. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload


### **API Endpoint: POST /generate-image**

#### **Description:**
Generates an image based on the provided text prompt.

#### **Request Body:**

| Field        | Type    | Description                                                          | Required |
|--------------|---------|----------------------------------------------------------------------|----------|
| `prompt`     | String  | The text prompt for image generation (e.g., "A futuristic city at sunset"). | Yes      |
| `model`      | String  | The model to use for generating the image (default: "stability-ai/stable-diffusion"). | No       |
| `version`    | String  | The specific version of the model to use (optional).                  | No       |
| `num_outputs`| Integer | The number of images to generate (default: 1).                        | No       |
| `width`      | Integer | The width of the generated image in pixels (default: 512).            | No       |
| `height`     | Integer | The height of the generated image in pixels (default: 512).           | No       |

#### **Response:**

| Field    | Type   | Description                                       |
|----------|--------|---------------------------------------------------|
| `images` | Array  | List of URLs of the generated images.              |

#### **Example Request:**
```json```
{
  "prompt": "A futuristic city at sunset",
  "num_outputs": 2,
  "width": 1024,
  "height": 1024
}


#### **Example Response:**
```json```
{
  "images": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg"
  ]
}

