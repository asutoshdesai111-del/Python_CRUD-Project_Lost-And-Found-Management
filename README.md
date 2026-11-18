# Lost and Found Management

A simple command-line application for recording and managing lost and found items. The program runs an interactive menu in the terminal and keeps item records in memory while it is running.

## Features

- Add a lost item or a found item
- List all recorded items
- Search for an item by its ID
- Update an item's location and contact information
- Delete an item by its ID
- Prevent duplicate item IDs

Each item record contains an ID, name, location, contact information, and type (`Lost` or `Found`).

## Requirements

- Python 3.10 or later (the program uses `match`/`case` syntax)

## Run the application

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py` instead.

## Menu options

| Option | Action |
| --- | --- |
| 1 | Add a lost item |
| 2 | Add a found item |
| 3 | Display all items |
| 4 | Search by item ID |
| 5 | Update an item's location and contact |
| 6 | Delete an item |
| 7 | Exit |

When adding an item, enter a unique numeric ID, its name, location, and contact information. Use that ID to search for, update, or delete the record.

## Data storage

Items are stored in a Python dictionary in memory. Records are available only for the current run and are cleared when the program exits; the application does not currently save data to a file or database.

## Project structure

```text
.
└── main.py    # Interactive lost and found management program
```
