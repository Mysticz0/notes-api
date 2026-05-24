from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

class Note(BaseModel):
    title: str = "Untitled"
    note: str = ""

notes = sqlite3.connect("notes.db", check_same_thread=False)
init_cursor = notes.cursor()
init_cursor.execute("""CREATE TABLE IF NOT EXISTS notes 
                    (id INTEGER PRIMARY KEY, 
                    title TEXT, 
                    body TEXT)""")
notes.commit()

app = FastAPI()

@app.get("/")
def root():
    return {"content" : "Welcome to the NoteAPI!"}

@app.post("/write")
def write_note(note: Note):
    with notes:
        notes.execute("INSERT INTO notes (title, body) VALUES (?, ?)", (note.title, note.note))
    

@app.get("/notes/{title}")
def search_notes_title(title: str):
    with notes:
        result = notes.execute("SELECT * FROM notes WHERE title = ?", (title,)).fetchall()
        if result != []:
            return result
        else:
            raise HTTPException(status_code=404, detail=f"'{title}' not found")

@app.get("/notes")
def show_all_notes():
    with notes:
        return notes.execute("SELECT * FROM notes").fetchall()

@app.get("/search")
def show_notes_containing(content: str):   
    with notes:
        result = notes.execute(f"SELECT * FROM notes WHERE body LIKE ?", (f"%{content}%",)).fetchall()
        if result != []:
            return result
        else:
            raise HTTPException(status_code=404, detail=f"{content} not found")