############################################################################
#
# ######### #########    ###### #       # #       #
#     #         #      ##       #       #   #    #
#     #         #      #        #########     ###
#     #         #      ##       #       #      #
# #########     #        ###### #       #     #
#
############################################################################
#
#   You control Itchy! You tell him what to do!
#
#   Heres a list of things you can tell itchy to do:
#       itchy.wait(number of seconds)
#       itchy.faceLeft()
#       itchy.faceRight()
#       itchy.move(number of pixels)
#       itchy.turnLeft(number of degrees)
#       itchy.turnRight(number of degrees)
#       itchy.pointInDirection(direction)
#       itchy.pointTowards((x coordinate, y coordinate))
#       itchy.goto((x coordinate, y coordinate))
#       itchy.changeXBy(number of pixels)
#       itchy.changeYBy(number of pixels)
#       itchy.setXTo(number of pixels)
#       itchy.setYTo(number of pixels)


def click(itchy):
    itchy.faceLeft()
    itchy.wait(0.1)
    itchy.faceRight()
def left(itchy):
    itchy.faceLeft()
    itchy.move(100)
def right(itchy):
    itchy.faceRight()
    itchy.move(100)
def up(itchy):
    itchy.pointInDirection(0)
    itchy.move(100)
def down(itchy):
    itchy.pointInDirection(180)
    itchy.move(100)
def space(itchy):
    itchy.changeYBy(100)
    for _ in xrange(360/30):
        itchy.turnLeft(30)
    itchy.changeYBy(-100)
