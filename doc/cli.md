# MediaManager module

The MediaManager module is a component of the overall application that handles the management of media files, including scanning directories for new files, renaming files, and updating metadata for files.

It is designed using SOLID principles which allows for greater modularity, testability, and maintainability of the overall application.

The MediaManager module defines an abstract class called *AbstractMediaManager* using the *abc* module, which defines three abstract methods: **scan_directory()**, **rename_files()**, and **update_metadata()**.

The class inherits from the AbstractMediaManager and provides concrete implementations of the abstract methods.

The MediaManager class takes instances of *FileSystem* and *MetadataService* classes where:

- The *FileSystem* class provides methods allowing interaction with the file system, such as listing files and renaming files.

- The *MetadataService* class provides methods for retrieving and updating metadata for the media files.

The **scan_directory()** method scans a directory for new media files and indexes them using the MetadataService.

The **rename_files()** method renames media files based on a specified format. It retrieves files using the MetadataService and renames them using the FileSystem.

The **update_metadata()** method updates metadata for media files using the MetadataService and the FileSystem.