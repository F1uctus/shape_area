from by_points import get_area
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple, Optional


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def draw_plot(points: List[Tuple[int, int]]):
    if len(points) > 1:
        points = list(points)
        if len(points) > 2:
            points.append(points[0])
        max_x = max(p[0] for p in points)
        min_x = min(p[0] for p in points)
        max_y = max(p[1] for p in points)
        min_y = min(p[1] for p in points)
        max_size = max(
            max(abs(max_x), abs(min_x)),
            max(abs(max_y), abs(min_y))
        )

        _, ax = plt.subplots(figsize=(max_size, max_size))
        plt.xticks(np.arange(min_x, max_x + 1, 1))
        plt.yticks(np.arange(min_y, max_y + 1, 1))
        plt.title(f"Area is " + str(get_area(*points)))
        ax.set_aspect('equal')
        ax.plot([p[0] for p in points], [p[1] for p in points])
        ax.grid()
        plt.show()


def interactive_mode():
    points: List[Tuple[int, int]] = []
    last_point: Optional[Tuple[int, int]] = None
    while True:
        print('>', end=' ')
        args = [a.strip() for a in input().split()]
        command = args[0]
        args = args[1:]

        if command in ('a', 'add', 'append'):
            try:
                p_to_add = (int(args[0]), int(args[1]))
                last_point = p_to_add
                points.append(p_to_add)
            except ValueError:
                print('Format: x, y (e.g. "1, 2")')
                continue
        elif command in ('d', 'del', 'delete'):
            if len(args) == 0:
                points.remove(last_point)
            else:
                try:
                    p_to_delete = (int(args[0]), int(args[1]))
                    points.remove(p_to_delete)
                except ValueError:
                    print('Format: x, y (e.g. "1, 2")')
                    continue
        elif command in ('?', 'h', 'help'):
            print("a|add 1, 5  --  Adds a point to the plot")
            print("d|del 3, 7  --  Remove a point from the plot")
            continue
        elif command in ('exit', 'quit', 'x', 'q', 'done', ''):
            return
        else:
            print("Unknown command. Try '?'")
            continue
        draw_plot(points)


def single_mode(args):
    if len(args) < 6:
        print("Shapes are built by more than 2 points.")
        exit(1)

    if (len(args) - 1) % 2 != 0:
        print("Invalid coordinates count")
        exit(1)
    points = []
    pt_idx = 0
    try:
        for arg in args[1:]:
            coord = int(arg)
            points.append(coord)
            pt_idx += 1
    except ValueError:
        print(f"Invalid coordinate for point #{pt_idx}")
    points = list(chunks(points, 2))
    draw_plot(points)


def main():
    from sys import argv
    if any(arg in ('-i', '--interactive') for arg in argv):
        interactive_mode()
    else:
        single_mode(argv)


if __name__ == "__main__":
    main()
