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
parser.add_argument('--coords', help="The lat lngs to download in the form 'min_lat,min_lng,max_lat,max_lng'")
parser.add_argument('--zoom', type=int, default=14)
parser.add_argument('--output-file', default="output/result.png", help="The file to write the resulting image to.")
parser.add_argument('--source', type=str, default='linz', help="linz or osm, depending on the preferred source")

def main(min_coord, max_coord, zoom, output_file, source: str):
    min_coord = min_coord
    max_coord = max_coord

    min_point = latlng_to_slippy(min_coord, zoom)
    max_point = latlng_to_slippy(max_coord, zoom)

    download_tiles(min_point, max_point, source)
    stitch_tiles(min_point, max_point, output_file, source)

if __name__ == "__main__":
    options = parser.parse_args()

    coords = [float(x) for x in options.coords.split(',')]
    min_coord = LatLng(max(coords[0], coords[2]), min(coords[1], coords[3]))
    max_coord = LatLng(min(coords[0], coords[2]), max(coords[1], coords[3]))

    main(min_coord, max_coord, options.zoom, options.output_file, options.source)