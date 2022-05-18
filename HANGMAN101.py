import random

word_dict = {'GAME': ['UNCHARTED', 'MINECRAFT', 'DESTINY', 'WITCHER', 'DOOM', 'FORTNIGHT'],
             'CHARACTER': ['KRATOS', 'DRAKE', 'FRAZER', 'SULLIVAN', 'LAZAREVIC', 'ELLIE', 'JOEL'],
             'GAME DIRECTOR': ['KOJIMA', 'FARES', 'HENNING', 'DRUCKMAN', 'BARLOG', 'MIYAMOTO', 'BOON', 'RUBIN',
                               'AMANO'],
             'GAME CREATURES': ['CRONES', 'YAGA', 'POKEMON', 'TRICO', 'AMYGDALA', 'PIKACHU'],
             'GAME MONSTERS': ['LESHEN', 'EKHIDNA', 'VALKYRIES', 'TROLLS', 'WENDIGO', 'DRAYGR', 'HYDRA', 'OROCHI',
                               'LYNEL'],
             'GAME BOSSES': ['ALIEN', 'ARES', 'GORO', 'MALUS', 'VERGIL', 'DAUD', 'DEATHSTROKE', 'CYBERDEMON', 'SAKON',
                             'ATHEON', 'BAAL', 'KAHN', 'DEATHSHEAD', 'CROTA', 'LUDWIG', 'DRACULA', 'SKOLAS'],

             }


def get_category_word():
    category = random.choice(list(word_dict.keys())).upper()
    return category, random.choice(word_dict[category])


def display_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()


def hangman_pics(tries):
    pics = [
        '''
           +---+
           |   |      
           O   |      
          \\|/  |      
          / \\  |      
               |     
           =====
        ''',

        '''
           +---+
           |   |      
           O   |      
          \\|/  |       
          /    |      
               |     
           =====
        ''',

        '''
           +---+
           |   |      
           O   |      
          \\|/  |      
               |      
               |     
           =====
        ''',

        '''
           +---+
           |   |      
           O   |      
          \\|   |      
               |      
               |     
           =====
        ''',

        '''
           +---+
           |   |      
           O   |      
           |   |      
               |      
               |     
           =====
        ''',

        '''
           +---+
           |   |      
           0   |      
               |    
               |      
               |     
           =====
        ''',

        '''
           +---+
           |   |      
               |      
               |    
               |      
               |     
           =====
        '''
    ]
    return pics[tries]


def game(random_):
    word = random_[1]
    print(word)
    category = random_[0]
    dashed_word = '_ ' * len(word)
    game_won = False
    players_letters = []
    players_words = []
    tries = 6
    print('Welcome to the Hangman game! Lets begin, \n')
    player_name = input("Enter your name in the console: ")
    # print(word)
    print(hangman_pics(tries))
    print(f'The category is : {category}')
    print(dashed_word)
    while True:
        player_input = input(f'{player_name}, enter a letter or a word: ').upper()
        # print(word_input)
        if not player_input.isalpha():
            print(f"{player_name}, your response is not valid, please enter ONLY letters and words.")
            continue
        if player_input in players_words or player_input in players_letters:
            print(f'{player_name},you have already used this letter: {player_input}')
            print(f'The category is : {category}')
            print(f'missed letters: {" ".join([c for c in players_letters if c not in list(word)])}')
            print(f'missed words:  {" ".join([m for m in players_words if m not in list(word)])}')
            continue
        if len(player_input) > 1:
            if player_input == word:
                print(f'{player_name}, congratulations! You are the champion! You guessed correctly: {word}!')
                break
            else:
                players_words.append(player_input)
                tries -= 1
                print(f'Wrong, tries left: {tries}')
                print(f'The category is : {category}')
                print(hangman_pics(tries))
                display_word(word, players_letters)
                print(f'missed letters: {" ".join([c for c in players_letters if c not in list(word)])}')
                print(f'missed words:  {" ".join([m for m in players_words if m not in list(word)])}')
                if tries == 0:
                    print(f'Bad luck! {player_name}, you lost, the correct word is: {word}')
                    break
                continue

        if player_input in word:
            players_letters.append(player_input)
            for c in word:
                if c not in players_letters:
                    print(f'{player_name}, you guessed correctly! Letter {player_input} is in the word.')
                    print(f'The category is: {category}')
                    print(hangman_pics(tries))
                    display_word(word, players_letters)
                    print(f'missed letters: {" ".join([c for c in players_letters if c not in list(word)])}')
                    print(f'missed words:  {" ".join([m for m in players_words if m not in list(word)])}')
                    game_won = False
                    break
                game_won = True
            if game_won:
                display_word(word, players_letters)
                print(f'{player_name}, congratulations! You are the champion! You guessed correctly: {word}!')
                break
        else:
            players_letters.append(player_input)
            tries -= 1
            print(f'Wrong, tries left: {tries}')
            print(hangman_pics(tries))
            print(f'The category is: {category}')
            display_word(word, players_letters)
            print(f'missed letters: {" ".join([c for c in players_letters if c not in list(word)])}')
            print(f'missed words:  {" ".join([m for m in players_words if m not in list(word)])}')
        if tries == 0:
            print(f'Bad luck! {player_name}, you lost, the correct word is: {word}')
            break


def play_again():
    while True:
        game(get_category_word())
        answer = input('Do you want to play again? ').upper()
        while answer not in ('Y', 'N', 'YES', 'NO'):
            print ('Give the valid response.')
            answer = input().upper()
        if answer == 'N' or answer == 'NO':
            print('Thank you for playing!')
            break

play_again()











