
def checkId(id):
    if(type(id) == str):
        return True
    else:
        raise Exception(f"The vertex id must be string. Type of {id} is", type(id))
        

def checkWeight(weight):
    if(type(weight) == int):
        return True
    else:
        raise Exception(f"The weight must be integer. Type of {weight} is", type(weight))
        