from fastapi import FastAPI, HTTPException

notes = {}

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to the NoteAPI!"

@app.post("/write")
def write_note(title, note):
    notes[title] = note
    return

@app.get("/notes/{title}")
def search_notes_title(title: str):
    if title in notes:
        return notes[title]
    else: 
        raise HTTPException(status_code=404, detail=f"'{title}' not found")

@app.get("/notes")
def show_all_notes():
    return notes