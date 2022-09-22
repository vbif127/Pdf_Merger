import os.path
import re

from tkinter.messagebox import showwarning

from PIL import Image

from components import Father


def isint(obj):
    try:
        return isinstance(int(obj), int)
    except ValueError:
        return False

class Merger(Father):
    def __init__(self, ui):
        super(Merger, self).__init__(ui)
        self.file = ""
        self.file_type = ""
        
    def merge(self, path: str):
        files = [ self.ui.filesL.item(i).text() for i in range(self.ui.filesL.count())]
        
        if not path:
            return
        if not path.endswith("pdf"):
            path += ".pdf"
            
        if len(files) == 0:
            showwarning("Ошибка", "Недостаточно файлов для объединения!")
            return
        print([os.path.exists(f) for f in files])
        images = [
            Image.open(f)
            for f in files
        ]
        # try:
        #     filename = "_".join(re.split(r"[-,.,_,\,,\ ,+,\*]", os.path.basename(files[0]))[:-1:])
        #     print(filename, isint(filename.split("_")[-1]))
        #     if isint(filename.split("_")[-1]):
        #         a = filename.split("_")
        #         try:
        #             filename = "_".join([a[0], str(int(a[1])+1)])
        #         except IndexError:
        #             filename = "_".join(["P", str(int(a[0])+1)])
        #
        #     self.file = filename
        # except Exception as e:
        #     self.file = e
        self.file = os.path.basename(path)
        print(self.file)
        
        # path = os.path.dirname(path) + f"{self.file}.pdf"
        
        images[0].save(
            path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
        )
        self.ui.filesL.clear()
        if self.ui.deletableC.isChecked():
            [os.remove(file) for file in files]
        print(path)