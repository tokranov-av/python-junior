def open_and_close_file(file_path: str) -> None:
    """Открывает и закрывает файл.

    Args:
        file_path: путь до файла
    """
    try:
        with open(file_path, "r", encoding="utf") as file:
            for line in file.readlines():
                print(line)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except EOFError:
        print("Ошибка чтения файла.")
