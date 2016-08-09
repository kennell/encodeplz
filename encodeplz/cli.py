import click
from .app import app
from .server import StandaloneServer


@click.command()
@click.option(
    '--port',
    default=5000,
    help='Port to listen on, default is 5000'
)
def main(port):
    server_options = {
        'bind': '{ip}:{port}'.format(
            ip='0.0.0.0',
            port=port
        ),
        'workers': 4,
        'accesslog': '-',
        'errorlog': '-'
    }
    app.config['ENCODEPLZ_PORT'] = port
    StandaloneServer(app, server_options).run()


if __name__ == '__main__':
    main()