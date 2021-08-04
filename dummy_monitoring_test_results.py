import json


# modelop.init
def begin():
    pass

# modelop.score
def action(data):
    yield data

# modelop.metrics
def metrics(df):
    with open("model_test_results.json", "r") as f:
        contents = f.read()
    test_results = json.loads(contents)
    yield test_results
