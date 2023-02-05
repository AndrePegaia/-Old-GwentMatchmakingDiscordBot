# -Old-GwentMatchmakingDiscordBot
Discord bot used as a matchmaking and ladder system for custom games of Gwent: The Witcher Card Game

The bot was able to extract info from the the user's Gwent page as a Register/Validation feature.
After that, user was be able to queue up against other players in queues of different difficulties with simple commands.
When there were enough players in queue for a match to be found, the bot created a private text channel in the server and added both players. In this text channel there was information about both players and the instructions for the match.
Players were also able to report results and close match, enabling them to find another match.
Results and user info were stored in a local .xlsx file (but technically it could be changed to support it being saved in a SQL server)
There was also a command to create images of the current leaderboards, post them in a text channel and update them every X minutes.

Since the 2022 Discord bot update, this code is not working properly anymore and would need to be rebuilt partially to fit the new standards.  
