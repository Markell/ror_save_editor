<br/>
<div align="center">
  <div align="center">
    <img src="./assets/program.png" width="800">
  </div>
  <h1 align="center">RoR save editor</h1>
  <div align="center">Risk of Rain Returns save file editor.</div>
</div>
<br/>

## About The Project
Initially this project was a development of the program by [PhoenixRem1x](https://github.com/PhoenixRem1x/RoRR-Save-Editor), but later it was completely redesigned and supplemented by [gameplay.tips guide](https://gameplay.tips/guides/risk-of-rain-returns-unlock-characters-and-abilities-through-save-file-cheat-mode.html).

## Compatibility
Editor works with Windows 10/11 only and tested on game version `1.0.4`.

## Requirements
- python3
- [beaupy](https://github.com/petereon/beaupy/)
- Tkinter 

## Installation
Download portable exe file from [`releases page`](https://github.com/markell/ror_save_editor/releases)

From source:

```sh
git clone https://github.com/markell/ror_save_editor.git
poetry build
pip install ./dist/ror_save_editor-{{some-version}}-py3-none-any.whl
```

### To Do
- [ ] Game wiki link system
- [ ] Translation to all in game languages
- [ ] Original Risk of Rain game support

## Problems/New Features?
This is my first python project, various bugs are possible.
In any case, ask for support [here](https://github.com/markell/ror_save_editor/issues).
