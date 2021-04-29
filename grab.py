from requests import get
from json import dumps
from urllib.parse import urlencode

def grabJSON(**kwargs):
    ENDPOINT = "https://api.coronavirus.data.gov.uk/v2/data"

    filters = [f"areaName={ kwargs['areaName'] }"]

    if 'areaType' in kwargs:
        filters.append(f"areaType={ kwargs['areaType'] }")

    structure = {
        "date": "date",
        "metric": kwargs['metricName']
    }   

    api_params = {
        "filters": str.join(";", filters),
        "structure": dumps(structure, separators=(",", ":"))
    }

    encoded_params = urlencode(api_params)

    response = get(ENDPOINT, params=encoded_params, timeout=20)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()
