# **HARRY POTTER WORDLE**

## <u>1. Introduction</u>
This project was about building a command-line application that allows users to manage a common dataset about a particular domain.
I decided to re-create the popular Wordle game, combined with the world famous Harry Potter books as a theme to the game. This game involves users trying to guess a five letter word, and in this case words related to Harry Potter, within a set number of attempts. The user will get clues as to whether the letters they have guessed are in the right position, or in the word but not the right position, or not in the word at all.
This command-line application game is designed for people who are keen Harry Potter fans and who also enjoy playing the famous Wordle game.
<hr>

## <u>2. User Stories</u>
As a user I want to easily understand the rules and play the five letter Harry Potter Wordle game without a high degree of difficulty in using the game. I want to be able to able to guess words related to Harry Potter and be given clues as to which letters I have entered are correct. I want to be able to check my answer at the end if I haven't got the correct word, and to be able to play again straight away or exit the game when I have finished.

### **End user goal:** 
I want to understand the rules of Harry Potter Wordle and to be able to get clues on the letters that I have guessed that will help me guess the correct word within the set number of attempts. 

### **Acceptance criteria:**
The welcome message will display instructions to the rules of the Harry Potter Wordle game.
As the user types 5 letter words, the clues will correctly show the user which letter is in the correct position, which letters are in the word but not in the correct position, and letters that are not in the word at all. Colors will help indicate which is which.
If the user does not guess correctly within the set number of attempts, it will display a message to the user with the answer and the options to play again or exit the game.
If the user guesses correctly, it will display a congratulations message to the user and the option to play again or exit the game.

### **Measurement of success:**
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

![landing-page](docs/screenshots/landing-page.png "Landing page")

### **Clues**
When the user types a 5 letter word, a message will display showing the user which word they just guessed, highlighted in blue. Below will be the clue, green letters representing the correct letter in the correct position, red letters representing correct letters in the word but in the wrong positions, and dashes representing letters that aren't in the word at all.
The user will be prompted to enter their next guess below.

### **Incorrect input from the user**
If the user does not enter a 5 letter word, they will be told to try again and to guess a 5 letter word. This will not count as one of the user's attempts.

### **Guessed correctly**
If the user guesses the correct word, they will be shown the word they guessed, the clue will include the correct answer lit up in green, and a congratulations message to the user showing how many guesses it took for the user to guess the correct answer. 
The user will then be given the option to either play again or exit the game.

![landing-page-levels](docs/screenshots/landing-page-levels.png "Landing page with levels")

### **User runs out of attempts**
If the user runs out of attempts, a message will display telling the user that they have run out of guesses and also what the correct answer was. 
The user will then be given the option to either play again or exit the game.

<hr>

## <u>4. Future features</u>

### **Display number of guesses as the user plays the game**
A feature that allows the user to know how many guesses they have remaining before they run out of guesses.

### **Username**
Allow the user to input a username at the beginning of the game so the display messages can refer to the user by name and speak to them directly.

### **Final score**
To add a scoring element so that when the user decides to exit the game, a final score will be displayed to show how many words they guessed correctly.

### **Display guessed letters not in word**
To show the user the letters that they have guessed already as they play the game, and which are not in the correct answer so the user knows which letters not to guess again.

<hr>

## <u>5. Color scheme</u>
I used the termcolor feature to add some basic color schemes to the game which helps add another dimension rather than the game being in black and white. I chose a cyan blue for the welcome message and instructions, and also to display the word that the user guessed.
I used a green color to display the letter that was guessed correctly in the correct position. Finally, I chose a red color to display a letter that is in the correct answer but not in the right position. I didn't want to add much more coloring to the game so as to keep it simple and easy to follow for the user.
<hr>

## <u>6. Lucidchart</u>
I used lucidchart to help me draw up the 

<hr>

## <u>7. Technology</u>
<b>HTML and CSS</b> were used to give the site it's core text and styling structures.

<b>JavaScript</b> was used to run the interactive parts of the game, including but not limited to the score updates, generating the random computer choice and the logic determining the win, lose and draw outcomes.

Two fonts were chosen from <b>Google Fonts</b> for the text styles of the site.

The icons for the player choices were taken from <b>Font Awesome</b>.

The audio files for the win and lose noises were taken from <b>Mixkit</b>.

<b>Gitpod</b> was the application chosen to develop the site.

The site has been deployed on <b>Github pages</b>. 
<hr>

