import requests, json

WCSID = "1J02zvv7fKemdpL03F6pZ5YCCU3E0ROa" # COPY your "wcsid" cookie here

def pp(d):
    print(json.dumps(d, indent=4))

def get_identifiers(result):
    return [x['properties']['identifier']['value'] for x in result['entities']]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    "Cookie": "wcsid:%s" % WCSID
}

def search(endpoint, query=[], order=[], field_ids=['identifier'], limit=5):
    response = requests.post(
        "https://www.crunchbase.com/v4/data/%s/search" % endpoint,
        headers=headers,
        json={
            "query": query,
            "order": order,
            "field_ids": field_ids,
            "limit": limit,
    })
    data = response.json()
    return data

print("Worst Company with Employees between 101 to 150")

result = search(
    endpoint="companies",
    query=[{
        "type": "predicate",
        "field_id": "num_employees",
        "operator_id": "eq",
        "values": ["00101_00250"]}],
    limit=1,
    order=[{"field_id": "rank", "sort": "desc"}])

pp(result)
print(get_identifiers(result))
print()

print("Find at least five companies that went this week.")

result = search(
    endpoint="companies",
    query=[{
        "type": "predicate",
        "field_id": "went_public_on_date",
        "operator_id": "gte",
        "values": ["1/10/2016"]}],
    order=[{"field_id": "rank", "sort": "asc"}],
    limit=5,
    field_ids=["identifier", "short_description", "rank"])

pp(result)
print(get_identifiers(result))
print()

print("Find at least five investors with a last name of Patel.")

result = search(
    endpoint="investors",
    query=[{
        "type": "sub_query",
        "relationship_id": "people",
        "query": [{
                "type": "predicate",
                "field_id": "last_name",
                "operator_id": "contains",
                "values": ["Patel"]
        }]
    }],
    order=[{"field_id": "rank", "sort": "asc"}],
    limit=5,
    field_ids=["identifier","num_investments","num_exits"])

pp(result)
print(get_identifiers(result))
print()

print("What is the name and rank of the best school with 1001-5000 employees?")

result = search(
    endpoint="schools",
    query=[{
        "type": "predicate",
        "field_id": "num_employees",
        "operator_id": "includes",
        "values": ["01001_05000"],
    }],
    order=[{"field_id": "rank", "sort": "asc"}],
    limit=1,
    field_ids=["identifier", "short_description", "rank"])

pp(result)
print(get_identifiers(result))
print()

print("Name at least 3 acquisitions that happened this week.")

result = search(
    endpoint="acquisitions",
    query=[{
        "type": "predicate",
        "field_id": "announced_on",
        "operator_id": "gte",
        "values": ["1/10/2016"]
    }],
    limit=3,
    field_ids=["identifier"])

pp(result)
print(get_identifiers(result))
print()

