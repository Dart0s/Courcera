class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]

        self.map[5][7] = 1  # Источники света
        self.map[5][2] = -1  # Стены
        self.map[3][3] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)
        print(*self.lightmap, sep='\n')


class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        """Кортеж из 2 чисел
        dim[1] отвечает за высоту карты,
        dim[0] за ее ширину."""
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        """Устанавливает массив источников света с заданными координатами и просчитывает освещение.
        Положение элементов задается списком кортежей. В каждом элементе кортежа хранятся 2 значения: elem[0] --
        координата по ширине карты и elem[1] -- координата по высоте соответственно. """
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()



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

        print(lights)
        print(obstacles)
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        print(self.adaptee.lights)
        print(self.adaptee.obstacles)
        return self.adaptee.generate_lights()


if __name__ == '__main__':
    light = Light([1, 1])
    system = System()
    adapt = MappingAdapter(light)
    system.get_lightening(adapt)