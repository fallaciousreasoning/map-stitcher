from lat_lng import Point, LatLng, latlng_to_slippy

def iterate_tiles(min_tile: Point, max_tile: Point):
    for x in range(min_tile.x, max_tile.x + 1):
        for y in range(min_tile.y, max_tile.y + 1):
            yield Point(x, y, min_tile.zoom)