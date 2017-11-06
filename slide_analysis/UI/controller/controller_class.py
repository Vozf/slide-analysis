from PyQt5.QtWidgets import QApplication
import os
import glob

from slide_analysis.UI.view import ImageViewer
from slide_analysis.UI.model import Model
from slide_analysis.UI.controller.constants import *
from slide_analysis.utils.functions import get_tile_from_coordinates


class Controller:
    def __init__(self, argv):
        self.app = QApplication(argv)
        self.model = Model()
        self.image_viewer = ImageViewer(self, self.model)
        self.app.installEventFilter(self.image_viewer)
        self.chosen_descriptor_idx = 1
        self.descriptor_params = (3, 2, 3)
        self.chosen_similarity_idx = 0
        self.similarity_params = None
        self.chosen_n = 10
        self.last_descriptor_database = None

    def run(self):
        self.image_viewer.show()
        return self.app.exec_()

    def get_imagepath(self):
        return self.image_viewer.image_helper.filepath

    def calculate_descriptors(self):
        imagepath = self.get_imagepath()
        descriptor_base = self.model.calculate_descriptors(self.chosen_descriptor_idx,
                                                           self.descriptor_params,
                                                           imagepath, DESCRIPTOR_DIRECTORY_PATH)
        self.last_descriptor_database = descriptor_base

    def get_descriptors(self):
        return self.model.descriptors

    def get_similarities(self):
        return self.model.similarities

    def find_similar(self):
        coordinates = self.image_viewer.user_selected_coordinates
        dimensions = self.image_viewer.user_selected_dimensions
        imagepath = self.get_imagepath()

        # todo remove when database select is added
        self.last_descriptor_database = self._select_last_modified_file_in_folder()

        desc_path = self.last_descriptor_database

        tile = get_tile_from_coordinates(imagepath, *coordinates, *dimensions)
        top_n = self.model.find_similar(desc_path, tile, self.chosen_n,
                                        self.chosen_similarity_idx, self.similarity_params)
        qts = list(map(lambda tup: self.image_viewer.image_helper.get_qt_from_coordinates(
            (tup[1].x, tup[1].y)), top_n))

        self.image_viewer.show_top_n(qts)

    @staticmethod
    def _select_last_modified_file_in_folder():
        files_path = os.path.join(DESCRIPTOR_DIRECTORY_PATH, '*')
        files = sorted(
            glob.iglob(files_path), key=os.path.getctime, reverse=True)
        return files[0]