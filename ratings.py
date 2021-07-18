"""Restaurant rating lister."""

import random

def process_ratings():
    """Reads scores from file and resturns dictionary of {restaurant-name: score}."""

    filename = open("scores.txt")

    ratings = {}

    for line in filename:
        restaurant, rating = line.strip().split(":")
        ratings[restaurant] = int(rating)

    return ratings


def print_sorted_ratings(ratings):
    """Print restaurant and its corresponding rating in alphabetical order."""

    for restaurant, rating in sorted(ratings.items()):
        print(f'{restaurant} is rated at {rating}.')


def add_new_restaurant(ratings):
    """Prompt user to add a new restaurant and to rate the restaurant."""

    user_restaurant = input("Name a restaurant you'd like to rate: ")
    user_rating = int(input("What rating would you like to give this restaurant? "))
    while user_rating < 1 or user_rating > 5:
        user_rating = int(input("Your rating must be between 1 and 5. What rating would you like to give? "))

    ratings[user_restaurant] = user_rating

def get_action_choice():
    """Gives the user a choice of actions and returns the user's choice.

    Choice 1: See ratings
    Choice 2: Add a new restaurant and rating
    Choice 3: Quit
    """

    print()
    print("What would you like to do?")
    print("1. See ratings for all restaurants")
    print("2. Add a new restauarnt and rating")
    print("3. Update a random restaurant's rating")
    print("4. Quit")

    return int(input("> "))

def update_restaurant_rating(ratings):
    """Chooce a restaurant at random and allow user to update its rating."""


    restaurant_list = list(ratings.keys())
    restaurant = random.choice(restaurant_list)
    print(f"The random restaurant chosen is {restaurant}.")
    new_rating = (input(f"What new rating would you like to give {restaurant}? "))

    while new_rating.isdigit() == False:
        print("You must enter a number for the rating.")
        new_rating = (input(f"What new rating would you like to give {restaurant}? "))

    #update restaurant rating with the new rating
    ratings[restaurant] = new_rating

    print_sorted_ratings(ratings)


#read existing scores in from file
ratings = process_ratings()

#prompt the user for what action they would like to perform


while True:
    action = get_action_choice()

    if action == 1:
        print_sorted_ratings(ratings)

    elif action == 2:
        add_new_restaurant(ratings)

    elif action == 3:
        update_restaurant_rating(ratings)

    elif action == 4:
        print("Thank you and goodbye!")
        break

    else:
        print("Invalid input. Please try again.")
