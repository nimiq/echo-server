# echo-server
An echo server for debugging purpose

Launch it with:
```
$ ./server.py
```
or:
```
$ ./server.py xml '<?xml version="1.0" encoding="UTF-8" ?><methodResponse><params>\n<param><value><struct>\n<member><name>success</name><value><i4>1</i4></value></member>\n</struct></value></param>\n</params></methodResponse>\n\n\n'
```

Test it with curl:
```
curl http://127.0.0.1:50000/api/order/add_order/ -d "id=123456&customer=509347002&reason=whatever&description=nowayyy"
```