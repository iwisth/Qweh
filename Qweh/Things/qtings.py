
import sys
import os
import shutil
from PyQt6 import QtCore, QtGui, QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc
from PyQt6.QtWidgets import QGraphicsItem, QGraphicsSceneDragDropEvent, QGraphicsSceneMouseEvent, QStyle
from PyQt6.QtCore import pyqtSlot, QEvent, Qt





####################################################################
####################################################################

def the_folders():
    pdir = os.getcwd()
    global import_dir, scenes_dir
    import_dir = os.path.join(pdir, 'ImportedAssets')
    scenes_dir = os.path.join(pdir, 'Scenes')
    dirs = [import_dir, scenes_dir]
    for dir in dirs:
        try:
            os.mkdir(dir)
        except OSError:
            print(os.path.basename(dir) + ' folder already exists! Nothing new.')
    return(import_dir, scenes_dir)

####################################################################

def import_files(self):
    files = qtw.QFileDialog.getOpenFileNames(
        parent=None,
        caption='Select file(s)',
        directory=os.getcwd())[0]
    print(files)
    for file in files:
        shutil.copy(file, import_dir)

####################################################################

def load_to_scene(self,scene):
    files = qtw.QFileDialog.getOpenFileNames(
        parent=self,
        caption='Select file(s)',
        directory=import_dir)[0]
    #print(files)
    for file in files:
        if file.endswith(('.png', '.jpg', '.jpeg')):
            image = qtg.QImage(file)
            pic = QGIPics(parent = None)
            pic.setPixmap(qtg.QPixmap.fromImage(image))
            scene.addItem(pic)
            

####################################################################

def display_scene_pop(self):
    self.pop = CreateScene()
    self.pop.display_pop()
    
####################################################################


def load_scene():
    scenefpath = qtw.QFileDialog.getOpenFileName(
        parent=None,
        caption='Select file(s)',
        directory=os.getcwd())[0]
    open(scenefpath, 'r')


####################################################################

def save_scene(self, scene):
    print("saving scene...")
    #identifies all imported assests in the scene
    #identify location of all different images
    #adds info to the scene file
    scene_imgs = scene.items
    print(scene_imgs)


####################################################################
    
    
def active_scene(scene_name):
    return(scene_name)


####################################################################
####################################################################


class CreateScene(qtw.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('seent it')
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)
        self.dalabel = qtw.QLabel('name your scene:')
        layout.addWidget(self.dalabel)
        self.scene_name = qtw.QLineEdit()
        layout.addWidget(self.scene_name)
        self.enter_scene = qtw.QPushButton('create new scene')
        self.enter_scene.clicked.connect(lambda: self.create_new_scene(self.scene_name.text()))
        self.enter_scene.clicked.connect(self.close)
        layout.addWidget(self.enter_scene)

    def display_pop(self):
        self.show()

    def create_new_scene(self, name):
        print(name)
        scenefpath = scenes_dir + '/' + name + '.txt'
        scenef = open(scenefpath, 'w')

####################################################################
        
class QGIPics(qtw.QGraphicsPixmapItem):
    def __init__(self, parent):
        super(QGIPics,self).__init__(parent)
        self.setFlag(qtw.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(qtw.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(qtw.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self.setFlag(qtw.QGraphicsItem.GraphicsItemFlag.ItemSendsScenePositionChanges)
    
    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if self.isSelected:
            self.setFocus()
        return super().mousePressEvent(event)

### fix this ###

    def dragMoveEvent(self, event: QGraphicsSceneDragDropEvent) -> None:
        if self.GraphicsItemChange.ItemPositionHasChanged:
            coords = [qtw.QGraphicsItem.pos(self).x(), qtw.QGraphicsItem.pos(self).y()]
            print("location is: " +str(coords))
        return super().dragMoveEvent(event)

### fix this ###

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if self.GraphicsItemChange.ItemPositionHasChanged:
            coords = [qtw.QGraphicsItem.pos(self).x(), qtw.QGraphicsItem.pos(self).y()]
            print("moved here: " + str(coords))
        return super().mouseReleaseEvent(event)
        


####################################################################

class GS(qtw.QGraphicsScene):

    def __init__(self, parent):

        super(GS, self).__init__(parent)
        self.setSceneRect(0, 0, 500, 400)

        self.focusItemChanged.connect(self.item_focus)
        

    @pyqtSlot("QGraphicsItem*", "QGraphicsItem*", Qt.FocusReason)
    def item_focus(self, new_item, old_item, reason):
        print("new focus: " + str(new_item))
        try:
            curr_coords = [qtw.QGraphicsItem.pos(new_item).x(), qtw.QGraphicsItem.pos(new_item).y()]
            print("current coordinates: " + str(curr_coords))
            #self.cBox = coordBox
            
            print("hath been doneth")
        except:
            print("nothing selected")
    


####################################################################

class coordBox(qtw.QGroupBox):
    def __init__(self, parent):
        super(coordBox,self).__init__(parent) 
        self.setTitle("coords")
        xLabel = qtw.QLabel("x position")
        self.x_edit = qtw.QLineEdit()
        self.x_edit.setMaximumWidth(50)
        yLabel = qtw.QLabel("y position")
        self.y_edit = qtw.QLineEdit()
        self.y_edit.setMaximumWidth(50)

        coord_layout = qtw.QFormLayout()
        coord_layout.addRow(xLabel, self.x_edit)
        coord_layout.addRow(yLabel, self.y_edit)
        coordBox.setLayout(self, coord_layout)

    def set_box(self, coords):
        print("we changing")
        self.x_edit.setText(coords[0])
        self.y_edit.setText(coords[1])


