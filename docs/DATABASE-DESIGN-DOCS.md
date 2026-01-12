# Database Schema – HubSpot Deals

```sql
CREATE TABLE hubspot_deals.deals (
    deal_id VARCHAR PRIMARY KEY,
    deal_name TEXT,
    amount NUMERIC(12,2),
    deal_stage TEXT,
    pipeline TEXT,
    close_date TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,

    _scan_id UUID NOT NULL,
    _tenant_id VARCHAR NOT NULL,
    _extracted_at TIMESTAMP NOT NULL
);
```
