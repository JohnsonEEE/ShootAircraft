def is_collided(obj_a, obj_b):
    is_top_inside = obj_b.rect.top < obj_a.rect.top < obj_b.rect.bottom
    is_bottom_inside = obj_b.rect.top < obj_a.rect.bottom < obj_b.rect.bottom
    is_left_inside = obj_b.rect.left < obj_a.rect.left < obj_b.rect.right
    is_right_inside = obj_b.rect.left < obj_a.rect.right < obj_b.rect.right
    return (is_top_inside or is_bottom_inside) and (is_left_inside or is_right_inside)
