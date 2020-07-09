from lat_lng import Point
from PIL import Image

TILE_SIZE = 256

def stitch_tiles(min: Point, max: Point):
    tile_width = (max.x - min.x + 1)
    tile_height = (max.y - min.y + 1)
    total_width = tile_width * TILE_SIZE
    total_height = tile_height * TILE_SIZE
    result = Image.new(mode='RGB', size=(total_width, total_height))

    for x in range(tile_width):
        for y in range(tile_height):
            p = Point(x + min.x, y + min.y, min.zoom)
            image = Image.open(p.filename())

            result.paste(image, (x*TILE_SIZE, y*TILE_SIZE))

    result.save('tiles/result.png')