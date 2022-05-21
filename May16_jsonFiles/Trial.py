import json

data = {
    "details1": {
        "name": "YxZ",
        "subject": "Engineering",
        "City": "Pune"
    },
    "details2": {
        "name": "AcB",
        "subject": "Science",
        "City": "Chennai"
    }
}

if __name__ == '__main__':

    #  Opens the json file in write mode to overwrite the data
    with open('sample.json', 'w') as f:
        """Serialization is the process wherein we \
                convert the data type of the raw data into a JSON format.
        """
        json.dump(data, f, indent=4, separators=(',', ': '))

    #  Opens the json file in read mode to dump data, throws an error
    """with open('sample.json', 'r') as f:
        json.dump(data, f)
    """
    with open('sample.json', 'r+') as f:
        """with deserialization, we can easily convert\
        the JSON data into the default/native data type which is usually a dictionary.
        """
        a = json.load(f)
        print(a, '\n')
        for item in a:
            print(a[item]['name'])

    with open('sample.json', 'a') as f:
        json.dump({"name": "John", "age": 30}, f)
        json.dump(["apple", "bananas"], f)
        print(json.dumps(("apple", "bananas")))
        print(json.dumps("hello"))
        print(json.dumps(42))
        print(json.dumps(31.76))
        print(json.dumps(True))
        print(json.dumps(False))
        print(json.dumps(None))
