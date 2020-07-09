import requests
from lat_lng import Point, LatLng
import os
from tile_iterator import iterate_tiles

output_folder = "tiles"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

url_base = "https://a.tile.opentopomap.org/%s/%s/%s.png"
def download_tile(point: Point):
    filename = point.filename(output_folder)
    if os.path.exists(filename):
        return

    url = point.get_url(url_base)
    response = requests.get(url)

    with open(point.filename(), 'wb') as f:
        f.write(response.content)

def download_tiles(min_coord: LatLng, max_coord: LatLng, zoom: int):
    iterator = iterate_tiles(min_coord, max_coord, zoom)

    for tile in iterator:
        download_tile(tile)

min_coord = LatLng(-33.508538, 151.192571)
max_coord = LatLng(-33.677381, 151.341555)
download_tiles(min_coord, max_coord, 14)