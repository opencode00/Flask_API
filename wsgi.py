from apps import init_app

app = init_app()
@app.after_request
def add_header(r):
    r.headers.add('Access-Control-Allow-Methods','*')
    r.headers.add('Access-Control-Allow-Headers' , '*')
    r.headers.add('Access-Control-Allow-Origin', '*')
    return r

if __name__ == "__main__":
    # Datos de produccion / para desarrollo setEnv.(bat|ps1) + flask run
    app.run(host='0.0.0.0', port=13594)