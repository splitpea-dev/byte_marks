import sys
from PIL import Image


# write a single tile (8 bytes)
def write_tile(im, of, tile_x, tile_y):
        start_x = tile_x * 8
        start_y = tile_y * 8
        for y in range(8):
                b = 0
                for x in range(8):
                        b = b << 1
                        p = im.getpixel((x + start_x, y + start_y))
                        if (p > 127):
                                b = b | 1
                of.write(bytes([b]))


# try to open image file from argument 1
if len(sys.argv) > 1:
        try:
                im = Image.open(sys.argv[1]).convert("L")
        except FileNotFoundError:
                print("The input file does not exist or is invalid.")
                exit()

# create binary output filename and open for writing bytes
outname = sys.argv[1].split('.')[0] + ".bin"
of = open(outname, "wb");

# write tile bytes
tile_rows = int(im.height / 8)
tile_cols = int(im.width / 8)
for tile_y in range(tile_rows):
        for tile_x in range(tile_cols):
                write_tile(im, of, tile_x, tile_y)

# clean up
im.close()
of.close()