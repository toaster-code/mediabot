# CLI

import argparse
from interfaces import AbstractCLI

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