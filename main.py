from fastapi import FastAPI, HTTPException
from models import ImageGenerationRequest, ImageGenerationResponse
from services import generate_image

app = FastAPI(
    title="Image Generation API",
    description="A FastAPI application that uses Replicate's API to generate images.",
    version="1.0.0",
)

@app.post("/generate-image", response_model=ImageGenerationResponse)
async def generate_image_endpoint(request: ImageGenerationRequest):
    """
    Endpoint to generate images using Replicate API.
    
    Parameters:
    - prompt: Text prompt to generate images from
    - model: Model name (default is Stable Diffusion)
    - version: Model version to use for image generation
    - num_outputs: Number of images to generate
    - width: Width of the generated image
    - height: Height of the generated image
    
    Returns:
    - URLs of the generated images
    """
    try:
        response = generate_image(
            prompt=request.prompt,
            model=request.model,
            version=request.version,
            num_outputs=request.num_outputs,
            width=request.width,
            height=request.height
        )
        
        # Extract the image URLs from the response
        image_urls = [output['output'] for output in response.get('outputs', [])]
        
        return ImageGenerationResponse(images=image_urls)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
