from calculator import calculator
from card_draw import draw_cards

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Use Calculator")
        print("2. Draw Cards")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            calculator()
        elif choice == '2':
            draw_cards()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()