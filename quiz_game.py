 ### changing the code to acccomodate more features and reduce bulkyness
print('Hey Scientist, Welcome to the Biology Quiz!')

# Check if the player wants to play
playing = input('Do you want to play? ')

# Exit if the player does not want to continue
if playing.lower() != 'yes':
    print("Goodbye!")
    quit()

print("Alright, let's brainstorm :)")
score = 0 # to calculate the score for the quiz

# Define questions, answers, and hints in a list of dictionaries for easy access
questions = [
    {
        "question": "What is the scientific name for the largest living organism?",
        "answer": "armillaria ostoyae",
        "hint": "It's a type of fungus found in forests."
    },
    {
        "question": "Which human organ is responsible for producing insulin?",
        "answer": "pancreas",
        "hint": "It is located behind the stomach."
    },
    {
        "question": "What is the term for organisms that make their own food?",
        "answer": "autotrophs",
        "hint": "Plants are an example of these organisms."
    },
    {
        "question": "What type of bond holds the two strands of DNA together?",
        "answer": "hydrogen bonds",
        "hint": "These bonds are relatively weak and occur between complementary bases."
    },
    {
        "question": "What blood type is considered the universal donor?",
        "answer": "o negative",
        "hint": "It's the only blood type that can be safely given to anyone."
    },
    {
        "question": "In which part of the cell does protein synthesis occur?",
        "answer": "ribosomes",
        "hint": "These structures are found on the rough endoplasmic reticulum and in the cytoplasm."
    },
    {
        "question": "Which organ in the human body is primarily responsible for filtering blood?",
        "answer": "kidneys",
        "hint": "This organ filters waste and excess substances to produce urine."
    },
    {
        "question": "What process do plants use to convert sunlight into energy?",
        "answer": "photosynthesis",
        "hint": "This process produces oxygen as a by-product."
    }
]

# Loop through each question
for item in questions:
    attempts = 0  # Count attempts for each question

    # Keep prompting until correct answer or maximum attempts (3) reached
    while attempts < 3:
        answer = input(f"{item['question']} ").lower()  # Convert input to lowercase 

        # Check if answer is correct
        if answer == item['answer']:
            print("Correct!")
            score += 1
            break
        else:
            attempts += 1  # Increment attempts
            print("Incorrect!")
            score -= 0.2

            # Provide hint option if the answer is incorrect after the second attempt
            if attempts == 2:
                use_hint = input("Would you like a hint? (yes/no) ").lower()
                if use_hint == 'yes':
                    print("Hint:", item['hint'])
                    score -= 0.4

            # Offer correct answer after the third failed attempt
            elif attempts == 3:
                reveal_answer = input("Would you like the correct answer? (yes/no) ").lower()
                if reveal_answer == 'yes':
                    print("The correct answer is:", item['answer'])
                    score -= 0.6
                else:
                    print("Let's move to the next question.")
                    
# the game ends:
print("Thank you for playing the Biology Quiz!")
print("You got " + str(score) + " out of " + str(len(questions)) + " questions correct! ")#gives a correct score out of the total number of questions.
print("You got " + str(score / len(questions) * 100) + "%")#gives a percentage