## <u>8. Testing</u>

   ### **Code validation**
   HTML and CSS. Small errors were found and have been corrected since when the codes were put through the [W3C validator](https://validator.w3.org/) for HTML and [Jigsaw validator](https://jigsaw.w3.org/css-validator/) for CSS.

   The JavaScript code was put through the [JShint validator](https://jshint.com/) with minor errors such as unnecessary semicolons that have now been rectified.

   ### **Test cases**

   #### **Desktop**

   #### <i>Landing page</i>
   As the user is on the landing page, the user is shown the game title in the header, and two images underneath with the rules of the game. There is a message that informs the user to enter a username in a text box, where the pointer is focused on the text box already as the landing page loads. The user has to enter text into the text box before the options for the two difficulty levels are displayed on the page, Easy Spock and Hard Devil. 

   ![landing-page-levels](docs/screenshots/landing-page_level-selected.png "Landing page with level selected")

   #### <i>Game page</i>
   When the user gets to the game page, the username that was typed into the text box on the landing page will appear on the left side of the screen. In between the username and computer name, there is a scoreboard that indicates the scores for the player and the computer. Underneath the scoreboard is a "Ready?" message, the choices the user needs to make which are represented as icons, and another message to promt the user to make the first move to start the game. 
   When the user hovers over the icons, the icons will "pop" out and is highlighted with a blue border. When the user clicks on a choice, the game starts immediately and the score will automatically update and the results message will appear to show the user whether they have won that round or not. If the user has won a round, the user's score in the scoreboard will light up green. If the user has lost the round, the computer's score in the scoreboard will light up red. If it's a draw, it will only be indicated through the results message.
   If the user clicks on the game title in the header, this will refresh the page and take the user to the landing page to restart the game.

   ![hard-game-page](docs/screenshots/hard-game-page_win.png "Win result on hard game")
   ![hard-game-page](docs/screenshots/hard-game-page_lose.png "Lose result on hard game")
   ![hard-game-page](docs/screenshots/hard-game-page_draw.png "Draw result on hard game")
   ![hard-game-page](docs/screenshots/hard-game-page_icon-selected.png "Icon selected on hard game")

   #### **Mobile** 
   For a mobile width of 390px, the rules images are stacked on top of each other. The heading, images and text are all made smaller to fit the screen size better. In the game page, the icons, messages and names are all made smaller. The transformation of the icons when the user hovers over an icon has also been made smaller to minimise the movement of the icons from one row to another.

   ![landing-page-390px](docs/screenshots/mobile_landing-page.png "Landing page 390px")
   ![landing-page-390px](docs/screenshots/mobile_landing-page-levels.png "Landing page with levels 390px")
   ![easy-game-page-390px](docs/screenshots/mobile_game-page-easy.png "Easy game page 390px")
   ![hard-game-page-390px](docs/screenshots/mobile_game-page-hard.png "Hard game page 390px")

   ### **Fixed bugs**
   * A loadlevels function and a keydown event listener was added to JavaScript in order to prompt the user to enter a username in the text box before progressing to the game page. Before this, the user was able to click on a difficulty level straight away before typing anything into the text box.
   
   * When I was incorporating a second option for the difficulty level, I started by trying to run two functions to generate the computer choices for the Easy and Hard games. However, in the Easy game the computer was still generating the Hard choices of Love and Devil which should not have been part of the Easy game. To fix the bug, I created only one function to generate the computer choice, and created arrays for easy and hard choices in addition to an empty array option for controls. This helped to simplify the code and allowed the computer to generate choices for the Easy and Hard levels separately.

   * I had not included the playerChoice and computerChoice arguments within the win(), draw() and lose() functions that were nested within the game function. This resulted in both the player and computer scores updating at the same time whether the player won or lost. This was easily rectified by including the arguments within these functions.

   ### **Unfixed bugs**
   There are no known unfixed bugs.
   
   ### **Supported screens and browsers**
   The site is fully supported for large, medium and small screen widths from widths larger than 1480px to small screens of 390px. The images and texts have all been adjusted so that the user experience is unaffected for different screen sizes.
<hr>

## <u>9. Deployment</u>

   ### **Gitpod**
   The site was developed using Gitpod. In order to access the Gitpod workspace, follow the steps below:
   
   In Github repository, select the mark3lau/Spock_Game.
   Click on the green Gitpod button near the top of the repository page, this will open the Gitpod workspace.
   Inside the workspace, you can generate the web page of the Spock Game by typing into the terminal "python3 -m http.server".

   ### **Github**
   The site was deployed to Github pages. The steps to deploy are as follows:

   In Github repository, navigate to the Settings tab.
   In the section 'Source', select the Main option and click Save.
   Once Save has been clicked, the page will automatically refresh.
   Scroll to the Github pages section where the live link can be found.

   The live link can be found here - https://mark3lau.github.io/Spock_Game/

<hr>

## <u>10. Credits</u>

   ### **Content**
   The icons for the player choices in the game page were taken from [Font Awesome](https://fontawesome.com/).
   The fonts for the site were taken from [Google Fonts](https://fonts.google.com/).
   The code for the starry night effect background for the site was taken from Marsei who posted on 26th November 2015 on [Stack Overflow](https://stackoverflow.com/questions/33948011/creating-a-starry-background-in-css).
    
   ### **Media**
   The rules image for the Easy Spock level with the five options, Rock, Paper, Scissors, Lizard and Spock, was taken from the [Juice Bubble](https://juicebubble.co.za/product/rock-paper-scissors-lizard-spock/) website. 
   The rules image for the Hard Devil level with seven options including the Love and Devil options, was taken from a blog post by Maddish on [Zebra Tiger Fish](http://zebratigerfish.blogspot.com/2018/02/a-seven-pointed-expansion-rock-paper.html).
   The audio files for when the user wins and loses a game were taken from [Mixkit](https://mixkit.co/free-stock-video/audio/).