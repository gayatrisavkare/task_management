import json
import os

FILE = "history.json"

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)

def add_history(action, filename):
    with open(FILE, "r") as f:
        data = json.load(f)

    data.append({
        "action": action,
        "file": filename
    })

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_history():
    with open(FILE, "r") as f:
        print(json.load(f))

add_history("create","test.txt")
add_history("delete","photo.jpg")        
show_history()