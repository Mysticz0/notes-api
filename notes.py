from textwrap import indent
import requests
import json

BASE = "http://localhost:8000"

def main():
    while True:
        action = input("""Select an action:\n 
        1. Write a note
        2. Show a note
        3. Show all notes
        4. Search for notes with specific content
        5. Exit\n""")
            
        if action == '1':
            title = input("Enter a title: ")
            body = input("Enter the body of the note: ")
            requests.post(f"{BASE}/write", json={"title": title, "note": body})
            print("\nNote created")

        elif action == '2':
            title = input("Enter the note's title: ")
            response = requests.get(f"{BASE}/notes/{title}")
            print(json.dumps(response.json(), indent = 2))
        
        elif action == '3':
            response = requests.get(f"{BASE}/notes")
            print(json.dumps(response.json(), indent=2))
        
        elif action == '4':
            content = input("Enter what content you want to find in the notes: ")
            response = requests.get(f"{BASE}/search", params={"content" : content})
            print(json.dumps(response.json(), indent=2))

        elif action == '5':
            break

        else:
            print("\nInvalid action. Try again..\n")

if __name__ == "__main__":
    main()