# Release Notes

Release notes for AutoFTG python script


---

## `2023/01/17`

### 2.5.4

1. Cleanup


---

## `2023/01/16`

### 2.5.3

1. Updates and improvements for processing progres indicators.
2. Added check for options:
  - Automatic Processing
  - Automatic Target Detection
  - Import Marker Coordinates


---

## `2023/01/14`

### 2.5.2

1. Added processing progres indicators.


---

## `2023/01/14`

### 2.5.1

1. Added check for point file and image number in Batch Chunk Creator
2. Fixed chunk prefix-suffix handling


---

## `2023/01/13`

### 2.5.0

1. Added new Batch Chunk Creator
2. Minor bug-fixes and improvements


---

## `2023/01/01`

### 2.4.6-RC

1. Reworked settings storage for all settings files to use *.ini file strusture.
2. Minor improvements for Camera Editer, Camera Add/Edit, and Edit Settings dialogs.


---

## `2023/01/01`

### 2.4.5-RC

1. Upgraded Add/Edit Camera dialog to use PySide2 module
2. Added new options for camera Type/SubType in cameras settings (cam_settings.ini)
3. Added 'Spherical', 'Cylindrical', and 'RPC' camera type options
4. Added new icons for camera type/subtype
5. Redone camera list refreshing in Camera Editor
6. Added new settings for chunk creation (category, menu icon, chunk name prefix/suffix)
7. Changed menu options for adding chunks<br>*Now opens a dialog window with drop-down menu containing a list of availabile settings for new chunk creation.*


---

## `2022/12/31`

### 2.4.4-RC

- Fixed list in camera editor (not loading properly ofter adding/editing camera)
- Fixed dialogs for editing prefix/suffix for chunk name creation


---

## `2022/12/30`

### 2.4.3-RC

- Fixed list in camera editor (not loading properly ofter adding/editing camera)
- Fixed camera Save/Edit functions in Camera Editor, so they are now saved with correct values


---

## `2022/12/29`

### 2.4.2-RC

- Added option `SubType` and `Resolution` to camera settings configuration (__cam_settings.ini__)
- Replaced easygui dialogs for Qt PySide2 custom dialog:
  - New Dialog Class: `class Ui_dialogChooseCamera()`

- Function definitions using new camera selection dialog:
  - Updated: `def cam_calibrationSettings()`
  - Updated: `def cam_calibrationChunk()`
  - Updated: `def newchunk_aero()`

- Updated camera list in Camera Editor to use new icons
- Updated `def appAbout()` to use PySide2 message box dialog


### 2.4.1-beta

- Replaced icon resorces to a more consistent themeing


---

## `2022/12/23`

### 2.4.0-beta

- Added more options to modify prefix/suffix for chunk names in New Chunk (2TIR)
- Fixed bug where script was in infinite loop when no project was present and user tried to load settings
- Reprogrammed default/current camera dialog to use PySide2 library instead of easygui


### 2.3.3-beta

- Added basic options to modify prefix/suffix for chunk names in New Chunk (2TIR)
- Settings for chunk name prefix/suffix are saved to settings file


### 2.3.2-beta

- Changed chunk naming format from prefix to suffix for following functions:
  - *New Chunk (2TIR)/STOPNICA (IZKOP)*
  - *New Chunk (2TIR)/STOPNICA (B.BET.)* 
- Removed redundant 'Project File' value from settings.


---

## `2022/12/18`

### 2.3.1-beta

- Updated resources
- Minor bux fix in menu icons


---

## `2022/12/18`

### 2.3.0-beta

- New settings per project module added


---

## `2022/12/11`

### 2.2.0-beta

- Major redesign for camera settings (no longer hard-coded)
- New camera settings configuration
- New 'Add Camera' function
- Better settings loading
- Improved settings reset code
- Bug fixes


---

## `2022/12/04`

### 2.1.1-beta

- Minor bug fixes in new chunk creation routines
- Updated README.md to include installation instructions
- Some file reorganization


---

## `2022/11/27`

### 2.1.0-beta

- New settings menu
- Settings loading process redesigned to be more consistent (still needs some polishing)
- Added new icons
- Added 'About AutoFTG' in menu
- Changed main 'New Chunk' method to give more options when creating chunk


---

## `2022/11/06`

### 2.0.x-beta

- Added basic settings menus
- New icons for menu items
- Completley rewritten routines for settings initialization and loading


---

## `2022/10/16`

### 1.7.6

- Reorder manus for default settings


---

## `2022/10/09`

### 1.7.5

- Added options to change default settings for:
  - Change default project folder
  - Change default camera calibration
  - Change default point filtering spacing
  - Change default point sampling


---

## `2022/09/25`

### 1.1

- Working version. First usable script.


---

## `2022/09/11`

### 1.0

- Initial version of AutoFTG
- Create chunk script


---

## Future ideas for improvements and upgrades

- [x] Options for modifiying chunk naming format (prefix/suffix)
- [ ] Importing multiple folders as chunks
- [ ] Write log of processed data to CSV or XLS/XLSX table
- [x] Replace easygui dialogs for Qt PySide2 (supported by Metashape)


