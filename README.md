<br/>
<div align="center">
  <div align="center">
    <img src="./assets/program.png" width="800">
  </div>
  <h1 align="center">🚀RoR save editor</h1>
  <div align="center">Risk of Rain Returns save file editor.</div>
</div>
<br/>

## 🗃️About The Project
Originally this project was a development of the program by [PhoenixRem1x](https://github.com/PhoenixRem1x/RoRR-Save-Editor), but later it was completely redesigned and supplemented by the [gameplay.tips guide](https://gameplay.tips/guides/risk-of-rain-returns-unlock-characters-and-abilities-through-save-file-cheat-mode.html).

## 🔌How To Use
1. Go to `\Steam\userdata\(random folder name)\1337520\remote`
2. Download portable exe file from the [`releases page`](https://github.com/markell/ror_save_editor/releases) and put the program in a folder mentioned above or choose save file from the program file picker.
3. Run the program 

> ⚠️ When you enter the game, all relevant Steam Achievements will be completed.


##  🧰Requirements
- python3
- [beaupy](https://github.com/petereon/beaupy/)
- Tkinter 

## 🔨 How to build

```sh
git clone https://github.com/markell/ror_save_editor.git
poetry build
pip install ./dist/ror_save_editor-{{some-version}}-py3-none-any.whl
```

### 📋Plans To Do
- [ ] Game wiki link system
- [ ] Translation to all in-game languages
- [ ] Original Risk of Rain game support

## 🤔Problems/New Features?
This is my first Python project, so various bugs are possible.
Feel free to ask for support [here](https://github.com/markell/ror_save_editor/issues).