from calculator import calculator
from card_draw import draw_cards
from weather import get_weather

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Use Calculator")
        print("2. Draw Cards")
        print("3. Get Weather")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            calculator()
        elif choice == '2':
            draw_cards()
        elif choice == '3':
            city = input("Enter the name of the city: ")
            api_key = "3579c46605605203ce0c54471372ec2c"  # Replace with your actual API key
            get_weather(city, api_key)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()