import base64
from django.core import serializers
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.http.response import JsonResponse
from myapp import models
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from xml.etree.ElementTree import Element, SubElement, tostring

import http.client
import json
# import json.decoder.jso
import xml.etree.ElementTree as ET

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

        client = http.client.HTTPSConnection(osmRestApiUrl)
        client.request('PUT', '/api/0.6/changeset/create', tostring(root), osmHeaders())

        response = client.getresponse()

        if response.status == 200:
            return str(response.read(), 'utf-8')

        else:
            raise TypeError("Error Al intentar Crear Changeset OSM: " + str(response.read(), 'utf-8'))

    except:
        raise TypeError("Error Al intentar Crear Changeset OSM " + str(response.read(), 'utf-8'))

def cerrarChangeset(changeset):

    client = http.client.HTTPSConnection(osmRestApiUrl)
    client.request('PUT', '/api/0.6/changeset/' + changeset + '/close', None, osmHeaders())

    response = client.getresponse()

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def AgregarElemento(request, instrid):

    try:
        instrumento = models.Instrumento.objects.get(pk = instrid)

        if instrumento.instrtipo == 2:

            data = json.loads(request.body)
            osmelement = models.ElementoOsm.objects.get(pk = data['osmelement'])

            if osmelement.closed_way == 1:
                coordinates = data['coordinates'][0:len(data['coordinates'])-1]
            else:
                coordinates = data['coordinates']

            nodes = []
            changeset = agregarChangeset()
            nodeCount = 0

            # Armando XML
            root = Element('osmChange')
            root.set('version', '0.6')

            create = SubElement(root, 'create')

            # Creando Nodos

            for node in coordinates:
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

            #Creando Way
            way = SubElement(create, 'way')
            way.set('id', '-1')
            way.set('changeset', changeset)

            #Especificando Nodos del way
            for node in nodes:
                nd = SubElement(way, 'nd')
                nd.set('ref', node.get('id'))

            if osmelement.closed_way == 1:
                nd = SubElement(way, 'nd')
                nd.set('ref', nodes[0].get('id'))

            #Etiqueta de Elemento tipo Way
            tag = SubElement(way, 'tag')
            tag.set('k', osmelement.llaveosm)
            tag.set('v', osmelement.valorosm)

            # Obteniendo cadena XML a enviar a OSM
            xmlRequest = str(tostring(root), 'utf-8')

            #return HttpResponse(xmlRequest)

            #Almacendo Elemento en OSM
            client = http.client.HTTPSConnection(osmRestApiUrl)
            client.request('POST', '/api/0.6/changeset/' + changeset + '/upload', xmlRequest, osmHeaders())
            response = client.getresponse()

            if response.status == 200:

                # Cerrar Changeset OSM
                cerrarChangeset(changeset)

                xmlResponse = str(response.read(), 'utf-8')
                xmlObject = ET.fromstring(xmlResponse)
                wayElement = xmlObject.findall('way')[0]

                #Almacenando Cartografia
                cartografia = almacenarCartografia(instrid, wayElement.get('new_id'), osmelement.elemosmid)

                response = {
                    'code': 200,
                    #'cartografia': cartografia,
                    'status': 'success'
                }

            else:
                xmlResponse = str(response.read(), 'utf-8')
                raise TypeError("Error al momento de crear el elemento en OSM: " + xmlResponse)

        else:
            raise TypeError("El tipo de instrumento es inválido")

    except ObjectDoesNotExist as e:
        response = {
            'code': 404,
            'message': str(e),
            'status': 'error'
        }

    except ValidationError as e:
        response = {
            'code': 400,
            'message': str(e),
            'status': 'error'
        }

    except json.JSONDecodeError:
        response = {
            'code': 400,
            'message': 'JSON inválido',
            'status': 'error'
        }

    except IntegrityError as e:
        response = {
            'code': 400,
            'message': str(e),
            'status': 'error'
        }

    except TypeError as e:
        response = {
            'code': 400,
            'message': str(e),
            'status': 'error'
        }

    # except:
    #     response = {
    #         'code': 500,
    #         'status': 'error'
    #     }

    return JsonResponse(response, status=response['code'])

def almacenarCartografia(instrid, wayid, elemosmid):

    cartografia = models.Cartografia(instrid=instrid, osmid=wayid, elemosmid=elemosmid)
    cartografia.save()

    return serializers.serialize('python', [cartografia])[0]

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def elementosOsm(request):

    elementosOsm = models.ElementoOsm.objects.all().values()

    response = {
        'code': 200,
        'elementosOSM': list(elementosOsm),
        'status': 'success'
    }

    return JsonResponse(response, status=response['code'], safe=False)

def cartografiasInstrumento(request, instrid):

    try:
        instrumento = models.Instrumento.objects.get(pk = instrid)

        cartografias = models.Cartografia.filter(instrid__exact=instrid)

        if len(cartografias) > 0:

            print(cartografias)
            return HttpResponse("")

        else:
            raise ObjectDoesNotExist("No hay cartografias para este instrumento")

    except ObjectDoesNotExist as e:
        response = {
            'code': 404,
            'message': str(e),
            'status': 'error'
        }

    except ValidationError:
        response = {
            'code': 400,
            'status': 'error'
        }