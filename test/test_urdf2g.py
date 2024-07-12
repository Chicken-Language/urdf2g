from src.urdf2g import urdf2g

path = './test.txt'

urdf2g(path, is_file=True)
urdf2g(path, is_file=True)

urdf2g(path, "stdout.gv", is_file=True)

path = './test.xml'
urdf2g(path, "stdout.gv", is_file=True)
urdf2g(path, "stdout.gv", is_file=True, img_format='svg')
urdf2g(path, "stdout.gv", is_file=True, img_format='jpg')
urdf2g(path, "stdout.gv", is_file=True, img_format='pdf')
