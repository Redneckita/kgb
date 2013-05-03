K.G.B.
======

Klaus Game Bot (which its acronym is K.G.B.) is a rework of the first bot (https://code.google.com/p/k-g-b/) written in python 2.7 that aims to be a flexible, stable and performant game bot for Urban Terror 4.x servers. Skills, ratios and other 'statistical' features are voluntarily excluded from the developing in order to keep focus on performance and flexibility.

K.G.B. is the ideal solution for a server that hosts multiple game instances because updates are managed centrally so that gameservers' admins don't need to worry about them. Their bot is always up-to-date and always get the latest bug fixes...


How to run K.G.B.
====================

All the configuration parameters are kept within a single unix shell-script file, compiling that part is in charge of clan admins or game servers administrator.

A basic example looks like the following script:

    #!/bin/bash
    # ============
    # yourfolder/run_bot.sh
    SERVER_ADDRESS="Your server IP"
    # i.e. SERVER_ADDRESS="1.2.3.4"
    
    SERVER_PORT="Your server port"
    # i.e. SERVER_PORT="27960"
    
    SERVER_RCON_PASSWD="$(echo -n 'Your RCON password'|base64)"
    # i.e. SERVER_RCON_PASSWD="$(echo -n 'myl33trc0np4ssw0rd'|base64)"
   
    SERVER_LOG="Your server logfile absolute path"
    # i.e. SERVER_LOG="/opt/urbanterror41/.q3a/q3ut4/myurtserver.log"
    # (look for "seta g_log" line in server.cfg)
   
    BOTROOT="Main K.G.B. installation path"
    # i.e. BOTROOT="/opt/KlausGameBot"

    BOTLOGFILE="Game instance bot logfile"
    # i.e. BOTLOGFILE="./kgb_bot.log"

    # API parameters... ask on our K.G.B. forum at http://rkf-clan.org
    API_URL="API URL"
    API_USER="API User"
    API_KEY="API Key"

    # GEOIP Database
    GEOIP_DATABASE="Your GeoLiteCity.dat absolute path"

    while true
    do
      echo -n "Starting Klaus Game Bot in 3 seconds..."
      echo ""
      echo ""
      echo "    /\___/\\"
      echo "    \ -.- /"
      echo "    \`-.^.-'"
      echo "      /\"\\"
      echo ""
      sleep 3
      python2.7 $BOTROOT/main.py -s $SERVER_ADDRESS -p $SERVER_PORT -r $SERVER_RCON_PASSWD -l $SERVER_LOG -u $API_URL -a $API_USER -k $API_KEY -d $GEOIP_DATABASE

      echo "$(date): Klaus Game Bot restarted." >> $BOTLOGFILE
    done

You may ask on our K.G.B. forum at http://rkf-clan.org for all API_* parameters. 
K.G.B. is meant to be installed in one place, pointed by the environment variable BOTROOT, and have multiple 'run_bot.sh' scripts in separated folders allowing system administrators to manage multiple game servers with ease. Of course, you'll need unique API_* parameters for each server.


What's new
====================
The new K.G.B. doesn't rely on a local database but communicates via RESTFUL APIs hosted by WebSite http://kgb-test.rkf-clan.org/.
Clan Admins can manage every aspect of their instance via the administration panel of the WebSite. They will be able to add/remove admins, ban/unban players, add/remove aliases and many other useful stuff.

Via K.G.B. WebSite you can access a publicly shared page where you can view permanent bans (with demo, reason and banner) of all clans that use the bot.