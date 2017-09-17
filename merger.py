# Tested with Python 3.6.2 on Windows 7 64bit (v3.6 required!)-python
import csv
import json
with open('D_Bahnhof_2017_09.csv', 'r', encoding='utf8') as csvfileinput, open('2017-09-15_stations.json', 'r', encoding='utf8') as jsonfileinput, open('D_Bahnhof_2017_09_BAHNHOFNUMMER.csv', 'w', encoding='utf8', newline='') as csvoutputfile:
	haltestellen = csv.reader(csvfileinput, delimiter=';')
	headers = next(haltestellen, None)
	stations = json.load(jsonfileinput)
	writer = csv.writer(csvoutputfile, delimiter=';', lineterminator='\r\n')
	
	if headers:
		headers.append('BAHNHOFNUMMER')
		writer.writerow(headers)
	
	exitFlag = False
	matchFlag = False
		
	for row in haltestellen:
		matchFlag = False
		for station in stations['result']:
			if exitFlag == True:
				exitFlag = False
				break
			for eva in station['evaNumbers']:
				if eva['number'] == int(row[0]):	# typecast to int
					exitFlag = True
					matchFlag = True
					row.append(str(station['number']));	# typecast to string
					break
		if matchFlag != True:
			row.append('');	# so csv.write will append a delimiter
		writer.writerow(row)