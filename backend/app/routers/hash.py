from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.tools.hash_generator import generate_hashes

router = APIRouter(
    prefix="/api/hash",
    tags=["Hash Generator"]
)


class HashRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="Text to hash"
    )


@router.post(
    "",
    summary="Generate Cryptographic Hashes",
    description="Generate MD5, SHA1, SHA256 and SHA512 hashes."
)
def generate(request: HashRequest):
    text = request.text.strip()

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Input cannot be empty."
        )

    return generate_hashes(text)