#MISCELLANEOUS HELPERS

#to register mouse click position.
#will use the method when registering mouse clicks to assign spots with colors.
def get_clicked_pos(pos, rows, size): 
    gap = size // rows #finding the gap between each row. 
    x, y = pos #getting the coordinate position of the cursor respective to pygame display. 
    return x//gap, y//gap #normalizing the cursor coordinates to a matrix coordinate, represented by integers.