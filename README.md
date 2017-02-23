# Twitter Puddle Problem
My solution to the [Twitter Puddle Problem](http://puzzles.bostonpython.com/puddle.html). Thanks to [BostonPython](http://puzzles.bostonpython.com/puddle.html) for providing this awesome puzzle.

Problem Description
----
Given a list of values, e.g., `[0,1,2,1,1,2,3]`, imagine that the magnitude of each value corresponds to the height of a 2D surface. Brown squares correspond to the surface, while white squares correspond to empty space.

![Small example with no puddle](/no_puddle.png?raw=true)

Now, using a list with 1000 elements, imagine a downpour of 2D rain, and the pools of water that would eventually come into place.

![example with piddle](/side_by_side.png?raw=true)

**Question** After sufficient rainfall such that all the puddles are completely full, how much water has pooled on the 2D surface? I.e., how much area does the water take up.

Solution
----
The solution lies in a simple realization. When viewed from the perspective of each *cell* of water, only those cells that have a wall on their left and right hand sides, will contain water in them. All cells that do not contain a wall on both their right and left hand sides will eventually drain out as there's nothing to keep the water in.
