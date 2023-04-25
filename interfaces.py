# Interfaces and abstract classes

import abc

class AbstractMediaManager(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def scan_directory(self, directory):
        pass

    @abc.abstractmethod
    def rename_files(self, file_format):
        pass

    @abc.abstractmethod
    def update_metadata(self):
        pass

class AbstractCLI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def parse_args(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass


class AbstractMetadataUpdater(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_metadata(self, file_path):
        pass

    @abc.abstractmethod
    def set_metadata(self, file_path, metadata):
        pass

class AbstractMediaFile(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def file_path(self):
        pass

    @abc.abstractproperty
    def metadata(self):
        pass

    @abc.abstractproperty
    def file_extension(self):
        pass