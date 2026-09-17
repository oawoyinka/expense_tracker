# Expense Tracker

A terminal-based expense tracker built in Python. Add, view, and analyze personal expenses, with data persisted to a local JSON file between runs.

## Features

- **Add expense** — record an amount, category, and description
- **View expenses** — list every recorded expense
- **Total spending** — sum of all expenses
- **Spending by category** — running total grouped by category
- **Delete expense** — remove a specific expense by its number in the list
- **Persistence** — all expenses are saved to `output.json` and reloaded automatically the next time the program runs

## Requirements

- Python 3

No external dependencies, this project only uses Python's standard library (`json`).

## Usage

Run the script from the terminal:

```bash
python expense_tracker.py
```

You'll see a menu:

```
1. Add expense
2. View expenses
3. Total expenses
4. Spending by category
5. Delete expense
6. Exit
```

Enter the number for the action you want, and follow the prompts. The menu keeps repeating until you choose **Exit**.

## Data Storage

Expenses are stored in `output.json`, in the same folder as the script, as a list of objects:

```json
[
    {
        "amount": 5000.0,
        "category": "Food",
        "description": "Lunch"
    }
]
```

This file is created automatically the first time you add an expense, you don't need to create it yourself.

## Deleting an Expense

Choosing **Delete expense** lists every expense with a number next to it. Enter that number to remove the corresponding expense. Entering an invalid or out-of-range number cancels the deletion instead of crashing the program.

## Notes

- Amounts are stored as floating-point numbers, so decimal values (e.g. `50.75`) are supported.
- This was built as a learning project — a good next step would be adding input validation for empty fields, editing existing expenses, or exporting a category summary to a separate report.