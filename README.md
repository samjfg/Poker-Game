Plan
 - Create a functional deck which can be delt and ranomized properly, can probably do this using my own seed created with the time and maybe a hash/signature to make it unique and unpredictable. Even possibility of creating a way for a user to confirm that each card draw is actually from a simulated deck by confirming PGP key etc.

 - Once it can be dealt, the infrastructure for the game can be built up, so some GUI and way to set number of players and then deal the correct number of cards in the correct order. Then can get to the point where the game actually functions. Will also need to implement chip counting etc.

 plan for classes 
 players
 hands
 chips
 pot 
 deck
 cards

deck
- cards subclass of deck
player
 - hand subclass of player (or its own... ?) consising of card objects
 - chips 

 Kind of wondering what the purpose of all the classes is, should I have a specific class just for chips. Could even have a thing in the chips class to keep track of all of the chips and ensure that none are lost

 - Strategy, final part use some online reasearch with the stats of the game to calculate hand winning percentages etc and try to build a bot that makes use of these. Can potentially have differnt attributes that make them more risky for example and should be some sort of difficulty setting.