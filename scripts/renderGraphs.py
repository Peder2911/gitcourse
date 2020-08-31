
import re
import sys
import os
import subprocess

SIGNIFIER = ",,,"
START = f"^{SIGNIFIER}graph"

COMMAND = (
        "dot -Tpng -Gsize={width},{height}\\! -layout=fdp -Gbgcolor='transparent' -Gdpi=8"
        " |openssl base64"
    )

cmd = lambda h,w: COMMAND.format(
        height=int(int(h)/2),width=int(int(w)/2),
        cheight=h,cwidth=w
        )

HEIGHT,WIDTH = 400,600

def renderGraphLines(lines,height,width):
    raw = "\n".join(lines)
    p = subprocess.Popen(cmd(height,width),
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            shell = True)
    imgData,*_ = p.communicate("\n".join(lines).encode())
    return (
            '<div class="graphcontainer">'
            f'<img class="graph" src="data:image/png; base64,{imgData.decode()}"'
            f'style="max-height:{height}px;max-width:{width}px">'
            '</div>'
        )

def scan(raw:str)->str:
    outlines = []
    graph = []
    readingGraph = False
    for ln in raw.split("\n"):

        if not readingGraph:
            if re.search(START,ln.strip()):
                readingGraph = True
                hw = re.search("(?<=\{)[0-9]+,[0-9]+(?=\})",ln)
                if hw:
                    height,width = hw[0].split(",")
                else:
                    height,width = HEIGHT,WIDTH
            else:
                outlines.append(ln)
        else:
            if ln.strip() == SIGNIFIER:
                readingGraph = False
                outlines.append(renderGraphLines(graph,height,width))
                graph = []
            else:
                graph.append(ln)

    return "\n".join(outlines)

if __name__  == "__main__":
    sys.stdout.write(scan(sys.stdin.read()))

