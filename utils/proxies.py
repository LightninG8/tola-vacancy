def format_proxy(proxy):
  return {
    "proxy_type": proxy["proxy_type"],
    "addr": proxy["addr"],
    "port": proxy["port"],
    "username": proxy["username"],
    "password": proxy["password"],
    "rdns": proxy["rdns"],
  }
