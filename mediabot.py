import os
import shutil
import requests
import argparse
from interfaces import (AbstractMediaManager,
                        AbstractMetadataUpdater,
                        AbstractMediaFile,
                        AbstractCLI)
from mediafile import MediaFile
from providers import IMDbProvider, TheTVDBProvider
from cli import CLI

class Movie(MediaFile):
    def __init__(self, path: str):
        super().__init__(path)

    def update_metadata(self):
        pass

class Series(MediaFile):
    def __init__(self, path: str, season: int, episode: int):
        super().__init__(path)
        self.season = season
        self.episode = episode

    def update_metadata(self):
        pass

class MetadataProvider:
    def get_metadata(self, title: str):
        pass

class MetadataUpdater(AbstractMetadataUpdater):
    def __init__(self, metadata_service):
        self.metadata_service = metadata_service

    def get_metadata(self, file_path):
        return self.metadata_service.get_metadata(file_path)

    def set_metadata(self, file_path, metadata):
        self.metadata_service.set_metadata(file_path, metadata)


class MediaManager(AbstractMediaManager):
    def __init__(self, file_system, metadata_service):
        self.file_system = file_system
        self.metadata_service = metadata_service

    def scan_directory(self, directory):
        files = self.file_system.list_files(directory)
        self.metadata_service.index_files(files)

    def rename_files(self, file_format):
        files = self.metadata_service.get_files()
        for file in files:
            new_name = file_format.format(file)
            self.file_system.rename_file(file, new_name)

    def update_metadata(self):
        files = self.metadata_service.get_files()
        for file in files:
            metadata = self.metadata_service.get_metadata(file)
            self.file_system.update_metadata(file, metadata)


if __name__ == '__main__':
    # Initialize metadata providers
    imdb_provider = IMDbProvider(api_key='your_api_key')
    tvdb_provider = TheTVDBProvider(api_key='your_api_key')
    metadata_providers = [imdb_provider, tvdb_provider]

    # Initialize metadata updater
    metadata_updater = MetadataUpdater(providers=metadata_providers)

    # Initialize media manager
    media_manager = MediaManager(path='/path/to/media/files', metadata_updater=metadata_updater)

    # Initialize command-line interface
    cli = CLI(media_manager=media_manager)

    # Run the program
    cli.run()
