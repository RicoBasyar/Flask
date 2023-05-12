# import libraries
import random

# define rules
rules = {
    'do you have a cat': ['Yes, I have a cat.', 'No, I do not have a cat.'],
    'what is your cat\'s name': ['My cat\'s name is Mittens.', 'I do not have a cat.'],
    'what does your cat look like': ['Mittens is a black and white cat with green eyes.']
}

# define function to respond to user input
def respond(input_text):
    # check each rule for a match
    for key in rules.keys():
        if key in input_text:
            return random.choice(rules[key])
    return "I'm sorry, I don't understand."

# get user input and respond