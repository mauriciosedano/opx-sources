from django.conf import settings
from django.core.mail import send_mail

def gestionCambios(usuarios, tipoReceptor, nombreReceptor, tipoCambio, detalle = ""):

    # Definición de tipos de cambio
    tiposCambio = {
        1:  'Cambio de Objetivo',
        2: 'Cambio de Tiempo',
        3: 'Cambio de Equipo',
        4: 'Cambio de Territorio'
    }

    # Asunto de la notificación via correo
    subject = "Notificacion de Cambio"

    # Verificacion de la existencia de tipo de cambio recibido
    cambio = tiposCambio.get(tipoCambio, None)

    if cambio is not None:
        message = "Hola. Ha habido un {} en {} {}." \
                  "<br /> {}" \
                  .format(cambio, tipoReceptor, nombreReceptor, detalle)

        # Envío de Notificación de Correo
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            usuarios,
            fail_silently = False,
            html_message = message
        )

        response = True

    else:
        response = False

    return response



