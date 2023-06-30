from helperFunction import *
def deleteFunction(ID,categoryOrProduct):
    if ID < 0:
        return
    if len(categoryOrProduct) < 1:
        return
    response = wcapi.delete(f"{categoryOrProduct}/{ID}", params={"force": True})
    return response