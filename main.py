def start_over():
  restart = input("Do you want to start over? (yes/no) ").lower()
  if restart == "yes":
      start_game()
  elif restart == "no":
      print("Thanks for playing! Goodbye.")
  else:
      print("Invalid choice. Please enter 'yes' or 'no'.")
      start_over()


def start_game():
  name = input("Please Enter Your Name: ")
  print("Welcome to the Hidden Leaf Village, " + name)

  answer = input(
      "As a young ninja from Hidden Leaf Village, you are setting out on a difficult path that requires you to make many decisions. Your choices will affect the course of the village and yourself as you go through the game. Naruto is a fictional world where one's path is determined by formidable jutsus, ninja clans, and epic battles. You now are leaving your home, will you go Left or Right? **Please note this is case sensitive** "
  )
  if answer == "Left":
      answer = input(
          "You're walking down the path and you see a boy with blonde hair. Do you want to catch up and speak to him? Yes or No? "
      )

      if answer == "Yes":
          print(
              "You catch up to the boy, tapping him on his shoulder before saying hello. He is startled as he turns around, flashing a bright smile at you once he registers your presence, 'Hey! We're gonna be late lets go!'"
          )
      elif answer == "No":
          print(
              "You continue walking down the path, ignoring the boy. The walk to school today will be long."
          )

  elif answer == "Right":
      answer = input(
          "You take a right and notice you forgot your books at home! You quickly run home to get them. You are late for school and end up getting in trouble"
      )
      start_over()

  else:
      print("Not a Valid Option. Please choose Left or Right.")
      start_game()


# Start the game
start_game()