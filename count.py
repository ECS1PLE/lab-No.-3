class count_floors:
    def __init__(self):
        self.__count = {}

    @property
    def get_dict(self):
        return self.__count

    def count_floors(self, records):
        self.__count = {}
        for item in records:
            if item.city not in self.__count:
                self.__count[item.city] = {
                    floor: 0 for floor in range(1, 6)
                }

                if 1<=item.floor<=5:
                    self.__count[item.city][item.floor] += 1
        return self.__count

                
