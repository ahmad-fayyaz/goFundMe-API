from ninja import NinjaAPI, schema
from apify_client import ApifyClient

api = NinjaAPI()

@api.get("/funds")
def hello(request, query: str, limit: int):
    
    # Initialize the ApifyClient with your API token
    client = ApifyClient("<YOUR_API_TOKEN>")

    # Prepare the Actor input
    run_input = {
        "query": query,
        "limit": limit
    }

    # Run the Actor and wait for it to finish
    run = client.actor("RDZ33qDF65SRiTnxx").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    results = []
    for index, item in enumerate(client.dataset(run["defaultDatasetId"]).iterate_items()):
        if index >= limit:
            break
        results.append(item)
    
    return results