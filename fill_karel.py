from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    # fill_the_row()
    # come_back_first_column()
    # ascend()
    while left_is_clear():
        # fill_row
        fill_the_row()
        # come_back_to_first_column
        come_back_first_column()
        # move up
        ascend()
  
    # # repeate this while last row whrere first column front is block
    # # move at the end of row
    fill_the_row()
    
def move_at_the_end():
    #precondition Karel facing north
    # post condition Karel facing East
    turn_right()
    while front_is_clear():
        move()
        
def fill_the_row():
    # pre condition Karel facing east
    # post condition: Karel facing east
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    
    
   
        
def come_back_first_column():
    # precondition Karel facing East
    # post condition, Karel facing north first column
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    
def ascend():
    #pre condition facing north
    #post condition face east
    move()
    turn_right()
    
    
def turn_around():
    turn_left()
    turn_left()
    
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
