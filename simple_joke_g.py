# import pyjokes

# def tell_joke():
#     # Randomly select a joke
#     joke = pyjokes.get_joke()
#     print(joke)

# def main():
#     print("Welcome to the Joke Generator!")
#     while True:
#         tell_joke()
#         again = input("Do you want to hear another joke? (yes/no): ").strip().lower()
#         if again != 'yes':
#             print("Thank you for using the Joke Generator! Goodbye!")
#             break

# if __name__ == "__main__":
#     main()
import pyjokes
import random

def show_menu():
    print("\n🤣 Random Joke Generator 🤣")
    print("1. Get a random joke")
    print("2. Get a joke by category (neutral, chuck, all)")
    print("3. Exit")

def get_random_joke():
    joke = pyjokes.get_joke()
    print("\n👉", joke)

def get_joke_by_category():
    categories = ['neutral', 'chuck', 'all']
    print("\nAvailable categories:")
    for i, cat in enumerate(categories):
        print(f"{i+1}. {cat}")

    choice = input("Choose a category (1/2/3): ")
    if choice in ['1', '2', '3']:
        selected = categories[int(choice) - 1]
        joke = pyjokes.get_joke(category=selected)
        print("\n👉", joke)
    else:
        print("❌ Invalid choice!")

while True:
    show_menu()
    option = input("Enter your choice: ")

    if option == '1':
        get_random_joke()
    elif option == '2':
        get_joke_by_category()
    elif option == '3':
        print("😄 Thanks for using Random Joke Generator!")
        break
    else:
        print("❌ Invalid input. Please choose 1, 2, or 3.")
