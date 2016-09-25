import tasks
from flask import Flask, jsonify, request
import models
from werkzeug.wrappers import Response
from werkzeug.wsgi import DispatcherMiddleware

API_ROOT = '/api/1.0'

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = API_ROOT


@app.route('/pages')
def show_pages():
    pages = models.get_all()

    return jsonify(pages)


@app.route('/pages/add', methods=['POST'])
def fetch_new_page():
    new_page = models.Page(
        title=request.json['title'],
        link=request.json['link'],
        path=request.json['path']
    )

    models.add(new_page)

    tasks.fetch_page.apply_async((new_page.link, new_page.path), expires=30)

    return jsonify(new_page.as_dict())


def noop(env, resp):
    response = Response('OK')
    return response(env, resp)

app.wsgi_app = DispatcherMiddleware(noop, {API_ROOT: app.wsgi_app})

# For debugging only
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Development Server Help')
    parser.add_argument("-d", "--debug", action="store_true", dest="debug_mode",
                        help="run in debug mode (for use with PyCharm)", default=False)
    parser.add_argument("-p", "--port", dest="port",
                        help="port of server (default:%(default)s)", type=int, default=5000)

    cmd_args = parser.parse_args()
    app_options = {"port": cmd_args.port}

    if cmd_args.debug_mode:
        app_options["debug"] = True
        app_options["use_debugger"] = False
        app_options["use_reloader"] = False

    app.run(**app_options)