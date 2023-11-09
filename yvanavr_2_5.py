# A function that returns the name of the root property that a particular integer lives in
def getRootProperty(obj, wanted_value):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if getRootProperty(value, wanted_value):
                return key
    elif isinstance(obj, list):
        if wanted_value in obj:
            return True
    return None


object = {
    "r1n": {
        "mkg": {
            "zma": [21, 45, 66, 111],
            "mii": {
                "ltf": [2, 5, 3, 9, 21]
            },
            "fv": [1, 3, 6, 9]
        },
        "rmk": {
            "amr": [50, 50, 100, 150, 250]
        }
    },
    "fik": {
        "er": [592, 92, 32, 13],
        "gp": [12, 34, 116, 29]
    }
}

print(getRootProperty(object, 250))
print(getRootProperty(object, 116))
print(getRootProperty(object, 111))
print(getRootProperty(object, 999))
