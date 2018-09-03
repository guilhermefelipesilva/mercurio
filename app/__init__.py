import logging
from vibora import Vibora

from app.api import api
from app.user.views import user_api
from app.user.model import db
from app.hooks.logging import teste

from raven.conf import setup_logging
from raven.handlers.logging import SentryHandler

app = Vibora()

app.add_blueprint(user_api, prefixes={'v1': '/v1'})
app.add_blueprint(api, prefixes={'v1': '/v1'})

app.add_hook(teste)

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

handler = SentryHandler(
    'https://8623ba4c373649b7ad625d951f619561:010d9e8c13c54533b33cca5b4c7281a0@sentry.io/1273731')
handler.setLevel(logging.ERROR)

setup_logging(handler)
