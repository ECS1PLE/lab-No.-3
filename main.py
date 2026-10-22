from path import PathUser
from csvParser import CsvParser


def main():
    path_user = PathUser()

    while True:
        path = path_user.get_file_path()

        if path is None:
            return

        if path.suffix.lower() != ".csv":
            print("XML-парсер пока не подключён.")
            continue

        try:
            parser = CsvParser()
            records = parser.parse(path)

            for record, count in records.items():
                print(record, count)

        except (OSError, ValueError) as error:
            print(f"Ошибка обработки файла: {error}")


if __name__ == "__main__":
    main()