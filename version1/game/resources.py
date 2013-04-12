import pyglet

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2


pyglet.resource.path = ['../resources']
pyglet.resource.reindex()


bullet_image = pyglet.resource.image("bullet.png")
player_image = pyglet.resource.image("player.png")
asteroid_image = pyglet.resource.image("asteroid.png")





center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)
