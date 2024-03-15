import random

# Define the quiz questions and answers with answer choices
quiz_questions = {
    "What is the capital of France?": ["Paris", "London", "Berlin", "Rome"],
    "What is the largest planet in our solar system?": ["Jupiter", "Saturn", "Neptune", "Mars"],
    "Who wrote 'Romeo and Juliet'?": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
    "What is the chemical symbol for water?": ["H2O", "CO2", "NaCl", "O2"],
    "What is the powerhouse of the cell?": ["Mitochondria", "Nucleus", "Ribosome", "Golgi Apparatus"]
}

def load_questions():
    """Load quiz questions."""
    return list(quiz_questions.keys())

def present_question(question, choices):
    """Present a quiz question along with answer choices and prompt the user for an answer."""
    print(question)
    for i, choice in enumerate(choices, start=0):
        print(f"{i}. {choice}")
    user_answer = input("Your answer (enter the number corresponding to your choice): ")
    return user_answer


def evaluate_answer(question, user_answer):
    """Evaluate the user's answer."""
    correct_answer = quiz_questions[question][0]
    user_choice_index = int(user_answer) - 1
    if quiz_questions[question][user_choice_index] == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")
        return 0

def display_final_results(score, total_questions):
    """Display the final results."""
    print("Quiz completed!")
    print(f"Your final score is: {score}/{total_questions}")
    print("Thanks for playing!")

def play_quiz():
    """Play the quiz game."""
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions. Let's get started!\n")

    questions = load_questions()
    random.shuffle(questions)

    score = 0

    for question in questions:
        user_answer = present_question(question, quiz_questions[question][0:])
        score += evaluate_answer(question, user_answer)
        print()

    display_final_results(score, len(questions))

def main():
    play_again = True
    while play_again:
        play_quiz()
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == "yes"

if __name__ == "__main__":
    main()
