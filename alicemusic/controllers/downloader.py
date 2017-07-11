import pafy
import os
import os.path
import sh
from tempfile import mkdtemp
import shutil

from alicemusic import settings


class DownloadController(object):

    def __init__(self):
        self.pafy_object = None

    def process(self, request):
        url = request.form['url']
        self._get_pafy(url)
        if not self._needed():
            return
        filename = self._download()
        self._extract(filename)

    def _get_pafy(self, url):
        self.pafy_object = pafy.new(url)

    def _needed(self):
        if self.pafy_object.title + '.ogg' in os.listdir(settings.OGG_DIR):
            return False
        return True

    def _download(self):
        stream = self.pafy_object.getbestaudio()
        filepath = os.path.join(mkdtemp(), self.pafy_object.title)
        stream.download(filepath)

        return filepath

    @staticmethod
    def _extract(filepath):

        output_file = os.path.basename(filepath) + '.ogg'
        print('pre transcode')
        abs_output_file = os.path.join(
                settings.OGG_DIR, output_file)
        sh.avconv(
            '-i', filepath, '-vn',
            '-acodec', 'copy', abs_output_file)
        print('post transcode')

        shutil.rmtree(os.path.dirname(filepath))
