stats count(*) as events by bin(1m)
| sort bin(1m) asc