import pycurl, json, cStringIO, urllib

class Api:

    def __init__(self, username, api_key, api_url):

        self.api_url = api_url
        self.api_server_uri = '' # api_server_uri
        self.api_user_uri = '' # api_user_uri
        self.headers = [
            "Content-Type: application/json",
            "Authorization: ApiKey %s:%s" % (username, api_key),
        ]


    def get_server(self):

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, self.api_url + 'server/')
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.perform()
        server = json.loads(buf.getvalue())
        buf.close()
        if c.getinfo(pycurl.HTTP_CODE)==200:
            if server['meta']['total_count'] == 0:
                return False, None
            elif server['meta']['total_count'] == 1:
                return True, server['objects'][0]
            else:
                return False, None
        return False, None

    def get_server_configs(self):

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, self.api_url + 'server_config/')
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.perform()
        server_configs = json.loads(buf.getvalue())
        buf.close()
        if c.getinfo(pycurl.HTTP_CODE)==200:
            return True, server_configs['objects']
        return False, None

    def get_user(self):

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, self.api_url + 'user/')
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.perform()
        user = json.loads(buf.getvalue())
        buf.close()
        if c.getinfo(pycurl.HTTP_CODE)==200:
            if user['meta']['total_count'] == 0:
                return False, None
            elif user['meta']['total_count'] == 1:
                return True, user['objects'][0]
            else:
                return False, None
        return False, None

    def get_player(self, guid):

        if self.api_server_uri == '':
            server_found, server_obj = self.get_server()
            if not server_found:
                print 'server resource_uri not found! check your input parameters'
                return False, None
            else:
                self.api_server_uri = server_obj['resource_uri']

        if self.api_user_uri == '':
            user_found, user_obj = self.get_user()
            if not user_found:
                print 'user resource_uri not found! check you input parameters'
                return False, None
            else:
                self.api_user_uri = user_obj['resource_uri']        

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        parameters = {'guid': guid}
        c.setopt(pycurl.URL, self.api_url + 'player/?' + urllib.urlencode(parameters))
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.perform()
        players = json.loads(buf.getvalue())
        buf.close()
        if c.getinfo(pycurl.HTTP_CODE)==200:
            if players['meta']['total_count'] == 0:
                return False, None
            elif players['meta']['total_count'] == 1:
                return True, players['objects'][0]
            else:
                return False, None
        return False, None

    def update_player_level(self, guid, level):

        player_found = False
        player_obj = None
        player_found, player_obj = self.get_player(guid)

        player_obj['level'] =  level

        player_json = {"level": player_obj['level']}
        player_data = json.dumps(player_json) 

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, self.api_url + 'player/' + str(player_obj['id']) + '/')
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, player_data)
        c.setopt(pycurl.CUSTOMREQUEST, "PATCH")
        c.perform()
        buf.close()
        if c.getinfo(pycurl.HTTP_CODE) == 202:
            return self.get_player(guid)
        else:
            return False, None

        return player_found, player_obj

    def insert_player(self, player):

        player_json = {"name": player.name, "guid": player.guid, "level": 0, "server": self.api_server_uri, "owner": self.api_user_uri}
        player_data = json.dumps(player_json) 
        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, self.api_url + 'player/')
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, player_data)
        c.perform()
        buf.close()
        if c.getinfo(pycurl.HTTP_CODE) == 201:
            return self.get_player(player.guid)
        else:
            return False, None#, None

    def get_alias(self, guid, name):

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        parameters = {'player__guid': guid, 'alias': name}
        c.setopt(pycurl.URL, self.api_url + 'alias/?' + urllib.urlencode(parameters))
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.perform()
        aliases = json.loads(buf.getvalue())
        buf.close()
        if c.getinfo(pycurl.HTTP_CODE)==200:
            if aliases['meta']['total_count'] == 0:
                return False, None
            elif aliases['meta']['total_count'] == 1:
                return True, aliases['objects'][0]
            else:
                return True, None
        return True, None

    def get_aliases(self, guid):

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        print guid
        parameters = {'player__guid': guid}
        c.setopt(pycurl.URL, self.api_url + 'alias/?' + urllib.urlencode(parameters))
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.perform()
        aliases = json.loads(buf.getvalue())
        buf.close()
        if c.getinfo(pycurl.HTTP_CODE)==200:
            return True, aliases
        return False, None        

    def insert_alias(self, player, player_uri):

        alias_json = {"alias": player.name, "player": player_uri, "owner": self.api_user_uri}
        alias_data = json.dumps(alias_json) 

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, self.api_url + 'alias/')
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, alias_data)
        c.perform()
        buf.close()
        
        if c.getinfo(pycurl.HTTP_CODE) == 201:
            return self.get_alias(player.guid, player.name)
        else:
            return False, None

    def get_profile(self, guid, ip):

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        parameters = {'player__guid': guid, 'ip': ip}
        c.setopt(pycurl.URL, self.api_url + 'profile/?' + urllib.urlencode(parameters))
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.perform()
        profiles = json.loads(buf.getvalue())
        buf.close()
        if c.getinfo(pycurl.HTTP_CODE)==200:
            if profiles['meta']['total_count'] == 0:
                return False, None
            elif profiles['meta']['total_count'] == 1:
                return True, profiles['objects'][0]
            else:
                return True, None
        return True, None

    def insert_profile(self, player, player_uri):

        profile_json = {
            "ip": player.address.split(":")[0], 
            "rate": str(player.rate), 
            "racered": player.variables['racered'], 
            "raceblue": player.variables['raceblue'], 
            "cg_rgb": player.variables['cg_rgb'], 
            "sex": player.variables['sex'], 
            "weapmode": player.variables['weapmodes'], 
            "isp": '-', 
            "country": '-', 
            'gear': player.variables['gear'],
            "player": player_uri, 
            "owner": self.api_user_uri
        }
        profile_data = json.dumps(profile_json)

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, self.api_url + 'profile/')
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, profile_data)
        c.perform()
        buf.close()
        
        if c.getinfo(pycurl.HTTP_CODE) == 201:
            return self.get_profile(player.guid, player.address.split(":")[0])
        else:
            return False, None            

    def get_bans(self, guid):

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        parameters = {'player__guid': guid}
        c.setopt(pycurl.URL, self.api_url + 'ban/?' + urllib.urlencode(parameters))
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.perform()
        bans = json.loads(buf.getvalue())
        buf.close()
        if c.getinfo(pycurl.HTTP_CODE)==200:
            if bans['meta']['total_count'] == 0:
                return False, None
            else:
                return True, bans['objects']
        return True, None            

    def insert_ban(self, player, ban_reason, ban_minute, is_permanent):

        player_found, player_obj = self.get_player(player.guid)
        if player_found:

            profile_json = {
                "ip": player.address.split(":")[0], 
                'ban_reason': ban_reason,
                'ban_minute': ban_minute,
                'is_permanent': is_permanent,
                "player": player_obj['resource_uri'], 
                "owner": self.api_user_uri
            }

            profile_data = json.dumps(profile_json)

            buf = cStringIO.StringIO()
            c = pycurl.Curl()
            c.setopt(pycurl.URL, self.api_url + 'ban/')
            c.setopt(pycurl.HTTPHEADER, self.headers)
            c.setopt(pycurl.WRITEFUNCTION, buf.write)
            c.setopt(pycurl.POST, 1)
            c.setopt(pycurl.POSTFIELDS, profile_data)
            c.perform()
            buf.close()
            
            if c.getinfo(pycurl.HTTP_CODE) == 201:
                return True
            else:
                return False 
        else:
            return False    

    def delete_ban(self, guid):

        player_json = {"player__guid": guid}
        player_data = json.dumps(player_json) 

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, self.api_url + 'ban/')
        c.setopt(pycurl.HTTPHEADER, self.headers)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, player_data)
        c.setopt(pycurl.CUSTOMREQUEST, "DELETE")
        c.perform()
        buf.close()
        if c.getinfo(pycurl.HTTP_CODE) == 204:
            return True
        else:
            return False           