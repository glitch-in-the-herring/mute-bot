# Mutebot
A simple bot that mutes and unmutes everyone in a discord voice channel

## Installation
Make sure that you have `git` and `python3` installed to use this bot
* Clone the repository using `git clone https://github.com/glitch-in-the-herring/mute-bot.git`  
* `cd` into the directory
* Run `python3 -m pip install -U -r requirements.txt`
* Run `python3 main.py [-t TOKEN] [-p PREFIX]` to start using the bot  
* If you do not provide a prefix, the bot defaults to `$`. 

## Usage
To mute everyone, use `$mute`. To unmute everyone, use `$unmute`.  
To deafen everyone, use `$deafen`. To undeafen everyone use `$undeafen`.  
Make sure you are connected to a voice channel, and have the proper permissions in the voice channel.