import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_lowercase + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Choose from 'low', 'medium', or 'high'")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Length must be a positive integer.")
            return
        complexity = input("Enter the complexity level (low/medium/high): ").lower()
        if complexity not in ['low', 'medium', 'high']:
            print("Invalid complexity level. Choose from 'low', 'medium', or 'high'")
            return
        password = generate_password(length, complexity)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
