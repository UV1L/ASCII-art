import Gui as GuiCls
import sys
import argparse
import Drawer as DrCls

parser = argparse.ArgumentParser(description='This program converts your image'
                                             ' to ascii-art. '
                                             'Use -f *image file name* to'
                                             ' get an art')
parser.add_argument('-f', '--file',
                    type=str,
                    help='Type image name here',
                    dest='file')
parser.add_argument('-r', '--res',
                    type=int,
                    help='Type resolution. Default = 100',
                    default=100,
                    dest='w')
parser.add_argument('-s', '--save', type=str,
                    help='Type filename to save in',
                    dest='save_name')
parser.add_argument('-a', '--ansi',
                    action='store_true',
                    help='Enter this flag if you want to do ANSI',
                    dest='ansi_flag')
parser.add_argument('-i', '--image',
                    action='store_true',
                    help='Enter this flag if you want to save as image',
                    dest='img_flag')

parser.parse_args()


def main(arg, width):

    """
    this method runs the app
    """

    if arg == "" and width == 0:
        try:
            arg = str(parser.parse_args()).split("'")[1]
            width = parser.parse_args().w
            save_name = parser.parse_args().save_name
            ansi_flag = parser.parse_args().ansi_flag
            image_flag = parser.parse_args().img_flag
            if save_name is None:
                sys.stdout.write('!!!Type filename to save in!!!\n'
                                 'Use -s *filename*')
                sys.exit(1)

        except Exception as e:
            print(e)
            app = GuiCls.QApplication(sys.argv)
            GuiCls.Window()
            parser.parse_args()
            sys.exit(app.exec_())
    try:
        drawer = DrCls.Drawer(arg)
        res = drawer.resize_image(width)
        pixels = drawer.get_image_data()
        arr = drawer.draw_picture(pixels)
        img = drawer.to_ascii_art(arr, res[0])
        with open("%s.txt" % save_name, "w") as f:
            f.write(img)

        print('\n------------------------------------\n'
              'Now you can find your image on %s.txt!'
              '\n------------------------------------\n' % save_name)
        print(img + '\n')

        if ansi_flag:
            _tuple = (arr, res)
            ansi_img = drawer.to_ansi_art(_tuple)
            sys.stdout.write('Type filename to save ansi in: ')
            ansi_name = input()
            with open("%s.txt" % ansi_name, "w") as f:
                f.write(ansi_img)

            print('\n------------------------------------\n'
                  'Now you can find your ansi image on %s.txt!'
                  '\n------------------------------------\n' % ansi_name)

        if image_flag:
            sys.stdout.write('Type filename to save image in: ')
            image_name = input()
            result_image = drawer.get_img(save_name)
            result_image.save("%s.png" % image_name)

            print('\n------------------------------------\n'
                  'Now you can find your png image on %s.png!'
                  '\n------------------------------------\n' % image_name)

        return img

    except Exception as e:
        print(e)
        raise


if __name__ == '__main__':
    main("", 0)
