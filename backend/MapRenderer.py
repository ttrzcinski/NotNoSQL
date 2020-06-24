class MapRenderer:

    def render(self, max_x, max_y):
        line = ''
        for y in range(0, max_y):
            for x in range(0, max_x):
                line += '#'
            line += '\n'
        print(line)
