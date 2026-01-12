# HubSpot Deals API Integration

## API Version
HubSpot CRM API v3

## Authentication
Private App Access Token.

Header:
Authorization: Bearer <HUBSPOT_ACCESS_TOKEN>

## Endpoint
GET /crm/v3/objects/deals

Base URL:
https://api.hubapi.com

## Query Parameters
| Name | Description |
|----|------------|
| limit | Number of records per page |
| after | Cursor for pagination |
| properties | Fields to return |
| archived | Include archived records |

## Rate Limits
150 requests per 10 seconds.

## Error Handling
- 401: Invalid token
- 403: Missing scopes
- 429: Rate limit exceeded
