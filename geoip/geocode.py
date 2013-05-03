import pygeoip

class GeoCode:

    def __init__(self, database_path):
        self.geo_code = pygeoip.GeoIP(database_path)

    def getInfoFromIP(self, ip):
        return self.geo_code.record_by_addr(ip)