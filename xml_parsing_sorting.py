import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

tree = ET.parse('produkty_CZ.xml')
root = tree.getroot()

a_file = open("CAT.txt", mode="r", encoding="utf-8")

list_of_lists = []
for line in a_file:
    list_of_lists.append(line.rstrip('\n'))
a_file.close()
print(list_of_lists, "\n")

SHOPITEM: Element
for SHOPITEM in root.findall('SHOPITEM'):
    for CATEGORIES in SHOPITEM.findall('CATEGORIES'):
        for CATEGORY in CATEGORIES:
            list_of_category = []
            list_of_category.insert(1, CATEGORY.text)
            print(list_of_category)
            if CATEGORY.text in list_of_lists:
                print("Položka nalezena v seznamu povolených")
                deleteCat = False
                break
            elif CATEGORY.text not in list_of_lists:
                print("Položka nenalezena v seznamu povolených")
                deleteCat = True

        if deleteCat == True:
            print(bcolors.WARNING + "Vyřazuji produkt", root.find('SHOPITEM'), " \n" + bcolors.ENDC)
            root.remove(SHOPITEM)
        else:
            print(bcolors.OKGREEN + "Produkt nesmazán \n" + bcolors.ENDC)

print(bcolors.OKCYAN + "Zápis výsledného .xml do souboru final.xml" + bcolors.ENDC)
tree.write('final.xml',encoding="UTF-8",xml_declaration=True)
