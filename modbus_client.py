import socket
from frame_reader import Frames_reader
import time
from pymodbus.client.sync import ModbusUdpClient

hostname = socket.gethostname()


def run_player():
    # запуск клиента
    client = ModbusUdpClient(hostname, 8234)
    client.connect()

    # переключение релейных выходов перед началом проигрывания анимации
    client.write_coil(0, 1)
    print('ON')

    # запуск проигрывания анимации
    play_animation()

    # переключение релейных выходов после окончания проигрывания анимации
    client.write_coil(0, 0)
    print('OFF')
    client.close()


def play_animation():
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # выгрузка всех пакетов из файла с анимацией в список с помощью импортированного кастомного класса
    frames_list = Frames_reader('Test_color.ani')

    # засекаем время начала проигрывания
    start = time.time()
    between = time.time()
    time.sleep(0.02)

    # алгоритм отправляет кадр на оба slave-устройства и проверяет в реальном времени, нужно ли отправлять новый кадр
    for frame in frames_list:
        while (time.time() - between) < 0.025:
            time.sleep(0.05)  # задержка для уменьшения нагрузки на систему
        else:
            # вместо различных IP адресов с одинаковыми портами использовался один и тот же IP с разными портами
            udp_sock.sendto(frame, ('192.168.56.1', 6454))
            udp_sock.sendto(frame, ('192.168.56.1', 6453))
            between += 0.025
            time.sleep(0.01)  # задержка для уменьшения нагрузки на систему

    # информация о времени и скорости проигранной анимации
    finish = time.time()
    print(f'Animation played in {round(finish - start)} seconds, {round(39168 / (finish - start))} frames per second')


if __name__ == "__main__":
    run_player()
