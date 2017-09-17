# Haltestellen-Stations-Merger

Python (3.6) script for adding the DB Station&Service AG "BAHNHOFNUMMER" from the StaDa-API[1] into the CSV file "Haltestellendaten"[1] - where the "EVA_NR" matches a "number" in "evaNumbers" arry of a "result" object.

Getting StaDa data via curl (see "2017-09-15_stations.json" in script):
curl -X GET --header "Accept: application/json" --header "Authorization: Bearer PUTYOUROWNKEYHERE" "https://api.deutschebahn.com/stada/v2/stations"

Data by Deutsche Bahn / DB Station&Service AG (CC BY 4.0)

[1] https://developer.deutschebahn.com/store/apis/info?name=StaDa-Station_Data&version=v2&provider=DBOpenData

[2] https://data.deutschebahn.com/dataset/data-haltestellen
