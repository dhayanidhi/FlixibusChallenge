### Installation
Works in python >=3.5.xxx 

```
cd CodingChallange
pip install .
```

### Start service

```
modelservice
```

### Functional test
```
pip install pytest
cd CodingChallange
pytest

```

### REST end point test
```
curl -X GET http://127.0.0.1:5000/challenge/model 
     -H "Content-Type: application/json" 
     -d '{"features":[
                        {"id":19, "feature1":"dummy", "feature2":"dummy"},
                        {"id":9, "feature1":"dummy", "feature2":"dummy"},
                        {"id":31, "feature1":"dummy", "feature2":"dummy"}
                      ]}'
```