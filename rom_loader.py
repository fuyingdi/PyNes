import pprint
import OpenGL_PlayGround


class Rom_Loader:
    banks = {}
    bank_id = 0
    pc = 0
    rs = 0
    ines_pgr = 1
    ines_map = 1
    ines_mir = 1

    header = ''

    def nes_id(self):
        return [0x4e, 0x45, 0x53, 0x1a]

    def nes_get_header(self):
        id = self.nes_id
        unused = [0, 0, 0, 0, 0, 0, 0, 0]
        header = []
        header.extend(id)
        header.append(self.ines_map)
        header.append(self.ines_mir)
        header.append(self.ines_pgr)
        header.extend(unused)
        return header

    def get_PRG_page_count(self):
        pass

    def get_CHR_page_count(self):
        pass

    def get_PRG_page(self, index):
        pass

    def get_CHR_page(self, index):
        pass

    def get_mapper(self):
        pass

    def is_horizontal_mirroring(self):
        pass

    def is_vertical_mirroring(self):
        pass

    def is_SRAM_enabled(self):
        pass

    def is_512_byte_trainer_present(self):
        pass

    def is_four_screen_mirroring(self):
        pass

    def getTrainer(self):
        pass


# 传入读到的bytes构造ROM对象
class ROM:
    row_content = ''
    row_header = ''
    row_prg = ''
    row_chr = ''

    prg_size = 0
    chr_size = 0

    header = {}
    prg = ''
    chr = ''

    rom_mapper = ''

    def __init__(self, content):
        self.row_content = content
        self.row_header = content[0:15]
        self.set_header()
        self.set_prg()
        self.set_chr()

    def set_header(self):
        row_header = self.row_header
        self.header['fixed_flag'] = row_header[0:4]
        self.header['prg_size'] = row_header[4:5].hex()
        self.header['chr_size'] = row_header[5:6].hex()
        for i in range(6, 11):
            self.header['flag' + str(i)] = row_header[i: i + 1].hex()
        self.header['unused'] = row_header[11:15].hex()

        self.prg_size = int(self.header['prg_size']) * 16 * 1024
        self.chr_size = int(self.header['chr_size']) * 8 * 1024

        self.header['mapper'] = self.header['flag7']

    def set_prg(self):
        content = self.row_content[16:]
        self.row_prg = content[0:self.prg_size]

    def set_chr(self):
        content = self.row_content[16 + self.prg_size:]
        self.row_chr = content[0:self.chr_size]


class BinaryReader:
    @staticmethod
    def readfile(path, method='bytes'):
        with open(path, 'rb') as f:
            if method == 'hex':
                return f.read().hex()
            elif method == 'bytes':
                return f.read()


def combine2layer():
    result = ''
    index = 0
    while True:
        row = bin(rom1.row_chr[index])[2:].ljust(8, '0')
        row_shadow = bin(rom1.row_chr[index + 1])[2:].ljust(8, '0')
        for i in range(0, 8):
            # result += str(int(row[i]) + int(row_shadow[i]) * 2)
            result += str(int(row[i]))
            # result += str(int(row_shadow[i]))

        # result += '\n'
        index += 2
        if index >= len(rom1.row_chr):
            break
    return result


if __name__ == "__main__":
    content = BinaryReader.readfile("mario.nes")
    rom1 = ROM(content)
    pprint.pprint("row_header:" + str(rom1.row_header))
    pprint.pprint("row_header_hex:" + rom1.row_header.hex())
    pprint.pprint(rom1.header)
    print("rom1_prg: " + str(rom1.row_prg[:20]) + "......")
    print("rom1_chr: " + str(rom1.row_chr[:20]) + "......")

    print(type(rom1.row_chr))
    index = 0
    while (True):
        print(bin(rom1.row_chr[index])[2:].ljust(8, '0'))
        index += 1
        if (index >= len(rom1.row_chr)):
            break

    with open('chr_combine', 'w+') as f:
        res = combine2layer()
        index = len(res) // 2
        x = 0
        y = 200
        row = 0
        while index < len(res):
            OpenGL_PlayGround.draw_pixel(x, y, int(res[index]))
            x += 1
            if(index+1) / 64 % 24 == 0:
                x = 0
                row += 1
            if (index+1) % 64 == 0:
                x += 8
                y = 200 - 8 * row
                f.write('\n')
            if (index+1) % 8 == 0:
                x -= 8
                y -= 1
                f.write('\n')
            f.write(res[index-1])
            index += 1



    OpenGL_PlayGround.main()


    # with open("chr", mode="w+")as f:
    #     index = 0
    #     row_num = 0
    #     x = 0
    #     y = 320
    # while (True):
    #     # f.write(bin(rom1.row_chr[index])[2:].ljust(8, '0')+'\n')
    #     row = bin(rom1.row_chr[index])[2:].ljust(8, '0')
    #     for bit in row:
    #         if bit == '1':
    #             OpenGL_PlayGround.draw_pixel(x, y)
    #         x += 1
    #     x -= 8
    #     y -= 1
    #     if (index + 1) % 8 == 0:
    #         x += 8
    #         y = 320 - 8 * row_num
    #     if (index + 1) / 8 % 40 == 0:
    #         x = 0
    #         row_num += 1
    #     index += 1
    #     if index >= len(rom1.row_chr):
    #         break
    # OpenGL_PlayGround.main()
