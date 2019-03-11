# Message tracking
This bot was created for the sole purpose of tracking messages sent and received by a discord user. I wrote this in discord.js a while back and as of the first commit it's very bland and just a framework. As I continue porting, the whole functionality will be added. Functions: log / track messages, commands to parse the saved files, to package into a db, and to exclude certain users / message types.

# Usage
To use this bot all you have to do is clone the repo, and run it with your discord token. A quick google search will provide you a step-by-step guide on getting your token. If you want to use this constantly, I recommend hosting the bot on a VPS. Files will be saved by their channelid. As of right now any names with "special chars" that aren't supported by basic unicodes will be skipped over. The rest will be wrote as User#1111 >> Message.
