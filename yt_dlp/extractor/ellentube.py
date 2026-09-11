from ..utils import ExtractorError
from .common import InfoExtractor


class EllenTubeIE(InfoExtractor):
    IE_NAME = 'ellentube'
    _VALID_URL = r'https?://(?:www\.)?ellentube\.com/'

    def _real_extract(self, url):
        raise ExtractorError('This extractor is not yet implemented', video_id=self._match_id(url))


class EllenTubeVideoIE(InfoExtractor):
    IE_NAME = 'ellentube:video'
    _VALID_URL = r'https?://(?:www\.)?ellentube\.com/video/.+'

    def _real_extract(self, url):
        raise ExtractorError('This extractor is not yet implemented', video_id=self._match_id(url))


class EllenTubePlaylistIE(InfoExtractor):
    IE_NAME = 'ellentube:playlist'
    _VALID_URL = r'https?://(?:www\.)?ellentube\.com/playlist/.+'

    def _real_extract(self, url):
        raise ExtractorError('This extractor is not yet implemented', video_id=self._match_id(url))
