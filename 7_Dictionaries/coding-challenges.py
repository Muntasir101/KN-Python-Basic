"""
Create To-Do lists. Filter by category.
"""

todo_items = {
    "Shopping": ["Buy Fruits", "Buy Vegetables", "Bug Bread"],
    "Work": ["Finish project", "Send mail to developers"],
    "Personal": ["walking", "meditation"]
}


def filter_by_category(category):
    if category in todo_items:
        print(f"Category: {category}")
        print("Items")
        for item in todo_items[category]:
            print(f"Item: {item}")

    else:
        print("Invalid category")


filter_by_category("Shopping12")
