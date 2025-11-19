from datetime import datetime

# Function to find out target audience
def generate_profile(current_age):
    if 0 <= current_age <= 12:
        return "Child"
    elif 13 <= current_age <= 19:
        return "Teenager"
    elif current_age >= 20:
        return "Adult"
    else:
        print("Invalid age")
        return 0

# Function to find ot about user hobbies
def hobbies():
    hobbies_list = []
    while True:
        hobby = input("Enter a favorite hobby (or type 'stop' to exit): ")
        if hobby.lower() == 'stop':
            break
        if hobby.strip():
            hobbies_list.append(hobby)
    return hobbies_list

def main():
    current_year = datetime.now().year
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")
    current_age = current_year - int(birth_year_str)
    target = generate_profile(current_age)
    hobbies_list = hobbies()

    # Interface
    print("\n---")
    print("\nProfile Summary:")
    print(f"Name: {user_name}")
    print(f"Age: {current_age}")
    print(f"Life Stage: {target}")
    if hobbies_list:
        print(f"Favorite hobbies ({len(hobbies_list)}): ")
        for hobby in hobbies_list:
            print(f"- {hobby}")
    else:
        print("You didn't mention any hobbies")
    print("---")

if __name__ == "__main__":
    main()
