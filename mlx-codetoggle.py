# #############################################################################
#
# Adds "Show/hide code" toggle buttons to Matlab Live Script HTML files.
#
# USAGE
#
#   python mlx-codetoggle.py [-h] <FileIn> <FileOut>
#
# ARGS
#   FileIn - input Matlab Live Script HTML file name
#   FileOut - output HTML file name to write
#
# July 2018
# Brendan Hasz
# winsto99@gmail.com
# brendanhasz.github.io
# #############################################################################

import argparse
import re

# Command line arguments
p = argparse.ArgumentParser(description='Adds Show/hide code toggle buttons to Matlab Live Script HTML files')
p.add_argument("FileIn", help="Filename of the input Matlab Live Script HTML file")
p.add_argument("FileOut", nargs='?', default=None, help="Filename of the output file to write (with toggle buttons)")
args = p.parse_args()

# Load file
with open(args.FileIn, "r", encoding='utf-8') as f:
    I = f.read()

# Add show/hide javascript function after title tag
find1 = r'</title>'
repl1 = r"""</title>
    <script>
    function showhide(id) {
        var e = document.getElementById(id);
        e.style.display = (e.style.display == 'block') ? 'none' : 'block';
     }
     </script> 
"""
O = re.sub(find1, repl1, I)

# Move outputParagraph to its own div outside inlineWrapper outputs
find2 = r"""<div class = 'inlineWrapper outputs'>(.+?)<div class="outputParagraph"(.+?)</div></div></div>"""
repl2 = r"""<div class = 'inlineWrapper outputs'>\1</div></div><div class = 'inlineWrapper outputs'><div class="outputParagraph"\2</div></div></div>"""
O = re.sub(find2, repl2, O)

# Add show/hide button to all codeblocks
Ncb = 0 #number of codeblocks
find3 = r"""<div class = 'LineNodeBlock contiguous'>"""
def showhide_replace(match):
    global Ncb #number of code blocks
    Ncb = Ncb + 1 #increment
    return r"""<div class = "S3"><span class = "S2"><a href="javascript:showhide('codeblock"""+str(Ncb)+r"""')">Show/hide code</a></span></div>
    <div class = 'LineNodeBlock contiguous' id='codeblock"""+str(Ncb)+r"""' style="display:none;">"""
O = re.sub(find3, showhide_replace, O)

# Write to input file if output not specified
if args.FileOut is None:
    args.FileOut = args.FileIn

# Write output file
with open(args.FileOut, "w", encoding='utf-8') as f:
    f.write(O)
