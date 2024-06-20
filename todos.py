todos = []
filename = 'todos.txt'

# Function to read the file and load todos
def load_todos(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split('-')
                if len(parts) > 1:
                    todos.append(parts[1].strip())
    except FileNotFoundError:
        print(f"{filename} does not exist. A new file will be created.")

# Function to save todos to the file
def save_todos(filename):
    with open(filename, 'w') as f:
        for index, item in enumerate(todos):
            line = f"{index + 1}-{item}"
            f.write(line + '\n')
    print("Written to todo.txt")

# Load the todos from the file initially
load_todos(filename)
if len(todos)==0:
    print("There is no any previous tasks to be completed")
else:
    print("The list of previous todos: ", todos)

while True:
    prompt = input("Enter options (add/show/edit/delete/save/file/exit): ").strip().lower()
    if prompt == 'add':
        todos.append(input("Enter the To-do work: "))
    elif prompt == 'show':
        if not todos:
            print("No todos to show.")
        else:
            for index, item in enumerate(todos):
                line = f"{index + 1}-{item}"
                print(line)
    elif prompt == 'edit':
        if not todos:
            print("No todos exist to be edited!")
            continue
        try:
            index_value = int(input("Enter the number of todo to edit: "))
            if 1 <= index_value <= len(todos):
                new_todo = input("Enter the new todo: ")
                todos[index_value - 1] = new_todo
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")
    elif prompt == 'delete':
        if not todos:
            print("No todos to delete.")
            continue
        try:
            index_value = int(input("Enter the number of todo to delete: "))
            if 1 <= index_value <= len(todos):
                deleted_todo = todos.pop(index_value - 1)
                print(f"Deleted todo: {deleted_todo}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")
    elif prompt == 'save':
        save_todos(filename)
    elif prompt == 'file':
        print("Contents in File: \n")
        try:
            with open(filename, 'r') as txt:
                for line in txt:
                    print(line, end='')
        except FileNotFoundError:
            print("File not found.")
    elif prompt == 'exit':
        break
    else:
        print("Enter a valid option")
