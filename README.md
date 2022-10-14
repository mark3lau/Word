# **HARRY POTTER WORDLE**

## <u>1. Introduction</u>
This project was about building a command-line application that allows users to manage a common dataset about a particular domain.
I decided to re-create the popular Wordle game, combined with the world famous Harry Potter books as a theme to the game. This game involves users trying to guess a five letter word, and in this case words related to Harry Potter, within a set number of attempts. The user will get clues as to whether the letters they have guessed are in the right position, or in the word but not the right position, or not in the word at all.
This command-line application game is designed for people who are keen Harry Potter fans and who also enjoy playing the famous Wordle game.
<hr>

## <u>2. User Stories</u>
As a user I want to easily understand the rules and play the five letter Harry Potter Wordle game without a high degree of difficulty in using the game. I want to be able to able to guess words related to Harry Potter and be given clues as to which letters I have entered are correct. I want to be able to check my answer at the end if I haven't got the correct word, and to be able to play again straight away or exit the game when I have finished.

* ### **End user goal** 
   I want to understand the rules of Harry Potter Wordle and to be able to get clues on the letters that I have guessed that will help me guess the correct word within the set number of attempts. 

* ### **Acceptance criteria**
   The welcome message will display instructions to the rules of the Harry Potter Wordle game.
As the user types 5 letter words, the clues will correctly show the user which letter is in the correct position, which letters are in the word but not in the correct position, and letters that are not in the word at all. Colors will help indicate which is which.
If the user does not guess correctly within the set number of attempts, it will display a message to the user with the answer and the options to play again or exit the game.
If the user guesses correctly, it will display a congratulations message to the user and the option to play again or exit the game.

* ### **Measurement of success**
   A clear set of instructions at the beginning of the game displayed to the user.
If the user types a word that is not 5 letters in length, a message will display to the user to type a 5 letter word.
Clearly color coded clues that display which letters are correct and in the right or wrong positions. 
If the user has guessed the word correctly within the set number of attempts, it will display a message to the user to show how many guesses it took the user to guess the correct answer.
If the user has not guessed the correct word, it will display the correct answer to the user and the options for them to either continue playing the game or exit.
Once the user has either guessed correctly or used up all their attempts, the ability for the user to easily continue playing the game or exit.

<hr>

## <u>3. Features</u>

### **Welcome message and instructions**
Firstly a colored welcome message to welcome the user to the game will be displayed. A short set of instructions will follow explaining the number of attempts the user has, which color indicates whether the word is in the correct position or if it's in the word but not in the correct position.
A short message will prompt the user to guess a 5 letter word related to Harry Potter, which is followed by an input message for the user to input their first guess.

![welcome-message](screenshots/welcome_page.png "Welcome message and instructions")

### **Clues**
When the user types a 5 letter word, a message will display showing the user which word they just guessed, highlighted in blue. Below will be the clue, green letters representing the correct letter in the correct position, red letters representing correct letters in the word but in the wrong positions, and dashes representing letters that aren't in the word at all.
The user will be prompted to enter their next guess below.

![clues](screenshots/clues.png "Clues")

### **Correct guess**
If the user guesses the correct word, they will be shown the word they guessed, the clue will include the correct answer lit up in green, and a congratulations message to the user showing how many guesses it took for the user to guess the correct answer. 
The user will then be given the option to either play again or exit the game.

![correct-guess](screenshots/correct_guess.png "Correct guess")

### **User runs out of attempts**
If the user runs out of attempts, a message will display telling the user that they have run out of guesses and also what the correct answer was. 
The user will then be given the option to either play again or exit the game.

![max-attempts](screenshots/max_attempts.png "User runs out of attempts")

<hr>

## <u>4. Future features</u>

* ### **Display number of guesses as the user plays the game**
   A feature that allows the user to know how many guesses they have remaining before they run out of guesses.

* ### **Username**
   Allow the user to input a username at the beginning of the game so the display messages can refer to the user by name and speak to them directly.

* ### **Final score**
   To add a scoring element so that when the user decides to exit the game, a final score will be displayed to show how many words they guessed correctly.

* ### **Display guessed letters not in word**
   To show the user the letters that they have guessed already as they play the game, and which are not in the correct answer so the user knows which letters not to guess again.

<hr>

## <u>5. Color scheme</u>
I used the termcolor feature to add some basic color schemes to the game which helps add another dimension rather than the game being in black and white. I chose a cyan blue for the welcome message and instructions, and also to display the word that the user guessed.
I used a green color to display the letter that was guessed correctly in the correct position. Finally, I chose a red color to display a letter that is in the correct answer but not in the right position. I didn't want to add much more coloring to the game so as to keep it simple and easy to follow for the user.

![color_theme_1](screenshots/color_theme_1.png "Cyan blue color theme")

![color_theme_2](screenshots/color_theme_2.png "Green and red color theme")

<hr>

