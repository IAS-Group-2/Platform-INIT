import json
import os

here = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(here, 'index.json')

def get_new_index(type):
    """
    get the new index of the type
    type 0: service
    type 1: application
    """
    f = open(file, 'r')
    data = json.load(f)
    
    if type == 0:
        data["service_index"] += 1
    elif type == 1:
        data["app_index"] += 1
    else:
        return -1
    
    f.close()
    f = open(file, 'w')
    json.dump(data, f)
    f.close()
    return str(type)+str(data[('app' if type==1 else 'service')+"_index"])
