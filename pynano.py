import subprocess as sp

content = []

def nano(content):
    sp.run(["clear"])
    user_input = ""
    while user_input != "exit":
        user_input = input("")
        if user_input == "~S":
            filename = input("Enter filename: ")
            with open(filename, "w") as file:
                for line in content:
                    file.write(line)
                    file.write("\n")
            print("File saved successfully!")
        if user_input == "~O":
            filename = input("Enter filename: ")
            try:
                with open(filename, "r") as file:
                    content = file.read().splitlines()
                    sp.run(["clear"])
                    for line in content:
                        print(line, end='\n')
            except FileNotFoundError:
                print(f"Error: File {filename} not found.")
        else:
            content.append(user_input)
        
nano(content)