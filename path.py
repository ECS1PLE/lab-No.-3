from pathlib import Path


class PathUser:
    def __init__(self, path: Path | None = None):
        self.__path = path

    @property
    def get_path(self) -> Path | None:
        return self.__path

    @staticmethod
    def check_path(path: Path) -> bool:
        if not path.is_file():
            print("Файл не найден или указан путь к папке.")
            return False

        if path.suffix.lower() not in {".csv", ".xml"}:
            print("Поддерживаются только CSV и XML.")
            return False

        return True

    def get_file_path(self) -> Path | None:
        while True:
            user_path = input(
                "Введите путь до файла csv/xml или exit: "
            ).strip()

            if not user_path:
                print("Путь не может быть пустым.")
                continue

            if user_path.lower() == "exit":
                print("Выход из программы...")
                return None

            path = Path(user_path).expanduser()

            if self.check_path(path):
                self.__path = path
                return path
