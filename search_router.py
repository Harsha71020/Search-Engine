from fastapi import APIRouter, HTTPException
from typing import List
from .common import read_files_from_folder
from .indexer import build_inverted_index

router = APIRouter()

FILES_FOLDER = "./data"

files_content = read_files_from_folder(FILES_FOLDER)
inverted_index = build_inverted_index(files_content)

@router.get("/search/", response_model=List[str])
def search_word(query: str):
    query = query.lower()
    if query in inverted_index:
        return list(inverted_index[query])
    else:
        raise HTTPException(status_code=404, detail="Word not found")