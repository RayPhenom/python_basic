try:
   
    with open("my_file.txt", "w") as file:
        file.write("This is the Onix's line.\n")
        file.write("The number is 42.\n")
        file.write("This is the third line with more text.\n")
    print("File 'my_file.txt' created and written successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred: {e}")

try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nContents of 'my_file.txt':")
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred: {e}")

try:
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line.\n")
        file.write("Another number: 100.\n")
        file.write("Final line in the file.\n")
    print("\nAdditional lines appended to 'my_file.txt' successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred: {e}")

try:
    with open("my_file.txt", "r") as file:
        updated_content = file.read()
        print("\nUpdated contents of 'my_file.txt':")
        print(updated_content)
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred: {e}")

finally:
    print("\nScript execution completed.")
