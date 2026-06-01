from db.database import initialise_db
from operations.card_ops import add_card, amend_card, remove_card, search_cards, export_to_json

def main():
    initialise_db()
    while True:
        print("\n--- Smartcard Management System ---")
        print("1. Add card")
        print("2. Amend card")
        print("3. Remove card")
        print("4. Search cards (SQL)")
        print("5. Export to JSON")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_card(
                input("Card number: "),
                input("Holder name: "),
                input("Card type (e.g. train/bus/ferry/metro/multi/tram): "),
                float(input("Balance: ")),
                input("Issue date (YYYY-MM-DD): "),
                input("Expiry date (YYYY-MM-DD): ")
            )

        elif choice == "2":
            card_number = input("Card number to amend: ")
            field = input("Field to update (balance / status / holder_name / card_type / expiry_date): ")
            value = input(f"New value for {field}: ")
            amend_card(card_number, **{field: value})

        elif choice == "3":
            remove_card(input("Card number to remove: "))

        elif choice == "4":
            print("Example: SELECT * FROM cards WHERE status = 'active'")
            query = input("Enter SQL query: ")
            rows = search_cards(query)
            if rows:
                for row in rows:
                    print(row)
            else:
                print("No results found.")

        elif choice == "5":
            export_to_json()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()