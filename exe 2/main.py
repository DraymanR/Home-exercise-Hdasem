def show_menu():
    print("\nEnter 1 to a rectangular tower\nEnter 2 to a triangular tower\nEnter 3 to exit")


def show_triangular_menu():
    print("Enter 1 to calculate the perimeter of the triangle\nEnter 2 to print the triangle")


def print_triangle_perimeter(width, height):
    side_length = (width / 2) ** 2 + height ** 2
    side_length = side_length ** 0.5
    perimeter = 2 * side_length + width
    print("The perimeter of the isosceles triangle is:", perimeter)


def print_triangle(width, height):
    if width % 2 == 0 or width > (height * 2):
        print("The triangle cannot be printed")
    else:
        space = int((width / 2) - 1)
        shap_amount = 1
        print(' ' * space, '*' * shap_amount)
        space -= 1
        shap_amount += 2
        count = [1]
        while count[-1] < width - 2:
            count.append(count[-1] + 2)
        del count[0]
        n = int((height - 2) / len(count))
        n_1 = int((height - 2) % (len(count)))
        for i in range(n_1 + n):
            print(' ' * space, '*' * shap_amount)
        for i in range((len(count) - 1)):
            space -= 1
            shap_amount += 2
            for j in range(n):
                print(' ' * space, '*' * shap_amount)
        print('*' * width)


def get_int_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_tower_dimensions_input():
    width = get_int_input("Enter the width of the tower ")
    height = get_int_input("Enter the height of the tower ")
    while height < 2:
        height = get_int_input("Invalid input, The height of a tower must be greater than or equal to 2.")
    return width, height


def choice_rectangular_tower():
    width, height = get_tower_dimensions_input()
    if width == height or abs(width - height) > 5:
        print("The area of the tower is:  ", width * height)
    else:
        print("The scope of the tower is:  ", (width + height) * 2)


def choice_triangular_tower():
    width, height = get_tower_dimensions_input()
    show_triangular_menu()
    choice = input("Enter yor choice: ")
    if choice == "1":
        print_triangle_perimeter(width, height)
    elif choice == "2":
        print_triangle(width, height)
    else:
        print("Invalid choice.")


def main():
    while True:
        show_menu()
        choice = input("Enter yor choice: ")

        if choice == "1":
            choice_rectangular_tower()
        elif choice == "2":
            choice_triangular_tower()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == '__main__':
    main()
