import pafy
import sh


class DownloadController(object):

    @classmethod
    def process(cls, request):
        url = request.form['url']
        filename = cls._download(url)
        cls._extract(filename)

    @staticmethod
    def _download(url):
        pafy_object = pafy.new(url)
        stream = pafy_object.getbestaudio()
        filename = stream.download()
        print(filename)
        return filename

    @staticmethod
    def _extract(filename):
        sh.ffmpeg(
            '-i', filename, '-vn',
            '-acodec', 'copy', filename.rsplit('.', 1)[-2]+'.ogg')
