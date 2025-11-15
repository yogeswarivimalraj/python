import requests

def api_data_fetcher(base_url, start_page=1):
   
    page = start_page

    while True:
        url = base_url.format(page)
        print(f"Fetching Page {page}...")

        response = requests.get(url)

        if response.status_code != 200:
            print("Error fetching API!")
            break

        data = response.json()

       
        if not data:
            break

        yield data
        page += 1
base_url = "https://jsonplaceholder.typicode.com/posts?_page={}"

for page_data in api_data_fetcher(base_url):
    print(page_data)