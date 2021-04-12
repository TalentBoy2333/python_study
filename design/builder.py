''' 建造者模式
'''

from abc import ABCMeta, abstractmethod 

class Player: 
    def __init__(self, face=None, body=None, arm=None, leg=None): 
        self.face = face 
        self.body = body 
        self.arm = arm 
        self.leg = leg

    def __str__(self): 
        return '{}, {}, {}, {}'.format(self.face, self.body, self.arm, self.leg)

class PlayerBuilder(metaclass=ABCMeta): 
    @abstractmethod
    def build_face(self): 
        pass

    @abstractmethod
    def build_body(self): 
        pass

    @abstractmethod
    def build_arm(self): 
        pass

    @abstractmethod
    def build_leg(self): 
        pass

class SexGirlBuilder(PlayerBuilder): 
    def __init__(self): 
        self.player = Player()

    def build_face(self): 
        self.player.face = 'beautiful face'

    def build_body(self):
        self.player.body = 'sexy body'
    
    def build_arm(self):
        self.player.arm = 'sexy arm'

    def build_leg(self):
        self.player.leg = 'long leg'
    
class MonsterBuilder(PlayerBuilder): 
    def __init__(self): 
        self.player = Player()

    def build_face(self): 
        self.player.face = 'monster face'

    def build_body(self):
        self.player.body = 'monster body'
    
    def build_arm(self):
        self.player.arm = 'monster arm'

    def build_leg(self):
        self.player.leg = 'monster leg'

class PlayerDirector:
    def build_player(self, builder): 
        builder.build_body() 
        builder.build_face() 
        builder.build_arm() 
        builder.build_leg() 
        return builder.player


# client
builder = SexGirlBuilder()
director = PlayerDirector() 
p = director.build_player(builder)
print(p)
