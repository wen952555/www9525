import requests

def fetch_free_nodes(api_url: str) -> list:
    """
    Fetch free nodes from the given API URL.
    :param api_url: The URL of the API to fetch free nodes from.
    :return: A list of free nodes.
    """
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # 假设 API 返回数据格式为 {"nodes": ["node1", "node2", ...]}
        return data.get("nodes", [])
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch nodes from {api_url}: {e}")