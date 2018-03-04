#
# 10 PRINT Scarf Generator
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
import random
import math

import c64font

X = 1200
Y = 100

CHAR_WIDTH = 8
CHAR_HEIGHT = 8

TEXT_ROWS = 11
TEXT_COLUMNS = 148

OVERSCAN_TOP = (Y - (TEXT_ROWS * CHAR_HEIGHT))/2
OVERSCAN_BOTTOM = Y - (TEXT_ROWS * CHAR_HEIGHT) - OVERSCAN_TOP

OVERSCAN_LEFT = (X - (TEXT_COLUMNS * CHAR_WIDTH)) / 2
OVERSCAN_RIGHT = X - (TEXT_COLUMNS * CHAR_WIDTH) - OVERSCAN_LEFT

# 7b76df
TEXT_COLOR = (0x7b, 0x76, 0xdf)
# 3c39a7
BG_COLOR = (0x3c, 0x39, 0xa7)

scarfImg = Image.new("RGB", (X, Y), BG_COLOR)

codeString = "10 PRINT CHR$(205.5+RND(1)); : GOTO 10"

charBuffer = [[random.choice([205,206]) for y in range(TEXT_ROWS)] for x in range(TEXT_COLUMNS)]
#charBuffer = [[205 for y in range(TEXT_ROWS)] for x in range(TEXT_COLUMNS)]

def drawOverscan():
    for x in range(X):
        for y in range(Y):
            if (x < OVERSCAN_LEFT or x >= X - OVERSCAN_RIGHT or
                y < OVERSCAN_BOTTOM or y >= Y - OVERSCAN_TOP):
                scarfImg.putpixel((x,y), TEXT_COLOR)

def drawCharAt(c, cx, cy):
    if not (c in c64font.font):
        fontEntry = c64font.font[32]
    else:
        fontEntry = c64font.font[c]

    for x in range(CHAR_WIDTH):
        for y in range(CHAR_HEIGHT):
            bit = 1 << y
            fontColumn = fontEntry[x]
            sx = OVERSCAN_LEFT + CHAR_WIDTH * cx + x
            sy = OVERSCAN_TOP + CHAR_HEIGHT * cy + y

            if bit & fontColumn:
                color = TEXT_COLOR
            else:
                color = BG_COLOR
            scarfImg.putpixel((sx, sy), color)

def drawCharBuffer():
    for x in range(TEXT_COLUMNS):
        for y in range(TEXT_ROWS):
            c = charBuffer[x][y]
            drawCharAt(c, x, y)

def drawStringCentered(s, row):
    sLen = len(s)
    startX = (TEXT_COLUMNS - sLen) / 2
    for si in range(sLen):
        c = s[si]
        x = startX + si
        print "placing {0} at x: {1} y: {2}".format(c, x, row)
        charBuffer[x][row] = ord(c)

drawOverscan()

r = TEXT_ROWS / 2
paddedCodeString = "  " + codeString + "  "
drawStringCentered(paddedCodeString, r)
whitespace = " " * len(paddedCodeString)
drawStringCentered(whitespace, r - 1)
drawStringCentered(whitespace, r + 1)
drawCharBuffer()

scarfImg.save("10PrintScarf.png")
#scarfImg.save("10PrintScarf.tiff")

