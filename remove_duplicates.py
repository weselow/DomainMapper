import sys

def remove_duplicates(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            unique_lines = set(f.readlines())

        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(sorted(unique_lines))  # Сортируем строки для удобства

        print(f"Уникальные строки сохранены в файл: {output_file}")

    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python script.py <имя_файла>")
    else:
        input_filename = sys.argv[1]
        output_filename = f"unique_{input_filename}"
        remove_duplicates(input_filename, output_filename)
