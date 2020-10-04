class MappingAdapter:

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        # Задаём новую размерность
        dim = [len(grid[0]), len(grid)]
        self.adaptee.set_dim(dim)

        lights = []
        obstacles = []

        for i in enumerate(grid):
            for x in enumerate(i[1]):
                if x[1] == 1:
                    lights.append([x[0], i[0]])
                elif x[1] == -1:
                    obstacles.append([x[0], i[0]])

        self.adaptee.lights = lights
        self.adaptee.obstacles = obstacles

        return self.adaptee.generate_lights()
