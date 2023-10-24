# CFKV

A simple wrapper to communicate with [Cloudflare KV Store ](https://developers.cloudflare.com/kv/). It can be used as a cache and features will be implemented to be used in frameworks such as ```FastAPI```


### Simple Usage

```
import KVStore
import datetime

store = KVStore(namespace_id="YOUR_NAMESPACE_ID", account_id="ACCOUNT_ID", api_key="API_KEY")


# Usage Example
key = "sample_key"
get = store.get(key)

if get is None:
    data = {"test": True, "date": str(datetime.datetime.now())}
    store.set(key)
    data['stored'] = False
    get = data
else:
    data['stored'] = True

print(get)



```