#### 1. When the application is started, the player may choose to (1) Play a word game, (2) View statistics, or (3) Adjust the game settings.  

*Create class Settings() to track the game setting. The class will interact with GUI to implement its attributes*

*Create class Statistics() to track game stats.*

*Create class Board(), Rack(), Pool() to design the game.*


#### 2. When choosing to adjust the game settings, the player (1) may choose for the game to end after a certain maximum number of turns and (2) may adjust the number of and the letter points for each letter available in the pool of letters, starting with the default matching the English Scrabble distribution (12 E’s worth 1 point each, 4 D’s worth 2 points each, etc).

*Add attributes LetterScoreDistribution() to record score for each letter, MaxRounds to record maximum number of turns*


#### 3. When choosing to play a word game, a player will:

      1. Be shown a ‘board’ consisting of 4 letters drawn from the pool of available letters.
      
     -- add a BoardLetter() attribute to class Board()
      
      2. Be shown a ‘rack’ of 7 letters also drawn from the pool of available letters.

     -- add a RackLetter() attribute to Rack()

      3. On each turn, up to the maximum number of turns either:
              
              1. Enter a word made up of one or more letters from the player’s rack of letters, and one from the board.  The word must contain only valid letters and may not be repeated within a single game, but does not need to be checked against a dictionary (for simplicity, we will assume the player enters only real words that are spelled correctly)
                  
              2.  Swap 1-7 letters from their rack with letters from the pool of letters.  This is the only time letters are returned to the pool during a game.

     -- add a IfSwap() attribute to Rack so that we can tell if we will trigger AddScore function() to add score to TotalScore() attribute. Add a SwapLetters() method to Rack class.

      4. After a word is played, that letter on the board will be replaced by a different random letter from the word that was just played.  Example:  If ‘c’ is on the board, and ‘j’,’a’,’k’,’e’,’t’,’s’ are part of the rack, then the player may enter ‘jackets’ as a word, and the ‘c’ will be randomly replaced by the ‘j’,’a’,’k’,’e’,’t’, or ’s’ for the next turn on the board.

     -- add a ReplaceBoardLetter() method to replace the letter on the board.
      
      5. After a word is played, the tiles used from the rack are replaced from the pool of letters.
      
     -- add a RackAdd() and RackMinus() method to Rack class to replace letter. When RackAdd(), enable PoolMinus, vice versa.
      
      6. After a word is played, the player’s score will increase by the total number of points for the letters in the word, including the letter used from the board. (So ‘jackets’, if using default values, would score 20 points.)
      
     -- add a addScore() method to Rack class
      
      7. If the pool of letters is empty and the rack cannot be refilled, the player will score an additional 10 points.
      
     -- add a iFEmpty(Arraylist(char))) method to Class Pool(). Envoke AddScore() method in Rack class to add additional 10 points.
      
      8. When the maximum number of turns has been played, or the pool of letters is empty and the rack cannot be refilled, the game will end, and the final score will be displayed before returning to the first menu.

     -- add a addToStats() method to insert datetime utility and Totalscore attribute to database.
      
4. A player may choose to leave a game in progress at any time.  Selecting to play a game from the menu should then return to the game in progress.

*create a isolation pause() class to archive status of all other classes information*

5. When choosing to view statistics, the player may view (1) game score statistics, (2) letter statistics or (3) the word bank.

*Create Statistics() class which is a parent class of gameScore class, Letter Class and WordBank Class*

6. For game score statistics, the player will view the list of scores, in descending order by final game score, displaying:

    1. The final game score
    2. The number of turns in that game
    3. The average score per turn
  The player may select any of the game scores to view the settings for that game’s maximum number of turns, letter distribution, and letter points.

*Create GameScore() Class*

7. For letter statistics, the player will view the list of letters, in ascending order by number of times played, displaying:

   1. The total number of times that letter has been played in a word
   2. The total number of times that letter has been traded back into the pool
   3. The percentage of times that the letter is used in a word, out of the total number of times it has been drawn

*Create letter() Class*

8. For the word bank, the player will view the list of words used, starting from the most recently played, displaying:

    1. The word
    2. The number of times the word has been played

*Create WordBank() class*

9. The user interface must be intuitive and responsive.

*This part will be taken care of GUI*

10. The performance of the game should be such that students do not experience any considerable lag between their actions and the response of the application.

*Code will be optimized to eliminate latency issues*

11. For simplicity, you may assume there is a single system running the application.

*This part will not be considered in this section*


