print(' Hey Scientist Welcome to the Biology Quiz!')

playing = input('Do you want to play? ')

if playing != 'yes':
    quit()
print('Alright lets brainstorm: )')

answer = input('What is the scientific name for the largest living organism? ')
if answer.lower() == 'armillaria ostoyae':
    print('Correct!')
else:
    print('Incorrect') 
    
