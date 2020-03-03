{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Let’s play Rock, Paper, Scissors? (yes/no) yes\n",
      "What's your choice?rock\n",
      "Tie!\n",
      "Play again?yes\n",
      "What's your choice?paper\n",
      "Tie!\n",
      "Play again?yes\n",
      "What's your choice?rock\n",
      "You Lose!\n"
     ]
    }
   ],
   "source": [
    "# Python Program for Rock Paper Scissors Game\n",
    "from random import *\n",
    "from sys import *   # used for the function 'exit()' to end the program\n",
    "def play():   # play() function\n",
    "    choice = input(\"What's your choice?\")\n",
    "    choices = {1 : 'rock', 2 : 'paper', 3 : 'scissors'}\n",
    "    c_choice = choices[randint(1,3)]    # randomly generaed choice\n",
    "    if choice == c_choice:   # choice- player's choice, c_choice- computer's choice\n",
    "        return print('Tie!')\n",
    "    if compare(choice,c_choice):\n",
    "        return print('You Win!')\n",
    "    else:\n",
    "        return print('You Lose!')\n",
    "def compare(pChoice,compChoice):    # compare() function\n",
    "    results = {('paper','rock') : True,\n",
    "                    ('paper','scissors') : False,\n",
    "                    ('rock','paper') : False,\n",
    "                    ('rock','scissors') : True,\n",
    "                    ('scissors','paper') : True,\n",
    "                    ('scissors','rock') : False}\n",
    "    return results[(pChoice,compChoice)]\n",
    "\n",
    "def game_play():   # game_play() function\n",
    "    begin = input(\"Let’s play Rock, Paper, Scissors? (yes/no) \")\n",
    "    while begin != \"yes\":\n",
    "        if begin == \"no\":\n",
    "            print(\"Game Over\")\n",
    "            sys.exit()\n",
    "        else:\n",
    "            print(\"Please try again\")\n",
    "            begin = input(\"Let’s play Rock, Paper, Scissors? (yes/no)\")\n",
    "    play()   # play() function called \n",
    "    while True:\n",
    "        begin = input('Play again?')\n",
    "        while begin != \"yes\":\n",
    "                if begin == \"no\":\n",
    "                    print(\"Game Over\")\n",
    "                    exit()\n",
    "                else:\n",
    "                    print(\"Please try again\")\n",
    "                    begin = input(\"Play again? \")\n",
    "        play()   # play() function called \n",
    "game_play()    # game_play() function called"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
