import argparse

def parse_lat_lng_pair(text: str) -> (float, float):
    parts = text.split(,)
    if len(parts) != 2:
        raise AssertionError(f'There should be exactly two parts')

    lat = float(parts[0])
    lng = float(parts[1])

    return lat, lng

parser = argparse.ArgumentParser(description="Download some map tiles")
parser.add_argument('--zoom', type=int, default=10)
parser.add_argument('--min')
parser.add_argument('--max')

options = parser.parse_args()