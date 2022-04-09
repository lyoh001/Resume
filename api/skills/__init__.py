import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        body=json.dumps({"text": "Python, Machine Learning, Deep Learning, DevOps, MLOps, AWS, Azure"}),
    )
