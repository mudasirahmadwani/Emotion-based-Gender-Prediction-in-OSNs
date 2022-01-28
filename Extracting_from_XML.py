from xml.etree import ElementTree as ET
source= '''<root>
  <conversation>
    <message>
      <author>97964e7a9e8eb9cf78f2e4d7b2ff34c7</author>
      <time>03:20</time>
      <text>Hola.</text>
    </message>
    </conversation>
    </root>'''

root = ET.fromstring(source)
conversation = root.findall('.//conversation')
for con in conversation:
    m=con.find('text').text
    print(m)