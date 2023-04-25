import abc
from interfaces import AbstractMediaFile

class MediaFile(AbstractMediaFile):
    def __init__(self, file_path, metadata_service):
        self._file_path = file_path
        self._metadata_service = metadata_service
        self._metadata = None

    @property
    def file_path(self):
        return self._file_path

    @property
    def metadata(self):
        if self._metadata is None:
            self._metadata = self._metadata_service.get_metadata(self.file_path)
        return self._metadata

    @metadata.setter
    def metadata(self, new_metadata):
        self._metadata_service.set_metadata(self.file_path, new_metadata)
        self._metadata = new_metadata

    @property
    def file_extension(self):
        return self._file_path.split('.')[-1]
