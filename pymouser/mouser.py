import requests, json


# Type aliases
MouserItem = dict[str: str]


class MouserAPI:
    SEARCH_API_KEY: str = None

    def __init__(self, search_api_key: str):
        self.SEARCH_API_KEY = search_api_key

    def search_by_PN(self, part_number: str) -> MouserItem:
        req_url = "https://api.mouser.com/api/v1/search/partnumber?apiKey=%s" % self.SEARCH_API_KEY

        req_body = {
            "SearchByPartRequest": {
                "mouserPartNumber": part_number,
                "partSearchOptions": "Exact"
            }
        }

        req_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.post(url=req_url, data=json.dumps(req_body), headers=req_headers).json()
        results = response['SearchResults']
        errors = response['Errors']
        
        return (errors, results)
