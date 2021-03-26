import unittest
import Drawer as DrCls


class TestLogic(unittest.TestCase):

    def setUp(self):
        self.drawer = DrCls.Drawer("test.png")
        self.incorrect_asciiArt = "BBBBBBBBBBBBBBBBBBBBB" \
                                  "BBSSSSSSS#######&&&&&&" \
                                  "@@@@@@$$$$$$%%%%%%****" \
                                  "***!!!!!!!:::::::::::" \
                                  ".............."
        self.name = 'test'

    def test_new_size(self):
        actual_height = self.drawer.resize_image(120)[1]
        test_height = 66.0
        actual_width = self.drawer.resize_image(120)[0]
        test_width = 120

        self.assertEqual(test_height, actual_height)
        self.assertEqual(test_width, actual_width)

    def test_data_of_image_with_one_black_pixel(self):
        actual_data = self.drawer.get_image_data()
        actual_data_len = len(actual_data)
        test_data_len = 1

        actual_data_opacity = self.drawer.get_image_data()[0]
        test_data_opacity = 0

        self.assertEqual(test_data_len, actual_data_len)
        self.assertEqual(test_data_opacity, actual_data_opacity)

    def test_pixels_in_picture_with_one_black_pixel(self):
        actual_data = self.drawer.get_image_data()
        actual_pixels = self.drawer.draw_picture(actual_data)
        test_pixels = ' '

        self.assertEqual(test_pixels, actual_pixels)

    def test_ascii_string_with_one_black_pixel_and_empty_arr(self):
        res = self.drawer.resize_image(100)
        actual_string = self.drawer.to_ascii_art([], res[0])
        test_string = ''

        self.assertEqual(test_string, actual_string)

    def test_image_size_is_not_none_empty_lines(self):
        actual_image_size = self.drawer.get_img(self.name).size

        self.assertIsNotNone(actual_image_size)

    def test_ansi_art_with_incorrect_str(self):
        incorrect_ansiArt = "[41m[31m&[0m[41m" \
                            "[31m&[0m[41m[31m&[0m" \
                            "[41m[31m&[0m[41m" \
                            "[31m&[0m[41m[31m&[0m" \
                            "[41m[31m&[0m[41m" \
                            "[31m&[0m[41m[31m&[0m" \
                            "[41m[31m&[0m[41m" \
                            "[31m&[0m[41m[31m&[0m" \
                            "[41m[31m&[0m[41m" \
                            "[31m&[0m[41m[31m&[0m" \
                            "[41m[31m$[0m[41m" \
                            "[31m$[0m[41m[31m$[0m" \
                            "[41m[31m$[0m[41m" \
                            "[31m$[0m[41m[31m$[0m" \
                            "[41m[31m$[0m[41m" \
                            "[31m$[0m[41m[31m$[0m" \
                            "[41m[31m$[0m[41m" \
                            "[31m$[0m[41m[31m$[0m" \
                            "[41m[31m$[0m[41m" \
                            "[31m$[0m[43m[33m![0m" \
                            "[43m[33m:[0m[43m" \
                            "[33m:[0m[43m[33m:[0m" \
                            "[43m[33m:[0m[43m" \
                            "[33m:[0m[43m[33m:[0m" \
                            "[43m[33m:[0m[43m" \
                            "[33m:[0m[43m[33m:[0m" \
                            "[43m[33m:[0m[43m" \
                            "[33m:[0m[43m[33m:[0m" \
                            "[43m[33m:[0m[43m" \
                            "[33m:[0m[42m[32m&[0m" \
                            "[42m[32m&[0m[42m" \
                            "[32m&[0m[42m[32m&[0m" \
                            "[42m[32m&[0m[42m" \
                            "[32m&[0m[42m[32m&[0m" \
                            "[42m[32m&[0m[42m" \
                            "[32m&[0m[42m[32m&[0m" \
                            "[42m[32m&[0m[42m" \
                            "[32m&[0m[42m[32m&[0m" \
                            "[42m[32m&[0m[42m" \
                            "[32m&[0m[46m[36m%[0m" \
                            "[46m[36m%[0m[46m" \
                            "[36m%[0m[46m[36m%[0m" \
                            "[46m[36m%[0m[46m" \
                            "[36m%[0m[46m[36m%[0m" \
                            "[46m[36m%[0m[46m" \
                            "[36m%[0m[46m[36m%[0m" \
                            "[46m[36m%[0m[46m" \
                            "[36m%[0m[46m[36m%[0m" \
                            "[46m[36m%[0m[46m" \
                            "[36m%[0m[44m[34m#[0m" \
                            "[44m[34m#[0m[44m" \
                            "[34m#[0m[44m[34m#[0m" \
                            "[44m[34m#[0m[44m" \
                            "[34m#[0m[44m[34m#[0m" \
                            "[44m[34m#[0m[44m" \
                            "[34m#[0m[44m[34m#[0m" \
                            "[44m[34m#[0m[44m" \
                            "[34m#[0m[44m[34m#[0m" \
                            "[44m[34m#[0m[45m" \
                            "[35m&[0m[45m[35m&[0m" \
                            "[45m[35m&[0m[45m" \
                            "[35m&[0m[45m[35m&[0m" \
                            "[45m[35m&[0m[45m" \
                            "[35m&[0m[45m[35m&[0m" \
                            "[45m[35m&[0m[45m" \
                            "[35m&[0m[45m[35m&" \
                            "[0m[47m[37m:[0m"

        width = 120
        height = 1.2352941176470587
        res = ("MMMMMMMM..............xxxxooooodddddd"
               "MMMMMMMMMxxxxxxxxxxxxxxxxoooooooood"
               "xxxxxxxxxx.............oooooo"
               "MMMMMMMMMMMMMkkkkkk", (width, height))

        dr = DrCls.Drawer('test.png')
        ansi_img = dr.to_ansi_art(res)

        self.assertNotEqual(incorrect_ansiArt, ansi_img)


if __name__ == '__main__':
    unittest.main()
