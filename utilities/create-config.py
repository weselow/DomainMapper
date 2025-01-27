import json
import sys

def update_json_with_domains(input_file):
    # Исходный JSON шаблон
    json_data = {
        "domains": [],
        "dns": [
            "127.0.0.11:53",
            "77.88.8.88:53",
            "8.8.8.8:53",
            "1.1.1.1:53"
        ],
        "timeout": 3600,
        "ip4": [],
        "ip6": [],
        "cidr4": [],
        "cidr6": [],
        "external": {
            "domains": [],
            "ip4": [],
            "ip6": [],
            "cidr4": [],
            "cidr6": []
        }
    }

    try:
        # Чтение доменов из файла
        with open(input_file, 'r') as file:
            new_domains = [line.strip() for line in file if line.strip()]
        
        # Обновление JSON-данных
        json_data["domains"].extend(new_domains)
        json_data["domains"] = list(set(json_data["domains"]))  # Удаляем дубликаты

        # Запрос имени выходного файла
        output_file = input("Введите имя выходного файла (с расширением .json): ")
        if not output_file.endswith(".json"):
            output_file += ".json"
        
        # Запись в файл
        with open(output_file, 'w') as outfile:
            json.dump(json_data, outfile, indent=4)

        print(f"Файл сохранен как {output_file}")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <файл_с_доменами>")
    else:
        update_json_with_domains(sys.argv[1])
