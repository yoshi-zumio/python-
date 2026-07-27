from datetime import date, datetime, timezone

dt = datetime.now(timezone.utc)
ts = dt.timestamp()

print(datetime.fromtimestamp(ts))
print(datetime.fromtimestamp(ts, timezone.utc))
print(date.fromtimestamp(ts))
