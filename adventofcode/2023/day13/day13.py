def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        above = above[:len(below)]
        below = below[:len(above)]

        print(len(above))
        print(len(below))
        
        if above == below:
            return r
        
    return 0


block = """
####....####.#.##
.....#..#.#...#.#
#......##..#.###.
...####.#.##.#...
###...##.#..#.###
###..###.#..#.###
...####.#.##.#...
.#..#......#####.
.#..#......#####.
...####.#.##.#...
###..###.#..#.###
###...##.#..#.###
...####.#.##.#...
"""

block.split("\n\n")
grid = block.splitlines()

row = find_mirror(grid)
print(row)