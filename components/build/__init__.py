import os.path
import re

from tkinter.filedialog import asksaveasfilename

from components import Father
from components.merger import Merger
from components.sort import Sorter_Files

from PySide2.QtGui import QDragMoveEvent, QDragEnterEvent, QDropEvent
from PySide2.QtWidgets import QAbstractItemView
from PySide2.QtCore import Qt, QUrl


class Build(Father):
    def __init__(self, ui):
        super(Build, self).__init__(ui)
        self.merger = Merger(ui)
        self.sorter_files = Sorter_Files()
        self.file = ""
        
        # self.ui.addB.clicked.connect(lambda : self.ui.filesL
        #                              .addItems(askopenfilenames(filetypes=(
        #     ("Изображение", "*.jpg"),
        # ))))
        
        self.ui.delB.clicked.connect(self.delete)
        files = [('All Files', '*.pdf'),]
        self.ui.mergeB.clicked.connect(lambda: self.merger.merge(asksaveasfilename(
            filetypes=files,
            initialfile=self.file
        )))
        self.ui.sort.clicked.connect(self.sort)
        
        self.ui.name.currentTextChanged.connect(self.combo_setFile)
        
        self.ui.filesL.setDragDropMode(QAbstractItemView.DragDrop)
        self.ui.filesL.dragEnterEvent = self.dragEnterEvent_
        self.ui.filesL.dragMoveEvent = self.dragMoveEvent_
        self.ui.filesL.dropEvent = self.addFiles
    @staticmethod
    def dragEnterEvent_(event: QDragEnterEvent) -> None:
        if event.mimeData():
            event.accept()
        else:
            event.ignore()
    @staticmethod
    def dragMoveEvent_(event: QDragMoveEvent) -> None:
        try:
            if event.mimeData().hasUrls():
                event.setDropAction(Qt.DropAction)
                event.accept()
            else:
                event.ignore()
        except TypeError:
            pass
    
    def combo_setFile(self, num):
        a = re.search(r"\d{1,5}", os.path.basename(self.ui.filesL.item(0).text()))
        try:
            self.file = num + a.group(0)
        except:
            self.file = num
    
    def setFile(self):
        a = re.search(r"\d{1,5}", os.path.basename(self.ui.filesL.item(0).text()))
        try:
            self.file = self.ui.name.currentText() + a.group(0)
        except:
            self.file = self.ui.name.currentText()
    
    def addFiles(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                url: QUrl
                if url.isLocalFile():
                    a = str(url.toLocalFile())
                    if a.endswith(".jpg"):
                        links.append(str(url.toLocalFile()))
                else:
                    a = str(url.toLocalFile())
                    if a.endswith(".jpg"):
                        links.append(str(url.toString()))
            [self.ui.filesL.addItem(link) for link in links]
            a = re.search(r"\d{1,5}", os.path.basename(self.ui.filesL.item(0).text()))
            try:
                self.file = self.ui.name.currentText() + a.group(0)
            except:
                self.file = self.ui.name.currentText()
            # print(self.merger.file)
            # self.setFile()
    
    def sort(self):
        items = self.sorter_files.sort([self.ui.filesL.item(i).text() for i in range(self.ui.filesL.count())])
        if len(items) > 0:
            self.ui.filesL.clear()
            [self.ui.filesL.addItem(item) for item in items]
            a = re.search(r"\d{1,5}", os.path.basename(items[0]))
            try:
                self.file = self.ui.name.currentText() + a.group(0)
            except:
                self.file = self.ui.name.currentText()
        return
        # self.setFile()
    
    def delete(self):
        file = self.ui.filesL.selectedItems()
        
        if file:
            file = self.ui.filesL.indexFromItem(file[0]).row()
            self.ui.filesL.takeItem(file)