## <u>6. Lucidchart</u>
I used lucidchart to help me draw up the structure of my game, from the beginning of the game with the welcome message and instructions through the various options the user could take, from displaying the various clues through to user guessing the word correctly or not, and how the application would tackle each possibility. 

![lucidchart](screenshots/harry_potter_wordle_lucidchart.jpeg "Lucidchart")

<hr>

## <u>7. Technology</u>
* <b>Python</b> was used to run this interactive command-line application.

* The <b>Termcolor</b> module was used to add basic color styles to text in the terminal.

* <b>Gitpod</b> was the application chosen to develop the site.

* The site has been deployed on <b>Heroku</b>. 

<hr>

## <u>8. Testing</u>

   ### **Code validation**
   The code has been put through the [Python checker](https://www.pythonchecker.com//) and returned minor errors. Most errors contained lines of code that were longer than 80 characters and unnecessary white spaces, which have all have now been rectified.

   ### **Test cases**

   * #### <u>Welcome message and instructions</u>
      The user is presented with a welcome message and instructions to the game. An input box message should show the user where to type their first guess.

   * #### <u>Clues</u>
      As the user types their 5 letter word, a display message will show the user what word they just typed, highlighted in cyan blue, followed on the next line by the clue. Green letters show letters that are in the correct position, red letters show letters that are in the answer but not in the correct position, and dashes show letters that are not in the answer.
      The user is then prompted to enter their next guess.

      ![clues](screenshots/clues.png "Clues")

   * #### <u>Incorrect input</u>
      If the user does not input a 5 letter word, a display message will tell the user that they have not typed a 5 letter word and to try again. This attempt will not count towards the total number of attempts.

      ![incorrect-input](screenshots/incorrect_input.png "Incorrect input")

   * #### <u>Correct guess</u>
      If the user guesses correctly, a display message will show the word they guessed, highlighted in cyan, followed by the correct answer highlighted in green as the clue. The following line will show a congratulations message and the number of guesses it took the user to guess the correct answer. The user will be given the option of playing again by pressing Enter, or typing 'mischief managed' to exit the game. 
      If they press Enter, the game will restart back to the beginning displaying the welcome message and instructions.
      If they decide to exit the game after typing 'mischief managed', a thank you for playing message will be displayed to the user.

      ![correct-guess](screenshots/correct_guess.png "Correct guess")

      ![play-again](screenshots/play_again.png "Play again")

   * #### <u>Incorrect guess and run out of attempts</u>
      If the user has guessed incorrectly and run out of attempts, a message will display telling the user that they have used up all their guesses, and what the correct answer was. The user will be given the option of playing again by pressing Enter, or typing 'mischief managed' to exit the game.

      ![max-attempts](screenshots/max_attempts.png "User runs out of attempts")

      ![exit-game](screenshots/exit_game.png "Exit game")

   * #### <u>Capitals changed to lower case</u>
      If the user uses capitals whilst typing their guesses, these will be converted to lower case so they match the values of the answer and a comparison can be made correctly. This also applies if the user wants to exit the game, the words 'mischief managed' are also changed to lower case so the user can properly exit the game even if they have typed in capitals.

      ![lower-case-1](screenshots/capitals_lower_case_1.png "Capitals changed to lower case in user guesses")

      ![lower-case-2](screenshots/capitals_lower_case_2.png "Capitals changed to lower case to exit game")

   ### **Fixed bugs**
   * The answer variable was originally generating a random word from the worksheet but displaying it as a list which was fixed by changing it to an array, this was added to the get_random_word function after the answer variable.
   
   * I had to make sure the user inputs were converted into lower cases, and also the answers being generated from the worksheet were also converted to lower cases so that the values matched. Some values were not matching previously therefore failing to make the comparisons to generate the clues.

   ### **Unfixed bugs**
   There are no known unfixed bugs.
   
<hr>

## <u>9. Deployment</u>

   ### **Gitpod**
   The site was developed using Gitpod. In order to access the Gitpod workspace, follow the steps below:
   
   In Github repository, select the mark3lau/harry_potter_wordle.
   Click on the green Gitpod button near the top of the repository page, this will open the Gitpod workspace.
   Inside the terminal, you can run the Harry Potter Wordle game by typing "python3 run.py".

   ### **Heroku**
   The site was deployed to Heroku. The steps to deploy are as follows:

   In the Heroku dashboard, click on the harry_potter_wordle app.
   Click on the 'Deploy' tab near the top of the page. 
   In the Deploy page, scroll down to the Manual deploy section. Choose the main branch to deploy, and click Deploy Branch. 
   Once the message 'Your app was successfully deployed' is displayed, click on the View button below. The app should now be running in a new tab.

<hr>

## <u>10. Credits</u>

   ### **Harry Potter words**
   The 5 letter words related to Harry Potter were taken from [Nerds Chalk](https://nerdschalk.com/5-letter-harry-potter-words-list-find-a-hint-for-harry-potter-wordle-easily/).