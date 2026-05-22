from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Note(BaseModel):
    title: str = "Untitled"
    note: str = ""

notes = []
app = FastAPI()

@app.get("/")
def root():
    return {"content" : "Welcome to the NoteAPI!"}

@app.post("/write")
def write_note(note: Note):
    notes.append({"title" : note.title, "body" : note.note})

@app.get("/notes/{title}")
def search_notes_title(title: str):
    for note in notes:
        if title == note["title"]:
            return note
        
    raise HTTPException(status_code=404, detail=f"'{title}' not found")

@app.get("/notes")
def show_all_notes():
    return notes

@app.get("/search")
def show_notes_containing(content: str):
    notes_with_content = []
    for note in notes:
        if content in note["body"]: 
            notes_with_content.append(note)
    
    if notes_with_content != []:
        return notes_with_content
    else:
        raise HTTPException(status_code=404, detail=f"{content} not found")