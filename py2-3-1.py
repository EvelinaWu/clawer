import xml.etree.ElementTree as ET

xml_data = '''
    <weather_report>
        <city name="台北">
            <temp>25</temp>
            <status>多雲</status>
        </city>
    </weather_report>
'''

root = ET.fromstring(xml_data)

print(root.tag)

city_node = root.find("city")
print("都市:",city_node.get("name"))

temp_node = city_node.find("temp")
