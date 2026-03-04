def show_menu():
    print("\nTo-Do List App")
    print("1) Add task")
    print("2) View tasks")
    print("3) Complete task")
    print("4) Delete task")
    print("5) Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "⬜"
        print(f"{i}. {status} {t['text']}")

def add_task(tasks):
    text = input("Task: ").strip()
    if text:
        tasks.append({"text": text, "done": False})
        print("Added.")
    else:
        print("Empty task ignored.")

def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Complete which task number? ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("Completed.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Delete which task number? ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            print("Deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
