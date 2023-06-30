
from helperFunction import isNameExists, checkIfNameIsnull,allExistingCategories

def createCategories(categories):
    if len(categories) < 1:
        return

    for category in categories:
        if checkIfNameIsnull(category) == False:
            print('Category name can not be blank')
            return
        if isNameExists(category['name'], allExistingCategories()):
            print('Category name already exits')
            return

        if 'slug' not in category:
            category['slug'] = category['name'].lower().replace(" ","-")


        if 'description' not in category:
            category['description'] = ''

        if 'parent' not in category:
            category['parent'] = 0

    return categories













