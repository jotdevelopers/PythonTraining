import xml.etree.ElementTree as ET

data = '''<persons>
<person>
<name>aa</name>
<age>12</age>
</person>
<person>
<name>aa</name>
<age>13</age>
</person>
<person>
<name>aa</name>
<age>12</age>
</person>
<person>
<name>aa</name>
<age>14</age>
</person>
</persons> '''
tree = ET.fromstring(data)
for name in tree.findall('person'):
    print(name.find('name').text)
    print(name.find('age').text)
    print("======================")
