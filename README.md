# Pokémon Images
Tired of finding a good resource from which you can download all the images of our favourite fictional creatures Pokémon?
Or found a source but it is too large for your network to handle?
If yes, then you are at the right place as I have made a python script which enables you to extract the png images of all the Pokémon pretty seamlessly.
Just install this script, execute it and you are ready to go!

## Features
1. Can extract images of all Pokémon till any Pokémon upto Generation 8 (the latest generation!).
2. Images are the **official artwork of Pokémon** released by Nintendo.
3. Images have a transparent background.
4. Can stop the process at any time and continue later as the images are extracted one by one.
5. Does not require an excellent internet connection.

## Example Image
<img src="1.png"/>

## Prerequisite
Only Python 3 needs to be installed in your system. If you don't have it, no worry download it from [here](https://www.python.org/downloads/) (it is a small download!) and install it.

## Steps To Extract The Images
1. Create a folder/directory named "Pokémon Images".
2. Download the script and keep it in the directory containing the directory of "Pokémon Images" you just created.
3. Execute the script and wait as the images start appearing in the "Pokémon Images" directory.

## Termination
If at some point you wish to stop/pause the extraction, you are just a step away.
You need to open the stopFile.txt which is created when the extraction is in progress, change the text in it from "start" to "stop" and save it.
The next time you execute the script, extraction will start from where you left.

## Courtesy
1. All images are copyright of Nintendo.
2. The source of these images is https://gearoid.me/pokemon, a fantastic browser-based Pokémon guessing game.

**Few points to note:**
1. If you get disconnected, and an image is not correctly extracted, delete the incomplete image and restart the process.
2. Images will be named with the corresponding Pokémon number (as per the National Pokédex).
