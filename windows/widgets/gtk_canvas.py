import tkinter as tk
import sys
from typing import Union, Tuple

class GTkCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(borderwidth=0, highlightthickness=0, *args, **kwargs)

    def roundedRectangle(self, x, y, width, height, r=25, **kwargs):
        points = [x+r, y,
                x+r, y,
                x+width-r, y,
                x+width-r, y,
                x+width, y,
                x+width, y+r,
                x+width, y+r,
                x+width, y+height-r,
                x+width, y+height-r,
                x+width, y+height,
                x+width-r, y+height,
                x+width-r, y+height,
                x+r, y+height,
                x+r, y+height,
                x, y+height,
                x, y+height-r,
                x, y+height-r,
                x, y+r,
                x, y+r,
                x, y]
        self.create_polygon(points, **kwargs, smooth=True)
        self.create_oval(-5, -5, 5, 5, fill='black')

    @classmethod
    def init_font_character_mapping(cls):
        """ optimizations made for Windows 10, 11 only """

        radius_to_char_warped = {19: 'B', 18: 'B', 17: 'B', 16: 'B', 15: 'B', 14: 'B', 13: 'B', 12: 'B', 11: 'B',
                                 10: 'B',
                                 9: 'C', 8: 'D', 7: 'C', 6: 'E', 5: 'F', 4: 'G', 3: 'H', 2: 'H', 1: 'H', 0: 'A'}

        radius_to_char_fine_windows_10 = {19: 'A', 18: 'A', 17: 'B', 16: 'B', 15: 'B', 14: 'B', 13: 'C', 12: 'C',
                                          11: 'C', 10: 'C',
                                          9: 'D', 8: 'D', 7: 'D', 6: 'C', 5: 'D', 4: 'G', 3: 'G', 2: 'H', 1: 'H',
                                          0: 'A'}

        radius_to_char_fine_windows_11 = {19: 'A', 18: 'A', 17: 'B', 16: 'B', 15: 'B', 14: 'B', 13: 'C', 12: 'C',
                                          11: 'D', 10: 'D',
                                          9: 'E', 8: 'F', 7: 'C', 6: 'I', 5: 'E', 4: 'G', 3: 'P', 2: 'R', 1: 'R',
                                          0: 'A'}

        radius_to_char_fine_linux = {19: 'A', 18: 'A', 17: 'B', 16: 'B', 15: 'B', 14: 'B', 13: 'F', 12: 'C',
                                          11: 'F', 10: 'C',
                                          9: 'D', 8: 'G', 7: 'D', 6: 'F', 5: 'D', 4: 'G', 3: 'M', 2: 'H', 1: 'H',
                                          0: 'A'}

        if sys.platform.startswith("win"):
            if sys.getwindowsversion().build > 20000:  # Windows 11
                cls.radius_to_char_fine = radius_to_char_fine_windows_11
            else:  # < Windows 11
                cls.radius_to_char_fine = radius_to_char_fine_windows_10
        elif sys.platform.startswith("linux"):  # Optimized on Kali Linux
            cls.radius_to_char_fine = radius_to_char_fine_linux
        else:
            cls.radius_to_char_fine = radius_to_char_fine_windows_10

    def _get_char_from_radius(self, radius: int) -> str:
        if radius >= 20:
            return "A"
        else:
            return self.radius_to_char_fine[radius]

    def create_aa_circle(self, x_pos: int, y_pos: int, radius: int, angle: int = 0, fill: str = "white",
                         tags: Union[str, Tuple[str, ...]] = "", anchor: str = tk.CENTER) -> int:
        # create a circle with a font element
        circle_1 = self.create_text(x_pos, y_pos, text=self._get_char_from_radius(radius), anchor=anchor, fill=fill,
                                    font=("CustomTkinter_shapes_font", -radius * 2), tags=tags, angle=angle)
        self.addtag_withtag("ctk_aa_circle_font_element", circle_1)
        self._aa_circle_canvas_ids.add(circle_1)

        return circle_1