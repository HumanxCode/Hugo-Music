<h1 align="center">Hugo Music 🎵</h1>

### A bot that can play music on Telegram Group and Channel Voice Chats
#### POWERED BY [MARSHALX TGCALLS](https://github.com/MarshalX/tgcalls)
### Available on telegram as [@HugoMusicBot](https://t.me/HugoMusicBot)

<h2> Features 🔥 </h2>

- Thumbnail Support
- Playlist Support
- Current playback support
- Showing track names when skipping
- Zero downtime, Fully Stable
- Deezer,Youtube & Saavn playback support
- Settings panel
- Control with buttons
- Userbot auto join
- Channel Music Play
- Keyboard selection support for youtube play


• Updates Channel : [Hugo Project](http://t.me/HugoProject)

• Support Group : [Hugo Support](http://t.me/HugoSupport)


```
Please fork this repository don't import code
Made with Python3
(C) @StevanKz

```

# Deploy
- [Heroku](#How-to-deploy)

### ⚔ Self-hosting (For Devs) 
```sh
# Install Git First (apt-get install git)
$ git clone https://github.com/StevanKz/Hugo-Music
$ cd HugoMusic
# Upgrade sources
# Install All Requirements 
$ pip3 install -U -r requirements.txt
# Fork This Repo and fill config.py vars with your own values.Then Start The Bot
$ python3 -m HugoMusic
```


### Mandatory Vars.

- Some Of The Mandatory Vars Are :
```- API_ID 
   - API_HASH
   - BOT_TOKEN
   - SUDO_USERS
   - SESSION
```
Get pyrogram (p)  `SESSION` from here:

[![Run on Repl.it](https://repl.it/badge/github/ChankitSaini/GenerateStringSession)](https://replit.com/@ChankitSaini/GenerateStringSession)





## Commands 🛠

• `/play <song name>` - play song you requested
• `/dplay <song name>` - play song you requested via deezer
• `/splay <song name>` - play song you requested via jio saavn
• `/playlist` - Show now playing list
• `/current` - Show now playing
• `/song <song name>` - download songs you want quickly
• `/search <query>` - search videos on youtube with details
• `/deezer <song name>` - download songs you want quickly via deezer
• `/saavn <song name>` - download songs you want quickly via saavn
• `/video <song name>` - download videos you want quickly

#### Admins only.
• `/player` - open music player settings panel
• `/pause` - pause song play
• `/resume` - resume song play
• `/skip` - play next song
• `/end` - stop music play
• `/userbotjoin` - invite assistant to your chat
• `/userbotleave` - remove assistant from your chat
• `/admincache` - Refresh admin list

### Commands for Channel Music Play 🛠
For linked group admins only:
• `/cplay <song name>` - play song you requested
• `/cplay <reply to link>` - play replied youtube link
• `/cplay <reply to audio>` - play replied file
• `/cdplay <song name>` - play song you requested via deezer
• `/csplay <song name>` - play song you requested via jio saavn
• `/cplaylist` - Show now playing list
• `/cccurrent` - Show now playing
• `/cplayer` - open music player settings panel
• `/cpause` - pause song play
• `/cresume` - resume song play
• `/cskip` - play next song
• `/cend` - stop music play
• `/userbotjoinchannel` - invite assistant to your chat
* channel is also can be used instead of c

If you donlt like to play in linked channel:
 1. Get your channel ID.
 2. Rename your group to: Channel Music: your_channel_id
 3. Add @HugoMusic as Channel admin with full perms
 4. add helper to channel
 5. Simply send commands in your group.

### Commands for Sudo Users ⚔️
• `/userbotleaveall` - remove assistant from all chats
• `/gcast <reply to message>` - globally brodcast replied message to all chats
• `/pmpermit [on/off]` - enable/disable pmpermit message

#### Pmpermit
• `.a` - approove someone to pm you
• `.da` - disapproove someone to pm you
+ Sudo Users can execute any command in any groups

#### Special Credits
- [StevanKz](http://github.com/StevanKz): Dev
- [Rojserbest](http://github.com/rojserbes): Callsmusic Developer
- [DaisyXMusic](http://github.com/TeamDaisyx/DaisyxMusic): Base code


### Made with ♥️ by [StevanKz](https://github.com/StevanKz)


## How to deploy



<details>
  <summary>Steps to deploy on Heroku !! </summary>

```
Fill in all the details, Deploy!
Now go to https://dashboard.heroku.com/apps/(app-name)/resources ( Replace (app-name) with your app name )
Turn on worker dyno (Don't worry It's free :D) & Webhook
Now send the bot /start, If it doesn't respond go to https://dashboard.heroku.com/apps/(app-name)/settings and remove webhook and port.
```

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/StevanKz/Hugo-Music)