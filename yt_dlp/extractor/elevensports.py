from ..utils import ExtractorError
from .common import InfoExtractor


class ElevenSportsIE(InfoExtractor):
    IE_NAME = 'elevensports'
    _VALID_URL = r'https?://(?:www\.)?elevensports\.com/'

    def _real_extract(self, url):
        raise ExtractorError('This extractor is not yet implemented', video_id=self._match_id(url))
