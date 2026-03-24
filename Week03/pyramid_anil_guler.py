def calculate_pyramid(blocks):
    height = 0
    while blocks >= height + 1:
        height += 1
        blocks -= height
    return height
