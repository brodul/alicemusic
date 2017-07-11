from flask import Blueprint
from flask import request

from alicemusic.controllers.downloader import DownloadController
# more a router than a view


downloader = Blueprint('downloader', __name__, url_prefix='/downloader')


@downloader.route('/', methods=['GET', 'POST'])
def index():
    dc = DownloadController()
    dc.process(request)
    return 'OK'
