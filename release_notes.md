# Release Notes

Release notes for AutoFTG python script


---

## `2022/09/11`

### 1.0

- Initial version of AutoFTG
- Create chunk script


---

## `2022/09/25`

### 1.1

- Working version. First usable script.


---

## `2022/10/09`

### 1.7.5

- Added options to change default settings for:
  - Change default project folder
  - Change default camera calibration
  - Change default point filtering spacing
  - Change default point sampling


---

## `2022/10/16`

### 1.7.6

- Reorder manus for default settings


---

## `2022/11/06`

### 2.0.x-beta

- Added basic settings menus
- New icons for menu items
- Completley rewritten routines for settings initialization and loading


---

## `2022/11/27`

### 2.1.0-beta

- New settings menu
- Settings loading process redesigned to be more consistent (still needs some polishing)
- Added new icons
- Added 'About AutoFTG' in menu
- Changed main 'New Chunk' method to give more options when creating chunk


---

## `2022/12/04`

### 2.1.1-beta

- Minor bug fixes in new chunk creation routines
- Updated README.md to include installation instructions
- Some file reorganization


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

## `2022/12/18`

### 2.3.0-beta

- New settings per project module added

---

## `2022/12/18`

### 2.3.1-beta

- Updated resources
- Minor bux fix in menu icons

---

## `2022/12/23`

### 2.3.2-beta

- Changed chunk naming format from prefix to suffix for following functions:
  - *New Chunk (2TIR)/STOPNICA (IZKOP)*
  - *New Chunk (2TIR)/STOPNICA (B.BET.)* 
- Removed redundant 'Project File' value from settings.


### 2.3.3-beta

- Added basic options to modify prefix/suffix for chunk names in New Chunk (2TIR)
- Settings for chunk name prefix/suffix are saved to settings file


### 2.4.0-beta

- Added more options to modify prefix/suffix for chunk names in New Chunk (2TIR)
- Fixed bug where script was in infinite loop when no project was present and user tried to load settings
- Reprogrammed default/current camera dialog to use PySide2 library instead of easygui


---

## Future ideas for improvements and upgrades

- [x] Options for modifiying chunk naming format (prefix/suffix)
- [ ] Importing multiple folders as chunks
- [ ] Write log of processed data to CSV or XLS/XLSX table


---

## `2022/12/28`

### 2.4.1-beta

- Replaced icon resorces to a more consistent themeing

