# -*- coding: utf-8 -*-
"""Main module to launch Sanic application
"""

import argparse
import base64

from concurrent.futures import ThreadPoolExecutor
from urllib.parse import parse_qsl
from sanic import Sanic, response
from utils.logger import get_logger

app = Sanic(__name__)
logger = get_logger("app.py")

@app.middleware("response")
async def cors_headers_response(request, response):
    """Add CORS headers to all responses, including errors.
    """
    response.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin", "*")
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, PUT, PATCH, DELETE, OPTIONS, GET"
    response.headers["Access-Control-Allow-Headers"] = "X-Requested-With,X-Prototype-Version," \
                                                       "Content-Type,Cache-Control,Pragma,Origin, \
                                                       Cookie,authorization"
    response.headers["Access-Control-Max-Age"] = "3600"


@app.route("/")
async def test(request):
    """test GET method
    """
    return response.json({"hello": "world"})


@app.route("/PortfolioTest", methods=["POST"])
async def test_request_content2(request):
    """test POST method
    """
    session = {}
    request["session"] = session

    body = request.body
    if body is not None:
        body = base64.b64encode(body).decode("ascii")

    data = {
        "received": True,
        "message": request.json,
        "args": request.args, "url": request.url,
        "query_string": request.query_string,
        "request.scheme": request.scheme,
        "method": request.method,
        "path": request.path,
        "headers": request.headers,
        "body": body,
        "content": request.body,
        "form": request.form,
        "params": dict(parse_qsl(request.query_string)),
    }

    logger_string = "<requested data> : %s" % data
    logger.warning(logger_string)

    return response.json({"message": "OK"}, status=200)


@app.listener("before_server_start")
async def setup(app, loop):
    """server setup
    """
    app.executor = ThreadPoolExecutor(max_workers=5)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="description")
    PARSER.add_argument("--host", help="host", default="127.0.0.1")
    PARSER.add_argument("--port", help="port", default=8000, type=int)
    ARGUMENTS = PARSER.parse_args()

    CONFIG_DICT = {
        "LOG_LEVEL":"INFO"
    }

    app.config.update(CONFIG_DICT)
    app.run(host="127.0.0.1", port=8000)
