from rom_loader import BinaryReader
from rednerer import Renderer


testfile = 'masmix.nes'


def test_reader():
    str1 = BinaryReader.readfile(testfile)
    str2 = BinaryReader.readfile(testfile, "hex")
    assert(str1[0:3] == b'NES')
    assert(str2[0:8] == '4e45531a')
    print("reader ok")


if __name__ == "__main__":
    test_reader()
    renderer = Renderer()
    renderer.run()
    renderer.test_random_points()
    
    
