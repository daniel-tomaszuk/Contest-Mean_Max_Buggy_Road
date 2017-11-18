import math


class Wreck:
    def __init__(self, ident, x_pos, y_pos, r):
        self.ident = ident
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.r = r


class Reaper:
    def __init__(self, ident, x_pos, y_pos, r, m):
        self.ident = ident
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.r = r
        self.m = m


def dist(x1, y1, x2, y2):
    # Euclidean metric for two points
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# game loop
while True:
    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    # units
    unit_count = int(input())

    my_reapers = []
    enemy_reapers = []
    wrecks = []
    # get inputs for the turn
    for i in range(unit_count):
        unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, \
        extra_2 = input().split()
        unit_id = int(unit_id)
        unit_type = int(unit_type)
        player = int(player)
        mass = float(mass)
        radius = int(radius)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        extra = int(extra)
        extra_2 = int(extra_2)

        if unit_type == 0:
            my_reapers.append(Reaper(unit_id, x, y, radius, mass))
        elif unit_type == 4:
            wrecks.append(Wreck(unit_id, x, y, radius))

    closest_wreck_dist = 6000
    closest_wreck_pos = [6000, 6000]
    for wr in wrecks:
        min_dist = dist(my_reapers[0].x_pos, my_reapers[0].y_pos,
                        wr.x_pos, wr.y_pos)
        if min_dist < closest_wreck_dist:
            min_dist = closest_wreck_dist
            closest_wreck_pos = [wr.x_pos, wr.y_pos]

    print(closest_wreck_pos[0], closest_wreck_pos[1], 300)
    print("WAIT")
    print("WAIT")




    # To debug: print("Debug messages...", file=sys.stderr)