class JsonParser:
    def __init__(self, _json):
        self.parent_level_for_mode_0 = 1
        self.parent_level_for_mode_1 = 1
        self.keywords = self.getKeyIcos()
        self.keywordToFindName = "Spoluvlastnícky podiel"
        self.mode = 0  # 0 means looking for "Spoluvlastnícky podiel", 1 means looking for keyword
        self._json = _json

        self.tempName = None

        self.results = []

    def runParser(self):
        self.recursively_find_data(self._json)

    def getKeyIcos(self):
        with open("icos.txt", "r") as icos_file:
            icos_raw = icos_file.readlines()
            icos_stripped = [i.strip() for i in icos_raw]
            icos_complete = ['IČO: ' + i for i in icos_stripped]

        return icos_complete

    def checkValue(self, found_value_result, level_of_object):
        if found_value_result is not None and found_value_result['value_found']:
            if level_of_object == int(found_value_result['level_of_object']) - (self.parent_level_for_mode_0 if self.mode == 0 else self.parent_level_for_mode_1):
                return 1
            return 0
        return -1

    def valueMatch(self, value):
        if self.keywordToFindName in value and self.mode == 1:
            self.mode = 0

        if self.mode == 1:
            for keyword in self.keywords:
                if keyword in value:
                    # print(f'Value {value} found, keyword "{keyword}"')
                    return True
        else:
            if self.keywordToFindName in value:
                # print(f'Value {value} found, keyword "{keywordToFindName}"')
                return True

        return False

    def getTextValuesFromObject(self, obj):
        values = []
        for prop in obj:
            if type(prop) is not str:
                x = prop
            else:
                x = obj[prop]

            keys = x.keys()
            if "#text" in keys:
                text = x["#text"]
                text = text.strip()
                text = " ".join(text.split())
                # print(text)
                values.append(text)

        return values

    def printValue(self, value):
        print(value, '\n\n\n')

    def addItemToResults(self, items):
        newRecord = {
            'name': items[0],
            'hypotec': items[1]
        }
        self.results.append(newRecord)

    def recursively_find_data(self, json_object, level_of_object=0):
        if type(json_object) is str:
            return {'value_found': self.valueMatch(json_object), 'level_of_object': level_of_object}

        for idx, key in enumerate(json_object):
            _value = None
            if type(key) is dict:
                _value = key
            elif key is not None and len(key) > 0 and str(key)[0] != '@':
                _value = json_object[key]

            if _value is not None:
                if type(_value) is str and self.valueMatch(_value):
                    return {'value_found': True, 'level_of_object': level_of_object}

                found_value = self.recursively_find_data(_value, level_of_object + 1)
                resultValue = self.checkValue(found_value_result=found_value, level_of_object=level_of_object)

                if resultValue == -1:  # value was not found, moving forward
                    continue
                if resultValue == 0:  # value was found but program needs to go some levels of recursion up
                    return found_value
                if resultValue == 1:
                    # value was found and here program can print the value, and continue looking for another coincidence

                    values = self.getTextValuesFromObject(json_object)

                    if self.mode == 0:
                        # print(f'Id: {values[0]}')
                        self.tempName = values[1]
                    else:
                        name = self.tempName
                        hypotec = None
                        if len(values) == 1:
                            hypotec = values[0]
                        else:
                            hypotec = values[1]

                        self.addItemToResults([name, hypotec])
                        self.tempName = None

                    # change mode from 1 to 0, and from 0 to 1
                    self.mode ^= 1

                    continue

        return {'value_found': False, 'level_of_object': level_of_object}
