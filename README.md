KGB
===

KGB (Klaus Game Bot) is a remake of https://code.google.com/p/k-g-b/ and he is a bot written in python 2.7 that aims to be flexible, stable and performant game bot for Urban Terror. Skills, ratios and other 'statistical' features are voluntarily excluded from the developing in order to focus on performance and flexibility.

KGB is currently being maintained and developed.

KGB is ideal for a server that hosts multiple game instances because updates are managed by the server so that gameservers' admins don't need to worry about them. Their bot is always up-to-date and always get the latest bug fixes...


How to run KGB
====================

A basic example looks like::

    # yourfolder/run_bot.sh
    # ============
    #!/bin/bash
    SERVER_ADDRESS="your server ip"
    SERVER_PORT=your server port
    SERVER_RCON_PASSWD=$(echo -n "your rcon password"|base64)
    SERVER_LOG="path of your log"
    BOTROOT="bot directory"

    # ask to klaus@rkf-clan.org or visit http://rkf-clan.org for all API_* parematers
    API_URL="api url"
    API_USER="api user"
    API_KEY="api key"
    API_USER_RESOURCE_URI="api resource for user"
    API_SERVER_RESOURCE_URI="api resource for server"

    while true
    do
      echo -n "Starting Klaus BOT in 3 seconds..."
      echo ""
      echo ""
      echo "    /\___/\\"
      echo "    \ -.- /"
      echo "    \`-.^.-'"
      echo "      /\"\\"
      echo ""
      sleep 3
      python2.7 $BOTROOT/main.py -s $SERVER_ADDRESS -p $SERVER_PORT -r $SERVER_RCON_PASSWD -l $SERVER_LOG -u $API_URL -a $API_USER -k $API_KEY -e $API_USER_RESOURCE_URI -f $API_SERVER_RESOURCE_URI

      echo "$(date): Klaus BOT restarted." >> ./kgb_bot.log
    done
