import pandas as pd
from pathlib import Path
from addressRecord import addressRecord
from fileParser import FileParser

class CsvParser(FileParser):
    def parse(self, path: Path) -> dict[addressRecord, int]:
        data = pd.read_csv(
            path,
            sep=None,
            engine="python",
            dtype={
                "city": str,
                "street": str,
                "house": str,
                "floor": int,
            },
        )

        records: dict[addressRecord, int] = {}

        for row in data[
            ["city", "street", "house", "floor"]
        ].itertuples(index=False, name=None):
            record = addressRecord(*row)
            records[record] = records.get(record, 0) + 1
        return records