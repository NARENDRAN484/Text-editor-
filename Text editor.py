def display_help():
    print("Simple Command Line Text Editor")
    print("Commands:")
    print("  help - Display this help message")
    print("  new - Create a new file")
    print("  open <filename> - Open an existing file")
    print("  save <filename> - Save the current content to a file")
    print("  exit - Exit the text editor")
    print("  Type your text below, line by line. Type 'end' on a new line to finish input.")

def create_new_file():
    print("Creating a new file. Enter your text below.")
    content = []
    while True:
        line = input()
        if line == 'end':
            break
        content.append(line)
    return "\n".join(content)

def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of {filename}:")
            print(content)
            return content
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return ""

def save_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' saved successfully.")

def main():
    current_content = ""
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == "help":
            display_help()
        elif command == "new":
            current_content = create_new_file()
        elif command.startswith("open "):
            filename = command[5:]
            current_content = open_file(filename)
        elif command.startswith("save "):
            filename = command[5:]
            save_file(filename, current_content)
        elif command == "exit":
            print("Exiting the text editor.")
            break
        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    display_help()
    main()
