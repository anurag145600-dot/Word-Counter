def count_words(file_name):
    try:
        # Open and read file
        with open(file_name, "r") as file:
            content = file.read()

        # Split content into words
        words = content.split()

        # Count words
        word_count = len(words)

        print("\n===== WORD COUNTER =====")
        print(f"File Name: {file_name}")
        print(f"Total Words: {word_count}")

    except FileNotFoundError:
        print("\nError: File not found!")
        print("Please check the file name and try again.")

    except Exception as error:
        print("\nAn unexpected error occurred:")
        print(error)


# Main Program
print("===== WORD COUNTER PROGRAM =====")

file_name = input("Enter the file name: ")

count_words(file_name)