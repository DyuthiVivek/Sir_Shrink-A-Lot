<h2> Zense HackNite '23 </h2>
<h2> Game Dev With Pygame </h2> 
<h2> Theme : Size is relative </h2> 
<h2> Sir Shrink-a-Lot </h2> 

## Team Membeers

1. Dyuthi Vivek 
2. Swetha Murali 


One dark, stormy night, Sir Shrink-a-Lot was riding back to the castle after a long battle through the forest and stumbled upon a lonely cottage, where he found a witch stirring a potion in a large cauldron. She offered him a steaming green potion. Once he drank it, he found himself shrinking rapidly. Enraged, he asked her what she had done to him and how to undo it. She simply said, “Follow the coins to your final goal, after which you will be whole again.” and handed him a scroll. On it was written 
<br>
<h3> Size is relative. It’s your courage that’s constant. </h3>

## How to play:
This is a multiplayer game. The objective is to reach the restoring diamond before the other player. You will be constantly shrinking. If you let your player disappear from the screen, you will lose a life. The game is lost once all 3 lives are lost. Collect coins to increase your player’s size.

Use the left, right and up arrow keys to control your player.

## Demo Video
https://drive.google.com/file/d/1N9SRsSHnMGl8sLQooDen7O1XIL1Gwqvy/view?usp=sharing


## Installation and Running:
1. Module requirements: pygame, os, sys, pickle, socket, _thread
2. Clone / download the github repository - https://github.com/DyuthiVivek/Hacknite_final
3. Path - set path to your working directory in line 10 of client.py and and line 6 of player.py
4. Install the above mentioned modules
5. Find the server’s IP address and add it in line 9 of network.py and line 8 of server.py.
6. To play the game, first run server.py (only once, in the system whose IP address was added). 
7. Now you can run client.py from two different systems. But both the systems need to be connected to the same network.

## Technologies used
Socket programming for multiplayer mode
Modules mentioned above

## Challenges faced
1. Collision detection: At times collisions with the platforms were not detected. We solved this issue but our solution caused some glitching when moving on the platform.
2. Sprite shrinking: We had trouble with the shrinking ratio but were able to fix it with the help of the mentors. When the player doesn’t move the sprite, it seems to crop the image instead of shrinking it to scale. We weren’t sure how to fix this.
3. Multiplayer start screen: The game now starts for the first player before the second player joins. We wanted to wait for the second player to join before starting the game but didn’t implement this due to the time constraint.





