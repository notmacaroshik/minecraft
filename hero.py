from const import *
class Hero():
    def __init__(self, pos, land):
        self.hero = loader.loadModel('smiley')
        self.land = land
        self.hero.reparentTo(land)
        self.hero.setScale(1)
        self.hero.setColor(ORANGE_05)
        self.hero.setPos(pos)
        self.camera_on = True
        self.mode = True
        self.step = 5
        self.camera_bind()
        self.accept_eventes()

    def camera_bind(self):
        base.disableMouse()
        base.camera.setH(270)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 0)
        self.camera_on = True

    def camera_up(self):
        pos = self.hero.getPos()
        base.enableMouse()
        base.camera.reparentTo(render)
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        self.camera_on = False

    def change_view(self):
        if self.camera_on:
            self.camera_up()
        else:
            self.camera_bind()
    
    def change_mode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True

    def tern_right(self):
        self.hero.setH((self.hero.getH() - self.step)%360)

    def tern_left(self):
        self.hero.setH((self.hero.getH() + self.step)%360)

    def chek_dir(self, angle):
        if 0 <= angle <= 20:
            return (0, -1)
        elif 20 < angle <= 65:
            return (1, -1)
        elif 65 < angle <= 110:
            return (1, 0)
        elif 110 < angle <= 155:
            return (1, 1)
        elif 155 < angle <= 200:
            return (0, 1)
        elif 200 < angle <= 245:
            return (-1, 1)
        elif 245 < angle <= 290:
            return (-1, 0)
        elif 290 < angle <= 335:
            return (-1, 1)
        else:
            return(0, -1)
    
    def look_at(self, angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())
        # d - дельта, смещение
        dx, dy = self.chek_dir(angle)
        # angle - угоЛ
        return x + dx, y + dy, z
    
    def accept_eventes(self):
        base.accept(VIEW, self.change_view)
        base.accept(TERN_RIGHT, self.tern_right)
        base.accept(TERN_LEFT, self.tern_left)
        base.accept(K_LEFT, self.come_left)
        base.accept(K_RIGHT, self.come_right)
        base.accept(K_FORWARD, self.come_forward)
        base.accept(K_BACK, self.come_back)
        base.accept(KEY_UP, self.up)
        base.accept(KEY_DOWN, self.down)
        base.accept(K_MODE, self.change_mode)
        

        
    
    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos) 
    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)
    def come_back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)
    def come_forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)
    def come_left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)
    def come_right(self):
        angle = (self.hero.getH() - 90) % 360
        self.move_to(angle)
    def up(self):
        self.hero.setZ(self.hero.getZ() + 1)            
    def down(self):
        self.hero.setZ(self.hero.getZ() - 1)
    def try_move(self, angle):
        pos = self.look_at(angle)
        print(pos)
        if self.land.isEmpty(pos):
            pos = self.land.find_highest_empty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
