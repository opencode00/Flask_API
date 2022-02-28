from apps import init_app

app = init_app()
@app.after_request
def add_header(r):
    r.headers.add('Access-Control-Allow-Methods','*')
    r.headers.add('Access-Control-Allow-Headers' , '*')
    r.headers.add('Access-Control-Allow-Origin', '*')
    return r

if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    app.run(host='127.0.0.1', port=5001)