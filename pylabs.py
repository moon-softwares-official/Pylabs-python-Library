# =========================================
# PyLabs Framework
# Made by Moon Softwares
# Version: 1.0
# =========================================

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests
import threading
import time


# =========================================
# DIGITAL SIGNATURE SYSTEM
# =========================================

_assinado = False


def Digital_signature(nome):

    global _assinado

    if nome.lower() == "moon softwares":

        _assinado = True

        print("""
=========================================
PyLabs Security Check Passed
Moon Softwares Signature Verified
=========================================
""")

    else:

        print("""
Invalid digital signature.
""")

        exit()


# =========================================
# SVG SUPPORT
# =========================================

def SVG(codigo):
    return codigo


# =========================================
# WIKIPEDIA SEARCH
# =========================================

def Wikipedia(pesquisa):

    try:

        url = f"https://pt.wikipedia.org/api/rest_v1/page/summary/{pesquisa}"

        resposta = requests.get(url)

        dados = resposta.json()

        return dados["extract"]

    except:

        return "Wikipedia search failed."


# =========================================
# JSON SUPPORT
# =========================================

def JSON(data):

    return json.dumps(data)


# =========================================
# TIMER
# =========================================

def Timer(segundos, func):

    def run():

        time.sleep(segundos)

        func()

    threading.Thread(target=run).start()


# =========================================
# COMPONENTS
# =========================================

def Card(titulo, texto):

    return f"""

    <div style='
    background:#1e293b;
    padding:20px;
    border-radius:20px;
    margin-top:20px;
    box-shadow:0 0 10px rgba(0,0,0,0.3);
    '>

    <h2 style='color:#60a5fa'>
    {titulo}
    </h2>

    <p>
    {texto}
    </p>

    </div>

    """


def Button(texto):

    return f"""

    <button style='
    background:#3b82f6;
    border:none;
    color:white;
    padding:12px 20px;
    border-radius:12px;
    cursor:pointer;
    font-size:16px;
    '>

    {texto}

    </button>

    """


# =========================================
# MAIN FRAMEWORK
# =========================================

class PyLabs:

    def __init__(self, nome):

        global _assinado

        if not _assinado:

            print("""

This application runs in Python and uses the pylabs library made by Moon Software.

The lack of a digital signature command completely blocks this application.

If you are the creator, please change the code to match what's on our YouTube channel.

            """)

            exit()

        self.nome = nome
        self.rotas = {}

        print(f"""
=========================================
PyLabs Started Successfully
Application: {nome}
Made by Moon Softwares
=========================================
""")


    # =====================================
    # ROUTES
    # =====================================

    def route(self, caminho):

        def decorator(func):

            self.rotas[caminho] = func

            return func

        return decorator


    # =====================================
    # SERVER
    # =====================================

    def run(self, host="0.0.0.0", porta=8080):

        rotas = self.rotas

        class Handler(BaseHTTPRequestHandler):

            def do_GET(self):

                if self.path in rotas:

                    resposta = rotas[self.path]()

                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()

                    self.wfile.write(resposta.encode())

                else:

                    self.send_response(404)
                    self.end_headers()

                    self.wfile.write(b"""
                    <h1>404</h1>
                    <p>Page not found.</p>
                    """)

        servidor = HTTPServer((host, porta), Handler)

        print(f"""
=========================================
Server Running
http://{host}:{porta}
=========================================
""")

        servidor.serve_forever()
