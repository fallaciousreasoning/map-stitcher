from lat_lng import Point
from PIL import Image
import os

TILE_SIZE = 256

def stitch_tiles(min: Point, max: Point, output_file, source: str):
    tile_width = (max.x - min.x + 1)
    tile_height = (max.y - min.y + 1)
    total_width = tile_width * TILE_SIZE
    total_height = tile_height * TILE_SIZE

    dirname = os.path.dirname(output_file)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    result = Image.new(mode='RGB', size=(total_width, total_height))

    for x in range(tile_width):
        for y in range(tile_height):
            p = Point(x + min.x, y + min.y, min.zoom)
            image = Image.open(p.filename(source))

            result.paste(image, (x*TILE_SIZE, y*TILE_SIZE))

    result.save(output_file)