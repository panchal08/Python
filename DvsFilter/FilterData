import xml.etree.ElementTree


class DvsDataFilter:

    roomType = {'All'}
    floor = {'All'}
    key = ['All']

    def filterData(self, file):

        document = xml.etree.ElementTree.parse(file).getroot()

        for item in document.findall('node'):
            if item.get('room_type') != None:
                self.roomType.add(item.get('room_type'))

        print(sorted(self.roomType))

        roomTypeValue = input('Choice Room Type : ')
        for item in document.findall('node'):
            if (roomTypeValue == 'All' or item.get('room_type') == roomTypeValue) and item.get('room_type') != None:
                self.floor.add(item.get('floor'))
        print(sorted(self.floor))

        floorValue = input('Choice Floor : ')
        for item in document.findall('node'):
            if (floorValue == 'All' or item.get('floor') == floorValue) and item.get('floor') != None:
                self.key.append(item.get('key_no'))
        print(sorted(self.key))


if __name__ == '__main__':

    DvsDataFilter().filterData('resourcexml')
