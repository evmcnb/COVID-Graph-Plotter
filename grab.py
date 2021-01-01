from requests import get
from json import dumps
from urllib.parse import urlencode


def grabJson(areaType, areaName, metricName):
    ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"

    filters = [
        f"areaType={ areaType }",
        f"areaName={ areaName }"
        ]

    structure = {
        "date": "date",
        "metric": metricName
        }   

    api_params = {
        "filters": str.join(";", filters),
        "structure": dumps(structure, separators=(",", ":"))
        }

    encoded_params = urlencode(api_params)

    response = get(ENDPOINT, params=api_params, timeout=20)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()

#print(grabJson("ltla", "ipswich", "newCasesByPublishDate"))