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

def main(min_coord, max_coord, zoom, output_file):
    min_coord = min_coord
    max_coord = max_coord

    min_point = latlng_to_slippy(min_coord, zoom)
    max_point = latlng_to_slippy(max_coord, zoom)

    download_tiles(min_point, max_point)
    stitch_tiles(min_point, max_point, output_file)

if __name__ == "__main__":
    options = parser.parse_args()

    coords = [float(x) for x in options.coords.split(',')]
    min_coord = LatLng(coords[0], coords[1])
    max_coord = LatLng(coords[2], coords[3])

    main(min_coord, max_coord, options.zoom, options.output_file)