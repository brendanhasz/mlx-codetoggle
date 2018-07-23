# mlx-codetoggle

Adds "Show/hide code" buttons to Matlab Live Script output HTML files.  [Matlab Live Scripts](http://www.mathworks.com/help/matlab/matlab_prog/what-is-a-live-script-or-function.html) are basically Matlab's take on the Jupyter notebook.  But when you output them as HTML files, there is no way to get a toggle button which shows/hides the code blocks.  The python script `mlx-codetoggle.py` in this repository adds buttons to each codeblock to toggle the visibility of that codeblock.

## Usage

If you have an HTML file `input.html` which was exported from a Matlab Live Script, to save a copy of that file with code block toggle buttons to `output.html`, run:

```
python mlx-codetoggle.py input.html output.html
```

Copyright (c) 2018 Brendan Hasz

Licensed under the MIT License

