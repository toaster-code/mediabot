import os
import shutil
import requests
import argparse
from interfaces import AbstractMediaManager, AbstractCLI

class MediaFile:
    def __init__(self, path: str):
        self.path = path
        self.name = os.path.basename(path)

    def rename(self, new_name: str):
        pass

    def update_metadata(self):
        pass

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

class IMDbProvider(MetadataProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_metadata(self, title: str):
        pass

class TheTVDBProvider(MetadataProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_metadata(self, title: str):
        pass

class MetadataUpdater:
    def __init__(self, providers: list):
        self.providers = providers

    def update_metadata(self, media_file: MediaFile):
        pass


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


class CLI(AbstractCLI):
    def __init__(self, media_manager):
        self.media_manager = media_manager

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Media Manager')
        subparsers = parser.add_subparsers(title='Commands', dest='command')

        scan_parser = subparsers.add_parser('scan', help='Scan directory for media files')
        scan_parser.add_argument('directory', help='Directory to scan')

        rename_parser = subparsers.add_parser('rename', help='Rename media files')
        rename_parser.add_argument('--format', help='File naming format')

        update_parser = subparsers.add_parser('update', help='Update metadata for media files')

        args = parser.parse_args()
        return args

    def run(self):
        args = self.parse_args()

        if args.command == 'scan':
            self.media_manager.scan_directory(args.directory)

        elif args.command == 'rename':
            self.media_manager.rename_files(args.format)

        elif args.command == 'update':
            self.media_manager.update_metadata()

        else:
            print('Invalid command')


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
