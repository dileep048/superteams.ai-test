from pydantic import BaseModel
from typing import Optional, List

class ImageGenerationRequest(BaseModel):
    prompt: str
    model: Optional[str] = "stability-ai/stable-diffusion"
    version: Optional[str] = "a9758cb4e9fd6c129f34907ef0a36a364131d4c515049ea6ef8cd6ab201549c8"
    num_outputs: Optional[int] = 1  
    width: Optional[int] = 512 
    height: Optional[int] = 512 

class ImageGenerationResponse(BaseModel):
    images: List[str] 
