# scarf-10print
python code to generate a pattern for a scarf memorializing the BASIC 10 PRINT "Maze" hack

## Requirements
- Python (tested with 2.7)
- PIL/Pillow

## To Run
```%python tenPrintScarf.py```

## Algorithm
First, I create a "character buffer", which is an array in memory for character information. I randomly populate this with 205 and 206 characters, simulating the output of the BASIC 10 PRINT code.

Then, I draw an "overscan" border around the edges of the scarf.

Next, I copy the BASIC code and some whitespace into the character buffer.

Finally, I render the character buffer into the scarf image.

## See Also
 - https://10print.org/
 - https://www.youtube.com/watch?v=m9joBLOZVEo
 - http://kofler.dot.at/c64/

