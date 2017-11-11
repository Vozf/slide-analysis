import openslide
from PIL import ImageQt
from PyQt5.QtCore import QRect

from slide_analysis.constants.tile import BASE_TILE_WIDTH, BASE_TILE_HEIGHT
from slide_analysis.UI.view.constants import BASE_SCALE_FACTOR, SCALE_MULTIPLIER


class ImageHelper:
    def __init__(self, filename):
        self.filename = filename
        self.openslide_image = openslide.OpenSlide(filename)
        self.max_level = self.openslide_image.level_count - 1
        self.current_level = self.max_level
        self.level_dimensions = self.openslide_image.level_dimensions
        self.current_displayed_image_part_coordinates = (0, 0)
        self.current_image_part_coordinates = self.current_displayed_image_part_coordinates

        self.current_displayed_image_part_size = self.level_dimensions[self.current_level]
        self.current_image_part_size = self.current_displayed_image_part_size

        self.image_dimensions = self.level_dimensions[0]
        self.scale_factor = BASE_SCALE_FACTOR
        self.current_movement_step = (self.image_dimensions[0] // self.scale_factor,
                                      self.image_dimensions[1] // self.scale_factor)
        self.image = self.openslide_image.read_region(self.current_displayed_image_part_coordinates, self.current_level,
                                                      self.level_dimensions[self.current_level])
        self.image_slide = openslide.ImageSlide(self.image)
        self.print_status()

    def get_filepath(self):
        return self.filename

    def get_tile_coordinates(self, mouse_pos_point):
        actual_coordianates_x = int((mouse_pos_point.x()) * pow(2, self.current_level) + self.current_image_part_coordinates[0])
        actual_coordianates_y = int((mouse_pos_point.y()) * pow(2, self.current_level) + self.current_image_part_coordinates[1])
        print('User selected tile coordinates: ', actual_coordianates_x, actual_coordianates_y)
        actual_coordianates = (actual_coordianates_x, actual_coordianates_y)

        if actual_coordianates[0] >= 0 and actual_coordianates[1] >= 0:
            return actual_coordianates
        else:
            return 0, 0

    def get_qt_from_coordinates(self, tile_coordinates):
        return ImageQt.ImageQt(self.openslide_image.read_region(tile_coordinates, 0, (BASE_TILE_WIDTH, BASE_TILE_HEIGHT)))

    def __calculate_movement_step_coordinates(self):
        self.current_movement_step = (self.image_dimensions[0] // self.scale_factor,
                                      self.image_dimensions[1] // self.scale_factor)
        print('Current movement step:', self.current_movement_step)

    # def set_current_coordinates(self, current_coordianates):
    #     self.current_coordinates = current_coordianates

    def set_current_image_rect(self, view_rect):
        self.current_displayed_image_part_size = (int(view_rect.width()), int(view_rect.height()))
        self.current_displayed_image_part_coordinates = (
            self.current_image_part_coordinates[0] + view_rect.x() * pow(2, self.current_level),
            self.current_image_part_coordinates[1] + view_rect.y() * pow(2, self.current_level))

    def update_q_image(self, viewrect=None):
        if viewrect is not None:
            factor = min(viewrect[0] / self.current_displayed_image_part_size[0],
                         viewrect[1] / self.current_displayed_image_part_size[1])
            if factor > 1.25:
                self.move_to_next_image_level()
        self.image = self.openslide_image.read_region(self.current_displayed_image_part_coordinates, self.current_level,
                                                      self.current_displayed_image_part_size)
        self.print_status()
        return ImageQt.ImageQt(self.image)

    def update_image_rect(self):

        offset = (self.current_displayed_image_part_size[0] * pow(2, self.current_level) // 2,
                  self.current_displayed_image_part_size[1] * pow(2, self.current_level) // 2)

        print(offset)
        print('previous')
        print(self.current_displayed_image_part_coordinates)
        print(self.current_displayed_image_part_size)
        print(self.current_image_part_coordinates)
        print(self.current_image_part_size)

        self.current_image_part_coordinates = (
            int(self.current_displayed_image_part_coordinates[0] - offset[0]),
            int(self.current_displayed_image_part_coordinates[1] - offset[1]))

        if self.current_image_part_coordinates[0] < 0:
            self.current_image_part_coordinates = (0, self.current_image_part_coordinates[1])

        if self.current_image_part_coordinates[1] < 0:
            self.current_image_part_coordinates = (self.current_image_part_coordinates[0], 0)

        self.current_image_part_size = (
            self.current_displayed_image_part_size[0] * 2,
            self.current_displayed_image_part_size[1] * 2)

        current_image_size = self.get_current_image_size()
        if self.current_image_part_size[0] > current_image_size[0]:
            self.current_image_part_size = (current_image_size[0], self.current_image_part_size[1])

        if self.current_image_part_size[1] > current_image_size[1]:
            self.current_image_part_size = (self.current_image_part_size[0], current_image_size[1])

        print('current')
        print(self.current_displayed_image_part_coordinates)
        print(self.current_displayed_image_part_size)
        print(self.current_image_part_coordinates)
        print(self.current_image_part_size)
        print('\n')

    #
    # def change_image_properties(self):
    #     self.image = self.openslide_image.read_region(self.current_coordinates,
    #                                                   self.current_level, self.current_window_size)
    #     return ImageQt.ImageQt(self.image)

    def get_q_image(self):
        return ImageQt.ImageQt(self.image)

    def get_current_image(self):
        # QRect(self.get_current_displayed_image_rect())
        # rect_tuple = self.get_current_displayed_image_rect()
        # rect = QRect(rect_tuple[0], rect_tuple[1], rect_tuple[2], rect_tuple[3])
        # print(rect)
        return ImageQt.ImageQt(self.image)

    def get_current_image_size(self):
        return self.level_dimensions[self.current_level]

    def move_to_next_image_level(self):
        if self.current_level != 0:
            self.current_level -= 1
            self.current_displayed_image_part_size = (
                self.current_displayed_image_part_size[0] * 2, self.current_displayed_image_part_size[1] * 2)
            self.update_image_rect()
            self.image = self.openslide_image.read_region(self.current_image_part_coordinates,
                                                          self.current_level,
                                                          self.current_image_part_size)
            # self.current_image_part_coordinates = (
            #     self.current_image_part_coordinates[0] + self.current_displayed_image_part_coordinates[0],
            #     self.current_image_part_coordinates[1] + self.current_displayed_image_part_coordinates[1])
            # self.image = self.openslide_image.read_region(self.current_image_part_coordinates,
            #                                               self.current_level,
            #                                               self.current_displayed_image_part_size)

    def get_scale_factor(self):
        return max(self.current_image_part_size[0] / self.current_displayed_image_part_size[0],
                   self.current_image_part_size[1] / self.current_displayed_image_part_size[1])

    def get_current_displayed_image_rect(self):
        return ((self.current_displayed_image_part_coordinates[0] - self.current_image_part_coordinates[0]) // pow(2, self.current_level),
                (self.current_displayed_image_part_coordinates[1] - self.current_image_part_coordinates[1]) // pow(2, self.current_level),
                self.current_displayed_image_part_size[0],
                self.current_displayed_image_part_size[1])

    def move_to_prev_image_level(self):
        if self.current_level != self.openslide_image.level_count - 1:
            self.current_level += 1
            self.current_displayed_image_part_size = (
                self.current_displayed_image_part_size[0] // 2, self.current_displayed_image_part_size[1] // 2)
            self.update_image_rect()
            self.image = self.openslide_image.read_region(self.current_image_part_coordinates,
                                                          self.current_level,
                                                          self.current_image_part_size)

    # Zooming is just moving to next level of image
    def zoom_in(self):
        if self.current_level != 0:
            self.current_level -= 1
            self.scale_factor *= SCALE_MULTIPLIER
            self.__calculate_movement_step_coordinates()
        return self.update_q_image()

    def zoom_out(self):
        if self.current_level < self.openslide_image.level_count - 1:
            self.current_level += 1
            self.scale_factor //= SCALE_MULTIPLIER
            self.__calculate_movement_step_coordinates()
        return self.update_q_image()

    # def move_right(self):
    #     self.set_coordinates(self.current_coordinates[0] + self.current_movement_step[0],
    #                          self.current_coordinates[1])
    #
    # def move_left(self):
    #     self.set_coordinates(self.current_coordinates[0] - self.current_movement_step[0],
    #                          self.current_coordinates[1])
    #
    # def move_down(self):
    #     self.set_coordinates(self.current_coordinates[0],
    #                          self.current_coordinates[1] + self.current_movement_step[1])
    #
    # def move_up(self):
    #     self.set_coordinates(self.current_coordinates[0],
    #                          self.current_coordinates[1] - self.current_movement_step[1])

    def set_coordinates(self, x, y):
        to_set_x = self.__get_correct_coordinate(x, self.image_dimensions[0],
                                                 self.current_movement_step[1])
        to_set_y = self.__get_correct_coordinate(y, self.image_dimensions[1],
                                                 self.current_movement_step[1])
        self.current_displayed_image_part_coordinates = (to_set_x, to_set_y)
        self.print_status()

    @staticmethod
    def __get_correct_coordinate(coordinate, dimension, step):
        if coordinate > 0:
            if coordinate < dimension:
                return coordinate
            else:
                return dimension - step
        else:
            return 0

    def print_status(self):
        print('Current level:', self.current_level)
        print('Level dimensions:', self.current_displayed_image_part_size)
        print('Coordinates:', self.current_displayed_image_part_coordinates)
        print('\n')
