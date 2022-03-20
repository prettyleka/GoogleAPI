from serpapi import GoogleSearch

search = GoogleSearch({"q": "Ukraine",  "serp_api_key": "39ffbd93e2e3def175a2a1d47da51d16399a3cf592b2da38f67b57a4948aac42"})
result = search.get_dict()
print(result['search_information']['total_results'])

