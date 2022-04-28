import requests
from lat_lng import Point, LatLng
import os
from tile_iterator import iterate_tiles

sources = {
    'linz': 'https://tiles-b.data-cdn.linz.govt.nz/services;key=d0772bed2204423f87157f7fb1223389/tiles/v4/layer=50767/EPSG:3857/%s/%s/%s.png',
    'osm': 'https://a.tile.opentopomap.org/%s/%s/%s.png'
}

for source in sources.keys():
    path = f'tiles/{source}'
    if not os.path.exists(path):
        os.makedirs(path)

def download_tile(point: Point, source: str):
    filename = point.filename(source)
    if os.path.exists(filename):
        return

    url = point.get_url(sources[source])
    response = requests.get(url)

    with open(point.filename(source), 'wb') as f:
        f.write(response.content)

def download_tiles(min_point: Point, max_point: Point, source: str):
    iterator = iterate_tiles(min_point, max_point)

    for tile in iterator:
        download_tile(tile, source)
