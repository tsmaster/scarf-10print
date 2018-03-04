#
# Voronoi Scarf Generator
# By Dave LeCompte tsmaster@gmail.com
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


from PIL import Image

im = Image.open("c64_low.gif").convert("1")

for row in range(4):
    for col in range(32):
        cols = []
        for x in range(8):
            bits = 0
            for y in range(8):
                px = im.getpixel((col * 8 + x, row * 8 + y))
                if px > 0:
                    px = 1
                bits += (1 << y) * (1 - px)
            cols.append(bits)
        print "  {0} : {1},".format(row*32 + col, cols)
