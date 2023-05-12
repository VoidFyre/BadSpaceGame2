def collide(obj1, obj2):
    offset_x = obj2.pos_x - obj1.pos_x
    offset_y = obj2.pos_y - obj1.pos_y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None