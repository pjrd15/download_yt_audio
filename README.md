# download_yt_audio
Small program made to extract the audio from a Youtube video/playlist, using yt_dlp for the download/extraction and PyQt5 for the GUI.

## Instalation
Download and install Python 3.11.8 :<br>
https://www.python.org/downloads/release/python-3118/<br><br>
Clone the repository:<br>
```git clone https://github.com/pjrd15/download_yt_audio.git```<br><br>
Change into the Directory:<br>
```cd download_yt_audio```<br><br>
Create a python3 Virtual enviroment inside the repo:<br>
```python3 -m venv .env```<br><br>
Then activate it:<br>
```source path/to/file/download_yt_audio/.env/bin/activate```<br><br>
Now install the requirements:<br>
```pip3 install -r requirements.txt```

## Usage
Change the diretory to 'main':<br>
```cd main```<br><br>
Run:<br>
```python3 main.py```<br><br>
Paste the Youtube link on the field (it can be a single video or playlist)<br>
select the format and click on download.<br><br>
If you get stuck on 'Preparing wheel metadata' use:<br>
```pip3 install --upgrade pip```<br>
and then install the requirements again
