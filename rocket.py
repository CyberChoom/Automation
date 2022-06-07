class Rocket:

    def __init__(self, x, y):
        self.x = 0
        self.y = 0

    def move_right(self):
        self.x += 1
        # will increment x position by 1

    def move_left(self):
        self.x -= 1
        # will decrement x position by 1

    def move_up(self):
        self.y += 1
        # will increment y position by 1

    def move_down(self):
        self.y -= 1
        # will decrement y position by 1

    def current_position(self):
        print(f"The current position of the Rocket: x={rocket_ship.x}, y={rocket_ship.y}")
        # - will print the current position of the Rocket


rocket_ship = Rocket(0, 0)

# Example
rocket_ship.move_right()
rocket_ship.move_right()
rocket_ship.move_up()
rocket_ship.move_up()
rocket_ship.move_left()
rocket_ship.move_down()
rocket_ship.move_up()

rocket_ship.current_position()
