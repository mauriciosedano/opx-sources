import base64
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.http.response import JsonResponse
import http.client
import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring

osmRestApiUrl = 'master.apis.dev.openstreetmap.org'

def osmHeaders():

    credentials = 'inge4neuromedia@gmail.com:;K7c8`EQ+82eyHKd'.encode('utf-8')
    credentialsEncode = str(base64.b64encode(credentials), 'utf-8')

    headers = {
        'Authorization': 'Basic ' + credentialsEncode,
        'Content-Type': 'text/xml'
    }

    return headers

def agregarChangeset():

    try:
        #Armando XML
        root = Element('osm')

        changeset = SubElement(root, 'changeset')
        changeset.set('version', '0.6')

        tag = SubElement(changeset, 'tag')
        tag.set('k', 'comment')
        tag.set('v', 'test')

        client = http.client.HTTPSConnection('master.apis.dev.openstreetmap.org')
        client.request('PUT', '/api/0.6/changeset/create', tostring(root), osmHeaders())

        response = client.getresponse()

        if response.status == 200:
            return str(response.read(), 'utf-8')

        else:
            raise TypeError

    except:
        raise TypeError


def AgregarElemento(request, instrid):

    try:
        data = json.loads(request.body)
        print(type(data))

        nodes = []
        changeset = agregarChangeset()
        nodeCount = 0

        # Armando XML
        root = Element('osmChange')
        root.set('version', '0.6')

        create = SubElement(root, 'create')
        coordinatesLength = len(data['coordinates'])

        # Creando Nodos en XML
        for node in data['coordinates'][0:coordinatesLength-1]:
            nodeCount -= 1
            longitud = str(node['lon'])
            latitud = str(node['lat'])

            node = SubElement(create, 'node')
            node.set('id', str(nodeCount))
            node.set('lon', longitud)
            node.set('lat', latitud)
            node.set('version', "0")
            node.set('changeset', changeset)

            nodes.append(node)

        #Reset nodecount
        nodeCount = 0

        #Creando Way
        way = SubElement(create, 'way')
        way.set('id', '-1')
        way.set('changeset', changeset)

        #Especificando Nodos
        for node in nodes:
            nodeCount -= 1
            nd = SubElement(way, 'nd')
            nd.set('ref', node.get('id'))

        nd = SubElement(way, 'nd')
        nd.set('ref', nodes[0].get('id'))

        xmlRequest = str(tostring(root), 'utf-8')

        #Almacendo Elemento en OSM
        client = http.client.HTTPSConnection(osmRestApiUrl)
        client.request('POST', '/api/0.6/changeset/' + changeset + '/upload', xmlRequest, osmHeaders())
        response = client.getresponse()

        if response.status == 200:
            xmlResponse = str(response.read(), 'utf-8')
            xmlObject = ET.fromstring(xmlResponse)
            wayElement = xmlObject.findall('way')[0]

            response = {
                'code': 200,
                'osmid': wayElement.get('new_id'),
                'status': 'success'
            }

        else:
            raise TypeError

    except:
        response = {
            'code': 500,
            'status': 'error'
        }

    return JsonResponse(response, status=response['code'])