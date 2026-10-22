from pathlib import Path
import xml.etree.ElementTree as ET

from addressRecord import addressRecord
from fileParser import FileParser

class XML_Parser(FileParser):
    def parse(self, path: Path) -> dict[addressRecord, int]:
        records:dict[addressRecord, int] = {}
        tree = ET.parse(path)
        root = tree.getroot()

        for item in root.findall("item"):
            record = addressRecord(
                city=item.attrib["city"],
                street=item.attrib["street"],
                house=item.attrib["house"],
                floor=int(item.attrib["floor"]),
            )

            records[record] = records.get(addressRecord, 0) + 1
        return records