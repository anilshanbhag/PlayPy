Play API
========

Python API to access app statistics of different apps on the play store.

```
from play import PlayAPI
p = PlayAPI(debug=True)
p.get_stats("com.facebook.katana")
```
