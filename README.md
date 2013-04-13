KGB
===

KGB (Klaus Game Bot) is a remake of irst kgb (https://code.google.com/p/k-g-b/) and he is a bot written in python 2.7 that aims to be flexible, stable and performant game bot for Urban Terror. Skills, ratios and other 'statistical' features are voluntarily excluded from the developing in order to focus on performance and flexibility.

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

For all API_* parameters you need to ask to klaus@rkf-clan.org or visit http://rkf-clan.org. 
You can have only one kgb installation and multiple run_bot.sh in separated folders for run kgb on multiple server on same machine. Of course, you'll need different API_* parameters for every server.


What's new
====================
The new KGB doesn't have a local database but communicates with RESTFUL API of the WebSite http://kgb-test.rkf-clan.org/. Clan Admins can go in administration area of WebSite and they can view (or change) all data recorded by kgb. They'll can be able to add admin, ban player, add alias and other useful stuff.

KGB WebSite will have a shared page where you can view permanent ban (with demo) of all clans that use kgb.