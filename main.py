from pathlib import Path
import xml.etree.ElementTree as ET

from path import PathUser
from csvParser import CsvParser
from xmlParser import XML_Parser


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
            parser = parsers[path.suffix.lower()]
            records = parser.parse(path)

            for record, count in records.items():
                print(record, count)

        except (OSError, ValueError, KeyError, ET.ParseError) as error:
            print(f"Ошибка обработки файла: {error}")


if __name__ == "__main__":
    main()