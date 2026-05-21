from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Note(BaseModel):
    title: str
    note: str

notes = {}
app = FastAPI()

@app.get("/")
def root():
    return {"content" : "Welcome to the NoteAPI!"}

@app.post("/write")
def write_note(note: Note):
    notes[note.title] = note.note

@app.get("/notes/{title}")
def search_notes_title(title: str):
    if title in notes:
        return {"content": notes[title]}
    else: 
        raise HTTPException(status_code=404, detail=f"'{title}' not found")

@app.get("/notes")
def show_all_notes():
    return {"content" : notes}