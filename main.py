from sys import exit

route = [
	{'dari': 'jakarta', 'ke': 'bekasi', 'jarak': 35},
	{'dari': 'jakarta', 'ke': 'depok', 'jarak': 25},
	{'dari': 'jakarta', 'ke': 'tangerang', 'jarak': 35},

	{'dari': 'bogor', 'ke': 'depok', 'jarak': 25},
	{'dari': 'bogor', 'ke': 'bekasi', 'jarak': 50},
	{'dari': 'bogor', 'ke': 'tangerang', 'jarak': 35},
	{'dari': 'bogor', 'ke': 'cianjur', 'jarak': 50},

	{'dari': 'depok', 'ke': 'jakarta', 'jarak': 25},
	{'dari': 'depok', 'ke': 'bogor', 'jarak': 25},
	{'dari': 'depok', 'ke': 'bekasi', 'jarak': 35},
	{'dari': 'depok', 'ke': 'tangerang', 'jarak': 35},

	{'dari': 'tangerang', 'ke': 'jakarta', 'jarak': 35},
	{'dari': 'tangerang', 'ke': 'depok', 'jarak': 35},
	{'dari': 'tangerang', 'ke': 'bogor', 'jarak': 35},
	{'dari': 'tangerang', 'ke': 'serang', 'jarak': 50},

	{'dari': 'bekasi', 'ke': 'jakarta', 'jarak': 35},
	{'dari': 'bekasi', 'ke': 'bogor', 'jarak': 50},
	{'dari': 'bekasi', 'ke': 'depok', 'jarak': 35},
	{'dari': 'bekasi', 'ke': 'karawang', 'jarak': 35},
]

def cekAsal(kota):
	exist = False
	for rute in route:
		if rute['dari'] == kota:
			exist = True
	return exist

def cekRute(asal, tujuan, dict, blacklist = []):
	data = []
	for x in dict:
		if (x['dari'] == asal) and (x['ke'] not in blacklist):
			if x['ke'] == tujuan:
				data.append(x)
				break
			else:
				dict.remove(x)
				blacklist.append(x['dari'])
				rec = cekRute(x['ke'], tujuan, dict, blacklist)
				if rec != []:
					x['lalu'] = rec
					data.append(x)
	return data

def ruteTerbaik(rute):
	data = {}
	for i in range(len(rute)):
		r = rute[i]
		jarak = 0
		while r != None:
			jarak += r['jarak']
			if 'lalu' in r:
				for x in r['lalu']:
					r = x
			else:
				r = None
		if ('jarak' not in data) or (jarak < data['jarak']):
			data['jarak'] = jarak
			data['rute'] = rute[i]
	return data

def printRute(data):
	if data == {}:
		print('Rute tidak ditemukan')
	else:
		rute = data['rute']
		output = ''
		while rute != None:
			output += 'dari ' + rute['dari'] + ' ke ' + rute['ke']
			if 'lalu' in rute:
				output += ' lalu '
				rute = rute['lalu'][0]
			else:
				output += ' dengan total jarak ' + str(data['jarak']) + 'km'
				rute = None
		print(output)

a = input('Masukkan kota asal: ')
while (cekAsal(a) == False):
	print('Rute tidak ditemukan')
	if input('Coba lagi? (y/n)') == 'y':
		a = input('Masukkan kota asal: ')
	else:
		exit()

b = input('Masukkan kota tujuan: ')

possibleRoute = cekRute(a, b, route)
bestRoute = ruteTerbaik(possibleRoute)
printRute(bestRoute)
