# Exercise 1: Menu filtering
"""Exercise 1: Menu filtering.

Load data/menu.json and print every AVAILABLE item under $10.00,
sorted by price, cheapest first.

Expected output shape:
    Green Tea            $3.25
    Iced Coffee          $4.25
    ...

Requirements:
  - use an f-string for the output
  - type-hint every function you write
"""

import json
from pathlib import Path

MENU_PATH = Path(__file__).parent / "data" / "menu.json"


def load_menu() -> list[dict]:
    """Read the menu file and return it as a list of dictionaries."""
    with MENU_PATH.open() as f:
        return json.load(f)


def available_under(menu: list[dict], limit: float) -> list[dict]:
    """Return available items priced below `limit`, sorted cheapest first."""
    # TODO: filter items priced under $10, then sort by price.
    # create empty array
    filtered =[]

    # looping through menu 
    for filtered_menu in menu:
        # find items in condition and puting into empty array
        if filtered_menu["available"] == True and filtered_menu["price"] < limit:
            filtered.append(filtered_menu)
    # sort the array by price
    sorted_price = sorted(filtered, key = lambda i : i["price"])
    return sorted_price



def main() -> None:
    menu = load_menu()
    for item in available_under(menu, 10.00):
        # TODO: print name and price using an f-string.
        # Hint: f"{item['name']:<20} ${item['price']:.2f}"
        print(f"{item['name']:<20} ${item['price']:.2f}")


if __name__ == "__main__":
    main()
