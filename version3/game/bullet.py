import pyglet
from game import physicalobject, resources

class Bullet(physicalobject.PhysicalObject):
    """Bullets fired by the player"""

    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__(resources.bullet_image, *args, **kwargs)
        pyglet.clock.schedule_once(self.die, 1.5)
        self.is_bullet = True

    def die(self, dt):
        self.dead = True
