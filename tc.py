import urllib
import re
 
url = "http://www.sat.gob.mx/sitio_internet/asistencia_contribuyente/informacion_frecuente/tipo_cambio/"
 
def listarTipoCambio():
    sock = urllib.urlopen(url)
    htmlSource = sock.read()
    tcs = re.findall("\d+/\d\d\.\d+",htmlSource)
    for tc in tcs:
        tcTmp = tc.split("/")
        print "El tipo de cambio para el dia %s es: %s" % (tcTmp[0], tcTmp[1])
   
listarTipoCambio()
