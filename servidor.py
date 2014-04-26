import fileinput
import re
import subprocess

tipo = './InfracompSeguridad/'
properties = 'servidor.properties'
jar = 'servidor.jar'

# Iterar sobre seguridad y no seguridad
for j in range(0, 2):

	# Iterar sobre el número de threads
	for i in range(0, 5):
	
		# Reemplazar la cantidad de threads para iterar
		for line in fileinput.input(tipo + properties, inplace=True):
			print(re.sub('[0-9]+$', '{}'.format(2 ** i), line), end='')
		
		# Ciencia, acá es lo chévere
		for k in range(0, 50):
			# Inicializar el servidor
			subprocess.call(['java', '-jar', tipo + jar])
			
			# Llamar al proceso remoto que inicia GLoad y recibir sus resultados
			# debe ser síncrono
			# TODO
			
			# Apagar servidor y agrupar resultados de la prueba
			# TODO
		
	tipo = './InfracompNoSeguridad/'