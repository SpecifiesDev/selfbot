# Message Clear
This bot is quite simple. It has 3 basic commands:
*adminclear
- Adminclear is straightforward. Run it in a server you have admin perms and it should purge the amount of messages you specify.

*clear 
- Run in a DM to messages in that DM.

*silentclear
- Silent clear works by typing silent {index}. Whole purpose of this command is to not notify the user. More explanation below.

# Usage
First you're going to want to grab your discord token. A simple google will give you a step-by-step guide on doing this. Then install the necessary discord.py depdencies, and run your bot. 

# Silent clear documentation.

*basics
Honestly I think it's interesting how I tackled this. I originally made the silentclear command because I had blocked someone and typing "clear" in the DM didn't work. It evolved to become much more useful, as I can use it to clear DMS without notifying the user. At the start of the program, every channel in your PMS is looped through and placed in a text file. Basic format of the output:
- (channelid) (position of id in created array) - Name of the person the DM is with

*using it
It's actually really simple. Open "clientids.txt" and find the number corresponding to the name you want to clear. Go to a private discord server or empty channel and type "silent (indexnumber.)" The bot will then silently delete in the range you specify.
