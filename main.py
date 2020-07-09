import argparse
from lat_lng import Point, latlng_to_slippy, LatLng
from tile_downloader import download_tiles
from tile_stitcher import stitch_tiles

def parse_lat_lng_pair(text: str) -> (float, float):
    parts = text.split(',')
    if len(parts) != 2:
        raise AssertionError(f'There should be exactly two parts')

    lat = float(parts[0])
    lng = float(parts[1])

    return lat, lng

parser = argparse.ArgumentParser(description="Download some map tiles")
parser.add_argument('--zoom', type=int, default=10)
parser.add_argument('--min')
parser.add_argument('--max')

# options = parser.parse_args()

def main():
    min_coord = LatLng(-33.508538, 151.192571)
    max_coord = LatLng(-33.677381, 151.341555)
    zoom = 14

    min_point = latlng_to_slippy(min_coord, zoom)
    max_point = latlng_to_slippy(max_coord, zoom)

    download_tiles(min_point, max_point)
    stitch_tiles(min_point, max_point)

main()