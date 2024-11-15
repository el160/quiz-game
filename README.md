# quiz-game
The idea here is ask users a punch of Questions and if they get it right they proceed to the next question and if they get it wrong they game breaks
Quiz Structure: Each question, answer, and hint is stored in a dictionary within a list called questions for organized access.
Attempts Tracking: A counter attempts is used to track how many attempts the user has made per question.
Correct Answer Check: If the answer is correct, "Correct!" is printed, and the program moves to the next question.
Hint Offer: After two incorrect attempts, the user is asked if they want a hint. If they say "yes," the hint is displayed.
Reveal Answer: If the user fails the third attempt, they are asked if they would like the correct answer. If they agree, it’s revealed; otherwise, the program moves to the next question.
At the end of the game the user is given a percentage score of what they got right out of the total number of questions asked.