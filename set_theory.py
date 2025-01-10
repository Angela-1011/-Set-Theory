def input_set(prompt):
    """Helper function to input a set."""
    while True:
        try:
            elements = input(prompt).strip().split()
            return set(elements)
        except ValueError:
            print("Invalid input. Please enter elements separated by spaces.")

def display_operations():
    """Display operation choices."""
    print("\nChoose an operation:")
    print("------------------------------------")
    print("| 1. Union (A ∪ B)                |")
    print("| 2. Intersection (A ∩ B)         |")
    print("| 3. Difference (A − B and B − A) |")
    print("| 4. Subset Check (A ⊆ B and B ⊆ A)|")
    print("| 5. Exit                         |")
    print("------------------------------------")

def main():
    print("Set Theory Operations\n")
    print("Instructions: Enter elements of the set separated by spaces. Duplicates will be removed.")

    # Input sets
    A = input_set("Enter elements of Set A separated by spaces: ")
    print("------------------------------------")
    B = input_set("Enter elements of Set B separated by spaces: ")

    while True:
        display_operations()
        choice = input("\nEnter your choice: ").strip()

        print("------------------------------------")

        if choice == '1':
            print(f"\nUnion (A ∪ B): {A | B}")
        elif choice == '2':
            print(f"\nIntersection (A ∩ B): {A & B}")
        elif choice == '3':
            print(f"\nDifference (A − B): {A - B}")
            print(f"Difference (B − A): {B - A}")
        elif choice == '4':
            print(f"\nIs A a subset of B (A ⊆ B)?: {A <= B}")
            print(f"Is B a subset of A (B ⊆ A)?: {B <= A}")
        elif choice == '5':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid operation.")

        print("------------------------------------")

if __name__ == "__main__":
    main()
