from PyQt5 import QtWidgets
from pyqtgraph.Qt import QtCore, QtGui
import numpy
import random

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from modules.MapWidget import *
from modules.Terrain.TerrainToolbar import *
from modules.PropertiesPanel import *
from modules.GeneratorsPanel import *

class TerrainEditorView(QMainWindow):
    """Main Window."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TT Map Generator')

        self._createWidgets()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self._createLayout())

    def _createWidgets(self):
        self.actionsPanel = TerrainToolbar()
        self.mapWidget = MapWidget()
        category = 'outdoor'
        self.propPanel = PropertiesPanel(category)
        self.generatorsPanel = GeneratorsPanel()

    def _createLayout(self):
        layout = QVBoxLayout()

        layout.addWidget(self.actionsPanel)
        mapLayout = QHBoxLayout()
        layout.addLayout(mapLayout)
        
        mapLayout.addWidget(self.mapWidget)
        
        rightLayout = QVBoxLayout()
        mapLayout.addLayout(rightLayout);
        rightLayout.addWidget(self.generatorsPanel)
        rightLayout.addWidget(self.propPanel)

        return layout

