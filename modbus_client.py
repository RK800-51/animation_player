import socket
from frame_reader import Frames_reader
import time
from pymodbus.client.sync import ModbusUdpClient

hostname = socket.gethostname()


def run_player():
    # ������ �������
    client = ModbusUdpClient(hostname, 8234)
    client.connect()

    # ������������ �������� ������� ����� ������� ������������ ��������
    client.write_coil(0, 1)
    print('ON')

    # ������ ������������ ��������
    play_animation()

    # ������������ �������� ������� ����� ��������� ������������ ��������
    client.write_coil(0, 0)
    print('OFF')
    client.close()


def play_animation():
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # �������� ���� ������� �� ����� � ��������� � ������ � ������� ���������������� ���������� ������
    frames_list = Frames_reader('Test_color.ani')

    # �������� ����� ������ ������������
    start = time.time()
    between = time.time()
    time.sleep(0.02)

    # �������� ���������� ���� �� ��� slave-���������� � ��������� � �������� �������, ����� �� ���������� ����� ����
    for frame in frames_list:
        while (time.time() - between) < 0.025:
            time.sleep(0.05)  # �������� ��� ���������� �������� �� �������
        else:
            # ������ ��������� IP ������� � ����������� ������� ������������� ���� � ��� �� IP � ������� �������
            udp_sock.sendto(frame, ('192.168.56.1', 6454))
            udp_sock.sendto(frame, ('192.168.56.1', 6453))
            between += 0.025
            time.sleep(0.01)  # �������� ��� ���������� �������� �� �������

    # ���������� � ������� � �������� ����������� ��������
    finish = time.time()
    print(f'Animation played in {round(finish - start)} seconds, {round(39168 / (finish - start))} frames per second')


if __name__ == "__main__":
    run_player()
