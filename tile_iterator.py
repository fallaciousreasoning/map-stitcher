from lat_lng import Point, LatLng, latlng_to_slippy

def iterate_tiles(min: LatLng, max: LatLng, zoom: int):
    min_tile = latlng_to_slippy(min, zoom)
    max_tile = latlng_to_slippy(max, zoom)

    print(min_tile)
    print(max_tile)

    for x in range(min_tile.x, max_tile.x + 1):
        for y in range(min_tile.y, max_tile.y + 1):
            yield Point(x, y, zoom)