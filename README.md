# This is a fork of the orignal repo that is used to generate replays I can use for machine learning

# Installing

```
cd osr2mp4/
python install.py
pip install cython
cd ImageProcess/Curves/libcurves/
python setup.py build_ext --inplace
```

To enable ffmpeg video writer:

```
cd VideoProcess/FFmpegWriter/
python setup.py build_ext --inplace
```

Then

### Pillow-SIMD

Download Pillow-SIMD here
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow-simd

Install pillow-simd
`pip install download-file.whl`

### ffmpeg

Download ffmpeg here:
https://www.ffmpeg.org/download.html#build-windows

# Usage

```bash
python main.py "Osu! Directory" "Skin Directory" "Map File (i.e. the .osu)"
```
