import requests
from waste_collection_schedule import Collection  # type: ignore[attr-defined]
from waste_collection_schedule.service.ICS import ICS

TITLE = "Südbrandenburgischer Abfallzweckverband"
DESCRIPTION = "SBAZV Brandenburg, Deutschland"
URL = "https://www.sbazv.de"
TEST_CASES = {
    "Wildau": {"url": "https://fahrzeuge.sbazv.de/WasteManagementSuedbrandenburg/WasteManagementServiceServlet?ApplicationName=Calendar&SubmitAction=sync&StandortID=1369739001&AboID=10760&Fra=P;R;WB;L;GS"},

    # Additional test cases can be added here
}

ICON_MAP = {
    "Restmülltonnen": "mdi:trash-can",
    "Laubsäcke": "mdi:leaf",
    "Gelbe Säcke": "mdi:sack",
    "Papiertonnen": "mdi:package-variant",
    "Weihnachtsbäume": "mdi:pine-tree",
}

class Source:
    def __init__(self, url):
        self.url = url
        self._ics = ICS()

    def fetch(self):
        standort_id = self.url.split("StandortID=")[1].split("&")[0]
        abo_id = self.url.split("AboID=")[1].split("&")[0]

        url = "https://fahrzeuge.sbazv.de/WasteManagementSuedbrandenburg/WasteManagementServiceServlet"
        params = {
            "ApplicationName": "Calendar",
            "SubmitAction": "sync",
            "StandortID": standort_id,
            "AboID": abo_id,
            "Fra": "P;R;WB;L;GS"
        }

        # GET request to retrieve ICS file
        r = requests.get(url, params=params)
        
        # Check if the response is successful
        if r.status_code != 200:
            raise ValueError(f"Error fetching ICS data. Status code: {r.status_code}")

        # Parse ICS data
        dates = self._ics.convert(r.text)

        entries = []
        for d in dates:
            waste_type = d[1].strip()
            next_pickup_date = d[0]
            # Remove duplicates
            if any(
                e.date == next_pickup_date and e.type == waste_type for e in entries
            ):
                continue
            entries.append(
                Collection(
                    date=next_pickup_date,
                    t=waste_type,
                    icon=ICON_MAP.get(waste_type),
                )
            )

        return entries