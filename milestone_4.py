import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.target_word = random.choice(word_list)  # pick a random word
        self.word_guessed = ['_' for _ in self.target_word]  # underscores represent unguessed letters
        self.remaining_unique_letters = len(set(self.target_word))
        self.num_lives = num_lives
        self.guessed_letters = []

    def check_player_guess(self, guessed_letter):
        guessed_letter = guessed_letter.lower()
        if guessed_letter in self.target_word:
            print('Good guess!')
            for index, letter in enumerate(self.target_word):
                if letter == guessed_letter:
                    self.word_guessed[index] = guessed_letter
            self.remaining_unique_letters -= self.target_word.count(guessed_letter)
        else:
            print(f'Sorry, {guessed_letter} is not in the word.')
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.')

    def prompt_player_for_input(self):
        while True:
            player_input = input("Please enter a single letter: ")
            if len(player_input) != 1 or not player_input.isalpha():
                print("Invalid input. Please, enter a single alphabetical character.")
            elif player_input in self.guessed_letters:
                print("You already tried that letter!")
            else:
                self.check_player_guess(player_input)
                self.guessed_letters.append(player_input)
                break

# Call to test the method

if __name__ == "__main__":
     word_list = ['banana', 'apple', 'lychee', 'mango']
     game = Hangman(word_list)
     print("Word to guess:", game.target_word)
     print("Word guessed so far:", game.word_guessed)
     print("Number of unique letters:", game.remaining_unique_letters)
     print("Number of lives:", game.num_lives)
     print("Guessed letters:", game.guessed_letters)

     # Test the prompt_player_for_input method
     game.prompt_player_for_input()
     print("Updated word guessed so far:", game.word_guessed)
     print("Updated guessed letters:", game.guessed_letters)
     print("Number of lives remaining:", game.num_lives)
     print("Number of unique letters remaining:", game.remaining_unique_letters)
