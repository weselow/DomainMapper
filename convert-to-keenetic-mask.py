import os
import re

# Функция для конвертации маршрутов до подсетей
def convert_to_subnet_route(route, mask="255.255.255.0"):
    # Разбираем строку маршрута, ожидая формат: ip route <IP> <CIDR> <GW> <IF> <optional>
    match = re.match(r'ip route (\d+\.\d+\.\d+\.\d+)/32 (\d+\.\d+\.\d+\.\d+) (\S+) .+', route)
    if match:
        ip = match.group(1)  # Извлекаем IP
        gw = match.group(2)  # Шлюз
        interface = match.group(3)  # Интерфейс
        # Создаем подсеть с маской /24 (по умолчанию) и возвращаем строку маршрута для подсети
        subnet = '.'.join(ip.split('.')[:3]) + '.0'
        return f"route add {subnet} mask {mask} {gw} IF {interface}"
    return None

# Получаем все файлы result-*.txt в текущей директории
for filename in os.listdir('.'):
    if filename.startswith('result-') and filename.endswith('.txt'):
        # Генерируем имя выходного файла с расширением .bat
        output_filename = f"result-config-{filename[7:-4]}.bat"  # убираем ".txt" и добавляем ".bat"
        with open(filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                # Конвертируем строку маршрута в маршрут до подсети
                converted_route = convert_to_subnet_route(line.strip())
                if converted_route:
                    outfile.write(converted_route + '\n')

        print(f"Конфигурация для {filename} сохранена в {output_filename}")
