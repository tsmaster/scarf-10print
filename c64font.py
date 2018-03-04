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


font = {
    0 : [0, 62, 127, 65, 77, 79, 46, 0],
    1 : [0, 32, 116, 84, 84, 124, 120, 0],
    2 : [0, 126, 126, 72, 72, 120, 48, 0],
    3 : [0, 56, 124, 68, 68, 68, 0, 0],
    4 : [0, 48, 120, 72, 72, 126, 126, 0],
    5 : [0, 56, 124, 84, 84, 92, 24, 0],
    6 : [0, 0, 8, 124, 126, 10, 10, 0],
    7 : [0, 152, 188, 164, 164, 252, 124, 0],
    8 : [0, 126, 126, 8, 8, 120, 112, 0],
    9 : [0, 0, 72, 122, 122, 64, 0, 0],
    10 : [0, 0, 128, 128, 128, 250, 122, 0],
    11 : [0, 126, 126, 16, 56, 104, 64, 0],
    12 : [0, 0, 66, 126, 126, 64, 0, 0],
    13 : [0, 124, 124, 24, 56, 28, 124, 120],
    14 : [0, 124, 124, 4, 4, 124, 120, 0],
    15 : [0, 56, 124, 68, 68, 124, 56, 0],
    16 : [0, 252, 252, 36, 36, 60, 24, 0],
    17 : [0, 24, 60, 36, 36, 252, 252, 0],
    18 : [0, 124, 124, 4, 4, 12, 8, 0],
    19 : [0, 72, 92, 84, 84, 116, 36, 0],
    20 : [0, 4, 4, 62, 126, 68, 68, 0],
    21 : [0, 60, 124, 64, 64, 124, 124, 0],
    22 : [0, 28, 60, 96, 96, 60, 28, 0],
    23 : [0, 28, 124, 112, 56, 112, 124, 28],
    24 : [0, 68, 108, 56, 56, 108, 68, 0],
    25 : [0, 156, 188, 160, 224, 124, 60, 0],
    26 : [0, 68, 100, 116, 92, 76, 68, 0],
    27 : [0, 0, 127, 127, 65, 65, 0, 0],
    28 : [64, 104, 124, 94, 73, 73, 34, 0],
    29 : [0, 0, 65, 65, 127, 127, 0, 0],
    30 : [0, 8, 12, 254, 254, 12, 8, 0],
    31 : [0, 24, 60, 126, 24, 24, 24, 24],
    32 : [0, 0, 0, 0, 0, 0, 0, 0],
    33 : [0, 0, 0, 79, 79, 0, 0, 0],
    34 : [0, 7, 7, 0, 0, 7, 7, 0],
    35 : [20, 127, 127, 20, 20, 127, 127, 20],
    36 : [0, 36, 46, 107, 107, 58, 18, 0],
    37 : [0, 99, 51, 24, 12, 102, 99, 0],
    38 : [0, 50, 127, 77, 77, 119, 114, 80],
    39 : [0, 0, 0, 4, 6, 3, 1, 0],
    40 : [0, 0, 28, 62, 99, 65, 0, 0],
    41 : [0, 0, 65, 99, 62, 28, 0, 0],
    42 : [8, 42, 62, 28, 28, 62, 42, 8],
    43 : [0, 8, 8, 62, 62, 8, 8, 0],
    44 : [0, 0, 128, 224, 96, 0, 0, 0],
    45 : [0, 8, 8, 8, 8, 8, 8, 0],
    46 : [0, 0, 0, 96, 96, 0, 0, 0],
    47 : [0, 64, 96, 48, 24, 12, 6, 2],
    48 : [0, 62, 127, 73, 69, 127, 62, 0],
    49 : [0, 64, 68, 127, 127, 64, 64, 0],
    50 : [0, 98, 115, 81, 73, 79, 70, 0],
    51 : [0, 34, 99, 73, 73, 127, 54, 0],
    52 : [0, 24, 24, 20, 22, 127, 127, 16],
    53 : [0, 39, 103, 69, 69, 125, 57, 0],
    54 : [0, 62, 127, 73, 73, 123, 50, 0],
    55 : [0, 3, 3, 121, 125, 7, 3, 0],
    56 : [0, 54, 127, 73, 73, 127, 54, 0],
    57 : [0, 38, 111, 73, 73, 127, 62, 0],
    58 : [0, 0, 0, 36, 36, 0, 0, 0],
    59 : [0, 0, 128, 228, 100, 0, 0, 0],
    60 : [0, 8, 28, 54, 99, 65, 65, 0],
    61 : [0, 20, 20, 20, 20, 20, 20, 0],
    62 : [0, 65, 65, 99, 54, 28, 8, 0],
    63 : [0, 2, 3, 81, 89, 15, 6, 0],
    64 : [24, 24, 24, 24, 24, 24, 24, 24],
    65 : [0, 124, 126, 11, 11, 126, 124, 0],
    66 : [0, 127, 127, 73, 73, 127, 54, 0],
    67 : [0, 62, 127, 65, 65, 99, 34, 0],
    68 : [0, 127, 127, 65, 99, 62, 28, 0],
    69 : [0, 127, 127, 73, 73, 65, 65, 0],
    70 : [0, 127, 127, 9, 9, 1, 1, 0],
    71 : [0, 62, 127, 65, 73, 123, 58, 0],
    72 : [0, 127, 127, 8, 8, 127, 127, 0],
    73 : [0, 0, 65, 127, 127, 65, 0, 0],
    74 : [0, 32, 96, 65, 127, 63, 1, 0],
    75 : [0, 127, 127, 28, 54, 99, 65, 0],
    76 : [0, 127, 127, 64, 64, 64, 64, 0],
    77 : [0, 127, 127, 6, 12, 6, 127, 127],
    78 : [0, 127, 127, 14, 28, 127, 127, 0],
    79 : [0, 62, 127, 65, 65, 127, 62, 0],
    80 : [0, 127, 127, 9, 9, 15, 6, 0],
    81 : [0, 30, 63, 33, 97, 127, 94, 0],
    82 : [0, 127, 127, 25, 57, 111, 70, 0],
    83 : [0, 38, 111, 73, 73, 123, 50, 0],
    84 : [0, 1, 1, 127, 127, 1, 1, 0],
    85 : [0, 63, 127, 64, 64, 127, 63, 0],
    86 : [0, 31, 63, 96, 96, 63, 31, 0],
    87 : [0, 127, 127, 48, 24, 48, 127, 127],
    88 : [0, 99, 119, 28, 28, 119, 99, 0],
    89 : [0, 7, 15, 120, 120, 15, 7, 0],
    90 : [0, 97, 113, 89, 77, 71, 67, 0],
    91 : [24, 24, 24, 255, 255, 24, 24, 24],
    92 : [51, 51, 204, 204, 0, 0, 0, 0],
    93 : [0, 0, 0, 255, 255, 0, 0, 0],
    94 : [204, 204, 51, 51, 204, 204, 51, 51],
    95 : [102, 204, 153, 51, 102, 204, 153, 51],
    96 : [0, 0, 0, 0, 0, 0, 0, 0],
    97 : [255, 255, 255, 255, 0, 0, 0, 0],
    98 : [240, 240, 240, 240, 240, 240, 240, 240],
    99 : [1, 1, 1, 1, 1, 1, 1, 1],
    100 : [128, 128, 128, 128, 128, 128, 128, 128],
    101 : [255, 255, 0, 0, 0, 0, 0, 0],
    102 : [51, 51, 204, 204, 51, 51, 204, 204],
    103 : [0, 0, 0, 0, 0, 0, 255, 255],
    104 : [48, 48, 192, 192, 48, 48, 192, 192],
    105 : [51, 153, 204, 102, 51, 153, 204, 102],
    106 : [0, 0, 0, 0, 0, 0, 255, 255],
    107 : [0, 0, 0, 255, 255, 24, 24, 24],
    108 : [0, 0, 0, 0, 240, 240, 240, 240],
    109 : [0, 0, 0, 31, 31, 24, 24, 24],
    110 : [24, 24, 24, 248, 248, 0, 0, 0],
    111 : [192, 192, 192, 192, 192, 192, 192, 192],
    112 : [0, 0, 0, 248, 248, 24, 24, 24],
    113 : [24, 24, 24, 31, 31, 24, 24, 24],
    114 : [24, 24, 24, 248, 248, 24, 24, 24],
    115 : [24, 24, 24, 255, 255, 0, 0, 0],
    116 : [255, 255, 0, 0, 0, 0, 0, 0],
    117 : [255, 255, 255, 0, 0, 0, 0, 0],
    118 : [0, 0, 0, 0, 0, 255, 255, 255],
    119 : [3, 3, 3, 3, 3, 3, 3, 3],
    120 : [7, 7, 7, 7, 7, 7, 7, 7],
    121 : [224, 224, 224, 224, 224, 224, 224, 224],
    122 : [0, 120, 120, 48, 24, 12, 6, 3],
    123 : [240, 240, 240, 240, 0, 0, 0, 0],
    124 : [0, 0, 0, 0, 15, 15, 15, 15],
    125 : [24, 24, 24, 31, 31, 0, 0, 0],
    126 : [15, 15, 15, 15, 0, 0, 0, 0],
    127 : [15, 15, 15, 15, 240, 240, 240, 240],

    205 : [3, 7, 14, 28, 56, 112, 224, 192],
    206 : [192, 224, 112, 56, 28, 14, 7, 3],
}
