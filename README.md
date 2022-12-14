# animation_player
тестовое приложение на python3, воспроизводящее анимации на эмуляции slave-устройств
![image](https://user-images.githubusercontent.com/99408107/188551790-54875c30-a737-45a5-9cc3-c1db7a9b06c8.png)

**Запуск:**
1. Загрузить все файлы репозитория в одну дерикторию
2. Установить модуль pymodbus (если не установлен)
3. Запустить файлы серверов: modbus_server.py (реле), modbus_slave1.py (устройство), modbus_slave2.py (устройство)
4. Запустить клиент modbus_client.py


**Задание:**

Написать тестовое приложение на python3 которое будет запускаться на PC(платформа x86).

Задача приложения - проигрывать файлы анимации путем отправки ArtNet пакетов на DMX конвертеры и изменять состояния дополнительных устройств (пример:  реле, реальный набор сетевых устройств уточнить)

Конвертер DMX - это сетевое устройство, получающее данные по ethernet интерфейсу по протоколу ArtNET и передающее САМОСТОЯТЕЛНЬО в соответствии со стандартом DMX данные по каналам dmx к управляемым устройствам.
Данные в файлах анимации уже лежат в формате ArtNET. Достаточно считать их и послать на IP адреса конверетров. За каждым конвертером закреплены  ArtNet вселенные.
Адреса конвертеров:
192.168.0.1:6454 - вселенная 1.
192.168.0.2:6454 - все остальные вселенные.
 Данные необходимо передавать с частотой 40 кадров в секунду. 

Формат файла представляет из себя DMX пакеты идущие "друг за другом". Перед написанием "плеера" этих пакетов, необходимо ознакомиться со структурой этих пакетов (https://art-net.org.uk/structure/streaming-packets/artdmx-packet-definition)

Параметры проигрывания IP:port dmx конвертеров, кол-во повторений проигрывания, частота проигрывания и т.д. можно свободно задавать в программе в коде, в наиболее оптимальных типах данных языка python3, именовать на своё усмотрение.

Для передачи данных на modbus устройства, можно использовать модуль pymodbus(ModbusTcpClient).
Карта регистров используемого устройства
(модуль реле WB-MR6C): https://wirenboard.com/wiki/Relay_Module_Modbus_Management
IP адрес шлюза Ethernet-RS485 (Преобразователи интерфейсов WB-MGE): 192.168.0.10
порт обмена данными: 8234
ID релейного модуля (адрес Modbus-устройства): 33, достаточно управлять (вкл/выкл) 1 и 2 релейным выходом, можно сделать привязку ВКЛ к старту анимации, и ОТКЛ к остановке.




