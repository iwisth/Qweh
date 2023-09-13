import sys
import os
import shutil
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc
from PyQt6.QtWidgets import QStyle
from PyQt6.QtCore import QEvent, Qt

from Things import qtings




####################################################################


class Wimdo(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("hewwo")
        main_layout = qtw.QVBoxLayout()


        layout_imports = qtw.QVBoxLayout()
        row_layout_imports = qtw.QHBoxLayout()
        
        self.im_dir = qtg.QFileSystemModel()
        self.im_dir.setRootPath(qtc.QDir.currentPath())
        self.im_tree =  qtw.QTreeView()
        self.im_tree.setModel(self.im_dir)
        self.im_tree.setRootIndex(self.im_dir.index(qtings.import_dir))

        load_assets_file = qtw.QPushButton('import from puter')
        load_assets_file.clicked.connect(lambda: qtings.import_files(self))


        row_layout_imports.addWidget(load_assets_file)

       
        layout_imports.addLayout(row_layout_imports)
        layout_imports.addWidget(self.im_tree)


        
        layout_scenes = qtw.QVBoxLayout()
        row_layout_scenes = qtw.QHBoxLayout()

        row_layout_scenes_1 = qtw.QHBoxLayout()
        new_scene = qtw. QPushButton('new scene')
        load_scene = qtw.QPushButton('load scene')
        im_to_scene = qtw.QPushButton('import to scene')
        im_to_scene.clicked.connect(lambda: qtings.load_to_scene(self, displayed_scene))
        new_scene.clicked.connect(lambda: qtings.display_scene_pop(self))
        run = qtw.QPushButton('RUN')
        save_scene = qtw.QPushButton('save scene')
        row_layout_scenes.addWidget(new_scene)
        row_layout_scenes.addWidget(load_scene)
        row_layout_scenes.addWidget(im_to_scene)
        row_layout_scenes.addWidget(save_scene)
        
        layout_scenes.addLayout(row_layout_scenes)
        layout_scenes.addWidget(run)

        row_layout_scenes_2 = qtw.QHBoxLayout()
        coords = qtings.coordBox(parent = None)
        displayed_scene = qtings.GS(parent = None)
        displayed_scene.addText('make a scene!')

        view = qtw.QGraphicsView(displayed_scene, parent=None)

        row_layout_scenes_2.addWidget(coords)
        row_layout_scenes_2.addWidget(view)
        

        layout_scenes.addLayout(row_layout_scenes_2)

        main_layout.addLayout(layout_imports)
        main_layout.addLayout(layout_scenes)

        widget = qtw.QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        self.show()



####################################################################



####################################################################
####################################################################

if __name__ == '__main__':
    qtings.the_folders()
    app = qtw.QApplication(sys.argv)
    mw = Wimdo()
    app.exec()
