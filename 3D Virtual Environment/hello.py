from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import AmbientLight, DirectionalLight, PointLight
from panda3d.core import NodePath
from panda3d.core import PandaNode
from pandac.PandaModules import WindowProperties
from direct.gui.OnscreenText import OnscreenText

class MyApp(ShowBase):
    xCoord = 0
    yCoord = 0
    textObject = None

    def __init__(self):
        ShowBase.__init__(self)

        self.accept('d', self.ChangeCameraPositionRight)
        self.accept('a', self.ChangeCameraPositionLeft)
        self.accept('s', self.ChangeCameraPositionBackward)
        self.accept('w', self.ChangeCameraPositionForward)
        self.taskMgr.add(self.UpdateCameraPosition)

        blank_node = PandaNode("my_blank_node")
        nodepath1 = NodePath(blank_node)
        nodepath1.reparentTo(self.render)

        blank_node2 = PandaNode("my_blank_node2")
        nodepath2 = NodePath(blank_node2)
        nodepath2.reparentTo(self.render)

        dlight = DirectionalLight('my dlight')

        self.scene = self.loader.loadModel("my-objects/plane.egg")
        self.scene.setPos(0,0,-0.5)
        self.scene.setScale(10, 10, 10)
        self.scene.reparentTo(nodepath2)

        self.sphObject = self.loader.loadModel("my-objects/sphere.egg")
        self.sphObject.setPos(0, 10, 0.1)
        self.sphObject.setScale(.6, .6, .6)
        self.sphObject.reparentTo(nodepath1)

        self.textObject = OnscreenText(text='x:0 y:0', pos=(-0.5, 0.02), scale=0.07)

        dlnp = nodepath1.attachNewNode(dlight)
        nodepath1.setLight(dlnp)


    def ChangeCameraPositionForward(self):
        self.yCoord += 5

    def ChangeCameraPositionBackward(self):
        self.yCoord -= 5     

    def ChangeCameraPositionRight(self):
        self.xCoord += 5          

    def ChangeCameraPositionLeft(self):
        self.xCoord -= 5           

    def UpdateCameraPosition(self, task):
        self.textObject.destroy()
        self.textObject = OnscreenText(text='x: ' + str(self.xCoord) + ' y:' + str(self.yCoord), pos=(-0.5, 0.02), scale=0.07)
        self.camera.setPos(self.xCoord, self.yCoord, 0)
        self.sphObject.setPos(self.xCoord,10+self.yCoord, 0.1)
        return task.cont



game = MyApp()
game.run()