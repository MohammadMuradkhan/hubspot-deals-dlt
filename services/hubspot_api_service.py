import requests
import time


class HubSpotAPIService:
    """
    Service for interacting with HubSpot Deals API
    """

    def __init__(self, token: str):
        self.base_url = "https://api.hubapi.com"
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def get_deals(self, after=None):
        """
        Fetch deals from HubSpot with pagination support
        """
        params = {"limit": 100}
        if after:
            params["after"] = after

        response = requests.get(
            f"{self.base_url}/crm/v3/objects/deals",
            headers=self.headers,
            params=params,
            timeout=10
        )

        # Handle rate limiting
        if response.status_code == 429:
            time.sleep(1)
            return self.get_deals(after)

        response.raise_for_status()
        return response.json()
