from zeep import Client
import xml.etree.ElementTree as ET

while True:
    client = Client(wsdl='http://localhost:8000/?wsdl')
    films = ET.Element('films')
    film = ET.SubElement(films, 'film')
    film.text = input("Enter film id(1-5): ")
    xml_send = ET.tostring(films)

    print("XML sent: {}".format(xml_send))
    print("Server answered: {}".format(client.service.getFilm(xml_send)))
