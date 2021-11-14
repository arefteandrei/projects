import xml.etree.ElementTree as ET

from spyne import Application, ServiceBase, Unicode, rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

films = {'1': {'Title': 'The Great Gatsby', 'Year': '2013', 'Type': 'History'},
         '2': {'Title': 'The Walking Dead', 'Year': '2010', 'Type': 'Horror'},
         '3': {'Title': 'Home Alone', 'Year': '1998', 'Type': 'Comedy'},
         '4': {'Title': 'Eternals', 'Year': '2021', 'Type': 'Drama'},
         '5': {'Title': 'Last Night In Soho', 'Year': '2010', 'Type': 'Horror'}
         }


class ExampleService(ServiceBase):

    @rpc(Unicode, _returns=Unicode)
    def getFilm(ctx, request):
        try:
            r = ET.fromstring(request)
        except:
            return 'No XML sent'
        try:
            return 'Requested film: %s' % films[r[0].text]
        except:
            return 'Film not found'


application = Application(
    services=[ExampleService],
    tns='example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11())

application = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    print("listening to http://127.0.0.1:8000")
    print("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, application)
    server.serve_forever()
