# Release Notes

Release notes for AutoFTG python script


---

### 2023/02/12

## `2.6.4`

- Fixed camera selection bug that prevented to define new settings
- Fixed variables in Chunk Quick Add


---

### 2023/02/12

## `2.6.3`

- Reorganized functions to separate files for easier further development
- Added settings dialog for Point Cloud processing in Batch Chunk Creator
- Changed status icons in tree list for processing/processed items
- Added columt to display chunk name for existing items, or processing time for items processed
- Added total time of processing for processed queue
- Some minor bug-fixes and improvements


---

### 2023/02/01

## `2.6.2`

- Created tabs for settings in Batch Chunk Creator
- Added dialog for Align Photos settings
- Added new options in chunk definitions settings file
- Minor bug-fixes


---

### 2023/01/31

## `2.6.1`

- Changed batch process logging to use python.csv module for working with log files.
- Updated mesh settings dialog to include options for depth maps generation.
- Changed values for 'mesh_depthmaps' and 'mesh_face_count_custom'.
- Removed manual batch processing as it will be replaced with post-processing function.
- Updated icons for options in Model Settings dialog.
- Improved routines for batch processing.
- Moved progress bar text inside the pprogress bar.
- Fixed 'Process' button status text when processing is in progress.
- Added new folder 'gui_designs' that contains GUI designs for dialogs used in AutoFTG.
- Files cleanup.


---

### 2023/01/28

## `2.6.0`

- Implemented processing of mesh, textures, point cloud, and data export options in Batch Chunk Creator
- List in Batch Chunk Creator now also show status for mesh and point cloud process (only works if done with batch processing)
- Added 'export_folder' to chunk definition settings (each definition has it's own export location)
- Settings dialog to editing options for mesh/texture processing in Batch Chunk Creator
- Added some new icons used in Batch Chunk Creator
- Added option in Batch Chunk Creator to open currently selected folder in File Explorer
- Added save and reset buttons in Batch Chunk Creator to store or reset current settings
- Created placeholder checkbox to disable importing of new data (in case if doing batch processing of Align Photos, Mesh, Point Cloud separatley for already imported chunks)
- Minor bug-fixes and improvements


---

### 2023/01/25

## `2.5.6` ... `2.5.9`

- Integrated option to align chunk when doing batch import
- Added column to see which chunks were aligned at import
- Added option 'set as default' to chunk definition and camera combo boxes in Batch Chunk Creator
- Implemented loading of project settings when starting Batch Chunk Creator
- Fixed column widths in Batch Chunk Creator folder list (now adjusts to contents)
- New menu/dialog for 'Chunk Definition Settings' to Add/Edit/Delete chunk definitions.


---

### 2023/01/17

## `2.5.5`

- Added process log file for projects. (Logs imported chunks)
- New logo icon for AutoFTG


## `2.5.4`

1. Cleanup


---

### 2023/01/16

## `2.5.3`

- Updates and improvements for processing progres indicators.
- Added check for options:
  - Automatic Processing
  - Automatic Target Detection
  - Import Marker Coordinates


---

### 2023/01/14

## `2.5.2`

- Added processing progres indicators.


---

### 2023/01/14

## `2.5.1`

- Added check for point file and image number in Batch Chunk Creator
- Fixed chunk prefix-suffix handling


---

### 2023/01/13

## `2.5.0`

- Added new Batch Chunk Creator
- Minor bug-fixes and improvements


---

### 2023/01/01

## `2.4.6-RC`

- Reworked settings storage for all settings files to use *.ini file strusture.
- Minor improvements for Camera Editer, Camera Add/Edit, and Edit Settings dialogs.


---

### 2023/01/01

## `2.4.5-RC`

- Upgraded Add/Edit Camera dialog to use PySide2 module
- Added new options for camera Type/SubType in cameras settings (cam_settings.ini)
- Added 'Spherical', 'Cylindrical', and 'RPC' camera type options
- Added new icons for camera type/subtype
- Redone camera list refreshing in Camera Editor
- Added new settings for chunk creation (category, menu icon, chunk name prefix/suffix)
- Changed menu options for adding chunks<br>*Now opens a dialog window with drop-down menu containing a list of availabile settings for new chunk creation.*


---

### 2022/12/31

## `2.4.4-RC`

- Fixed list in camera editor (not loading properly ofter adding/editing camera)
- Fixed dialogs for editing prefix/suffix for chunk name creation


---

### 2022/12/30

## `2.4.3-RC`

- Fixed list in camera editor (not loading properly ofter adding/editing camera)
- Fixed camera Save/Edit functions in Camera Editor, so they are now saved with correct values


---

### 2022/12/29

## `2.4.2-RC`

- Added option `SubType` and `Resolution` to camera settings configuration (__cam_settings.ini__)
- Replaced easygui dialogs for Qt PySide2 custom dialog:
  - New Dialog Class: `class Ui_dialogChooseCamera()`

- Function definitions using new camera selection dialog:
  - Updated: `def cam_calibrationSettings()`
  - Updated: `def cam_calibrationChunk()`
  - Updated: `def newchunk_aero()`

- Updated camera list in Camera Editor to use new icons
- Updated `def appAbout()` to use PySide2 message box dialog


## `2.4.1-beta`

- Replaced icon resorces to a more consistent themeing


---

### 2022/12/23

## `2.4.0-beta`

- Added more options to modify prefix/suffix for chunk names in New Chunk (2TIR)
- Fixed bug where script was in infinite loop when no project was present and user tried to load settings
- Reprogrammed default/current camera dialog to use PySide2 library instead of easygui


## `2.3.3-beta`

- Added basic options to modify prefix/suffix for chunk names in New Chunk (2TIR)
- Settings for chunk name prefix/suffix are saved to settings file


## `2.3.2-beta`

- Changed chunk naming format from prefix to suffix for following functions:
  - *New Chunk (2TIR)/STOPNICA (IZKOP)*
  - *New Chunk (2TIR)/STOPNICA (B.BET.)* 
- Removed redundant 'Project File' value from settings.


---

### 2022/12/18

## `2.3.1-beta`

- Updated resources
- Minor bux fix in menu icons


---

### 2022/12/18

## `2.3.0-beta`

- New settings per project module added


---

### 2022/12/11

## `2.2.0-beta`

- Major redesign for camera settings (no longer hard-coded)
- New camera settings configuration
- New 'Add Camera' function
- Better settings loading
- Improved settings reset code
- Bug fixes


---

### 2022/12/04

## `2.1.1-beta`

- Minor bug fixes in new chunk creation routines
- Updated README.md to include installation instructions
- Some file reorganization


---

### 2022/11/27

## `2.1.0-beta`

- New settings menu
- Settings loading process redesigned to be more consistent (still needs some polishing)
- Added new icons
- Added 'About AutoFTG' in menu
- Changed main 'New Chunk' method to give more options when creating chunk


---

### 2022/11/06

## `2.0.x-beta`

- Added basic settings menus
- New icons for menu items
- Completley rewritten routines for settings initialization and loading


---

### 2022/10/16

## `1.7.6`

- Reorder manus for default settings


---

### 2022/10/09

## `1.7.5`

- Added options to change default settings for:
  - Change default project folder
  - Change default camera calibration
  - Change default point filtering spacing
  - Change default point sampling


---

### 2022/09/25

## `1.1`

- Working version. First usable script.


---

### 2022/09/11

## `1.0`

- Initial version of AutoFTG
- Create chunk script


---

