from datetime import datetime
import dlt
from services.hubspot_api_service import HubSpotAPIService


def extract_deals(token: str, tenant_id: str, scan_id: str):
    service = HubSpotAPIService(token)
    after = None

    while True:
        data = service.get_deals(after)

        for deal in data.get("results", []):
            properties = deal.get("properties", {})

            yield {
                "deal_id": deal.get("id"),
                "deal_name": properties.get("dealname"),
                "amount": properties.get("amount"),
                "deal_stage": properties.get("dealstage"),
                "_scan_id": scan_id,
                "_tenant_id": tenant_id,
                "_extracted_at": datetime.utcnow()
            }

        if "paging" not in data or "next" not in data["paging"]:
            break

        after = data["paging"]["next"]["after"]


# 🔹 COMPATIBILITY WRAPPER (DO NOT REMOVE)
def create_data_source(*args, **kwargs):
    token = kwargs.get("auth_config", {}).get("accessToken")
    tenant_id = kwargs.get("job_config", {}).get("organizationId", "default")
    scan_id = kwargs.get("filters", {}).get("scan_id", "default")

    @dlt.resource(
        name="hubspot_deals",
        write_disposition="replace"
    )
    def hubspot_deals_resource():
        yield from extract_deals(token, tenant_id, scan_id)

    return [hubspot_deals_resource]
