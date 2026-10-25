import http.server
import socketserver
import threading
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def local_server():
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("127.0.0.1", 0), handler) as httpd:
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        yield f"http://127.0.0.1:{port}"
        httpd.shutdown()

@pytest.fixture
def driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--headless=new")
    d = webdriver.Edge(options=options)
    yield d
    d.quit()

@pytest.fixture
def index_url(local_server):
    return f"{local_server}/index.html"