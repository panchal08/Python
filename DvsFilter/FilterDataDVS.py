import xml.etree.ElementTree
import json


class DvsDataFilter:

    roomType = {'All'}
    wing = {'All'}
    floor = {'All'}
    key = {'All'}

    def filterData(self, file):

        xmlDocument = xml.etree.ElementTree.parse("res.xml").getroot()
        jsonDocument = json.load(open('resource.json'))

        for item in xmlDocument.findall('node'):
            if item.get('room_type') != None:
                self.roomType.add(item.get('room_type'))
            if item.get('floor') != None:
                self.floor.add(item.get('floor'))
            if item.get('key_no') != None:
                self.key.add(item.get('key_no'))

        for item in jsonDocument.get('data'):
            self.wing.add(item.get('wing_name'))
        print(self.roomType, self.floor, self.key, self.wing)



if __name__ == '__main__':

    DvsDataFilter().filterData('res.xml')
