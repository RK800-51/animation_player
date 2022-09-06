# класс читает весь файл покадрово и помещает каждый кадр в список

class Frames_reader():
    def __init__(self, file):
        self.list = []
        self._read_frames(file)

    def __iter__(self):
        self.m = -1
        return self

    def __next__(self):
        self.m += 1
        try:
            result = self.list[self.m]
        except IndexError:
            raise StopIteration
        return result

    def _read_frames(self, file):
        f = open(file, 'rb')
        i = 0
        while True:
            f.seek(i * 530)
            frame = f.read(530)
            if not frame:
                break
            self.list.append(frame)
            i += 1
