dataDict={
    "a":{"r":1,
         "s":2,
         "t":3
         },
    "b":{
        "u":1,
        "v":{
            "x":1,
            "y":2,
            "z":3
            },
        "w":3
        }
    }
mapList=["a","r"]
def getFromDict(dataDict,mapList):
    for k in mapList:dataDict=dataDict[k]
    return dataDict

def setInDict(dataDict,mapList,value):
    for k in mapList[:-1]:dataDict=dataDict[k]
    dataDict[mapList[-1]]=value
print(mapList)
print(dataDict)







example={'foo':{'bar':{'baz':'ok'}}}
keys=['foo','bar']
def nested_set(element,values,*keys):
    if type(element) is not dict:
        raise AttributeError('nested_set() expects dict as first argument.')
    if len(keys)<2:
        raise AttributeError('nested_set() expects dict at least arguments,not enough given.')

    _keys=keys[:-1]
    _elements=element
    for key in _keys:
        _element=_elements[key]
    _element[keys[-1]]=value   
print(example)







           
