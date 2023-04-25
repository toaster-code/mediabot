# MediaBot Application

The proposed application has several modules that interact with each other. The interconnections between these modules are as follows:

1. The **CLI module** interacts with the MediaManager module to receive user commands and provide output to the user.

2. The **MediaManager module** interacts with the MetadataUpdater module to update metadata for media files.

3. The **MetadataUpdater module** interacts with the **MetadataProvider modules** (i.e., **IMDbProvider** and **TheTVDBProvider**) to retrieve metadata for media files.

4. The **MediaManager module** interacts with the **MediaFile modules** (i.e., **Movie** and **Series**) to perform actions such as renaming and updating metadata.

5. The **Movie** and **Series** modules inherit from the MediaFile module to share common functionality.

6. The **MetadataProvider** and **MetadataUpdater** modules use HTTP requests to interact with external APIs, such as the IMDb and TheTVDB APIs.

7. The **IMDbProvider** and **TheTVDBProvider** modules use API keys to authenticate requests and retrieve metadata from their respective sources.

8. The **MediaManager module** interacts with the file system using the *os* and *shutil* modules to scan directories, rename files, and move files to new directories.

Overall, the modules are interconnected through method calls and parameter passing, and each module has a specific responsibility and interacts with other modules to accomplish the overall goal of renaming and updating metadata for media files. The use of modules and object-oriented programming allows for modularity and extensibility of the application.