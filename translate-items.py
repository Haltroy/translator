from googletrans import Translator
from googletrans.constants import LANGUAGES
import xml.etree.ElementTree as ET
import sys

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    data_list = []

    for child in root:
        data_list.append({"name": child.get("name"), "value": child[0].text})

    return data_list

if __name__ == "__main__":

    before = ''
    after = ''
    template = ''
    original = ''

    if len(sys.argv) < 3:
        print("USAGE: python translate-items.py <original> <template> [before] [after]")
        print("<> - Required arguments ")
        print("[] - Optional arguments ")
        sys.exit(0)

    original = sys.argv[1]

    templateF = open(sys.argv[2], 'r')
    template = templateF.read()
    templateF.close()

    if len(sys.argv) > 3:
        beforeF = open(sys.argv[3], 'r')
        before = beforeF.read()
        beforeF.close()


    if len(sys.argv) > 4:
        afterF = open(sys.argv[4], 'r')
        after = afterF.read()
        afterF.close()

    result = parse_xml(original)

    translator = Translator()

    for lang in LANGUAGES:
        f = open('result-' + lang + '.xml', 'w')
        f.write(before)
        for item in result:
            if item['name'] is None: continue
            if item['value'] is None: continue
            translation = translator.translate(item['value'], dest=lang).text.replace("&","&amp;").replace("<","&lt;").replace(">","&lgt;").replace("\"","&quot;").replace("\'","&apos;")
            content = template.replace('$name$', item['name']).replace('$value$', translation)
            f.write(content)
        f.write(after)
        f.close()
        print('Done:' + lang)
