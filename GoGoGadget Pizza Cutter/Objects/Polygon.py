"""
Last Edited By: Kevin Flathers
Date Last Edited: 05/17/2016

Author: Kevin Flathers
Date Created: 05/17/2017


Polygon shape class to interpret polygons from a TGML file
"""
from lxml import etree
from decimal import Decimal

class Polygon():
    """
    Polygon class to deal with polygons drawn on TGML
    """

    
    def __init__(self, tgml_shape):
        """
        Constructor

        param tgml_shape: <Polygon ... /> tag in string form
        """
        
        self.tgml_shape = tgml_shape
        self.min_x = self.min_x()
        self.max_x = self.max_x()
        self.min_y = self.min_y()
        self.max_y = self.max_y()
        self.height = self.height()
        self.width = self.width()
        self.left = self.min_x
        self.top = self.min_y
        self.new_points_string = self.new_points_to_string()

    
    def find_points(self):
        """
        Finds all the points in a TGML polygon

        return: points as a string
        """
        
        return self.tgml_shape.get('Points')


    def points_to_list(self):
        """
        Puts points string into a list

        return: list of x,y coordinates
        """
        
        pairs_string_list = self.find_points().split()
        new_list = []
        for item in pairs_string_list:
            add_item = item.split(',')
            x_y_list = []
            for sub_item in add_item:
                x_y_list.append(round(Decimal(float(sub_item)), 3))
            new_list.append(x_y_list)
        return new_list


    def all_x(self):
        """
        Finds all x coordinates

        return: list of x coordinates
        """
        x_list = []
        for item in self.points_to_list():
            x_list.append(item[0])
        return x_list


    def all_y(self):
        """
        Finds all y coordinates

        return: list of y coordinates
        """
        y_list = []
        for item in self.points_to_list():
            y_list.append(item[1])
        return y_list


    def min_x(self):
        """
        Returns min x coordinate
        """
        return min(self.all_x())


    def max_x(self):
        """
        Returns miax x coordinate
        """
        return max(self.all_x())


    def min_y(self):
        """
        Returns min y coordinate
        """
        return min(self.all_y())


    def max_y(self):
        """
        Returns max y coordinate
        """
        return max(self.all_y())


    def height(self):
        return self.max_y - self.min_y


    def width(self):
        return self.max_x - self.min_x


    def new_points(self):
        new_points_list = self.points_to_list()
        for item in enumerate(new_points_list):
            for sub_item in enumerate(item):
                if sub_item[0]:
                    new_points_list[item[0]][sub_item[0]] -= self.min_y
                else:
                    new_points_list[item[0]][sub_item[0]] -= self.min_x
        return new_points_list

    def new_points_to_string(self):
        new_points_string = ""
        for count, item in enumerate(self.new_points()):
            if count == self.new_points()[-1]:
                end_char = ""
            else:
                end_char = " "
            new_points_string += "{x},{y}{end_char}".format(x=item[0], y=item[1], end_char=end_char)
        if new_points_string[-1].isspace():
            new_points_string = new_points_string[:-1]
        return new_points_string


    def transform(self):
        self.tgml_shape.set('Points', self.new_points_string)
