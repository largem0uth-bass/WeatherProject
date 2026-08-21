from metar import getMetar
from metar import dumpsMetar
from metar import formatMetar

KILNdata = getMetar("KILN")
formattedData = formatMetar(KILNdata)
for field in formattedData:
    print(formattedData.get(field))
    print()
