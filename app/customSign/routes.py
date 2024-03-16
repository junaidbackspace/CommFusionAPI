# routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import database
from app.customSign.services import get_custom_signs
from app.customSign.schemas import CustomSignDetails
from typing import List

router = APIRouter(prefix="/customsign", tags=['Custom Signs'])


@router.get("/{user_id}", response_model=List[CustomSignDetails])
def get_user_custom_signs(user_id: int, db: Session = Depends(database.get_db)):
    custom_signs = get_custom_signs(db, user_id)
    if not custom_signs:
        raise HTTPException(status_code=404, detail="Custom signs not found for the user")
    return custom_signs
