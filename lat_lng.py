from collections import namedtuple
import math

LatLng = namedtuple('LatLng', ['lat', 'lng'])

class Point:
    def __init__(self, x, y, zoom):
        self.x = x
        self.y = y
        self.zoom = zoom

    def get_url(self, format_url):
        return format_url % (self.zoom, self.x, self.y)

    def filename(self, source: str):
        return f'tiles/{source}/{self.zoom}_{self.x}_{self.y}.png'

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, zoom={self.zoom})'

def sec(num):
    return 1/math.cos(num)

def latlng_to_slippy(latlng: LatLng, zoom: int) -> Point:
    lat_rad = latlng.lat / 180 * math.pi

    n = 2 ** zoom
    x = math.floor(n * (latlng.lng + 180) / 360)
    y = math.floor(n * (1 - (math.log(math.tan(lat_rad) + sec(lat_rad)) / math.pi)) / 2)

    return Point(x, y, zoom)