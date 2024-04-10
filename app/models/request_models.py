from pydantic import BaseModel

class SynthesizeRequest(BaseModel):
    text: str
    speaker: int = 1
