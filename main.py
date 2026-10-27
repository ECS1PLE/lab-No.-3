import xml.etree.ElementTree as ET

from path import PathUser
from csvParser import CsvParser
from xmlParser import XML_Parser
from csv import Error as CsvError

from count import count_floors

import time
def main():
    path_user = PathUser()

    parsers = {
        ".csv": CsvParser(),
        ".xml": XML_Parser(),
    }

    while True:
        path = path_user.get_file_path()

        if path is None:
            return

        try:
            start_time = time.time()
            parser = parsers[path.suffix.lower()]
            records = parser.parse(path)
            counter = count_floors()

            for record, count in records.items():
                if count > 1:
                    print(record, count)

            result_floors = counter.count_floors(records)
            work_time = time.time() - start_time

            for city, floors in result_floors.items():
                    print(f"\nГород: {city}")
                    for floor in range(1, 6):
                        print(
                            f"Количество зданий с {floor} эт.: {floors[floor]}"
                        )

            print(f"\nВремя обработки: {work_time:.3f} с")

        except (OSError, ValueError, KeyError, ET.ParseError, CsvError) as error:
            print(f"Ошибка обработки файла: {error}")


if __name__ == "__main__":
    main()