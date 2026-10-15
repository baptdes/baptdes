"""Generate dark_mode.svg / light_mode.svg for the profile README.

Static, stdlib only. Edit info_lines() below, then run: python3 update_profile.py
"""
import html

USER = "baptdes"
W = 56  # info column width in characters

ART = r"""
          .   ,               
       '. '.  \  \            
      ._ '-.'. `\  \          
        '-._; .'; `-.'.       
       `~-.; '.       '.      
        '--,`           '.    
           -='.          ;    
 .--=~~=-,    -.;        ;    
 .-=`;    `~,_.;        /
`  ,-`'    .-;         |         
   .-~`.    .;         ;         
    .;.-   .-;         ,\        
      `.'   ,=;     .-'  `~.-._
       .';   .';  .'      .'   '-.     
          .\  ;  ;        ,.' _  a',   
         .'~";-`   ;      ;"~` `'-=.) 
       .' .'   . _;  ;',  ;
       '-.._`~`.'  \  ; ; :          
            `~'    _'\\_ \\_         
                  /=`^^=`""/`)-.     
                  \ =  _ =     =\    
                   `""` `~-. =   ;  
"""

PALETTES = {
    "dark": {"bg": "#0d1117", "border": "#30363d", "art": "#8b949e", "h": "#58a6ff",
             "k": "#ffa657", "v": "#c9d1d9", "d": "#484f58", "g": "#3fb950", "r": "#f85149"},
    "light": {"bg": "#ffffff", "border": "#d0d7de", "art": "#57606a", "h": "#0969da",
              "k": "#953800", "v": "#24292f", "d": "#afb8c1", "g": "#1a7f37", "r": "#cf222e"},
}


def kv(key, val, width=W):
    dots = "." * max(width - len(key) - len(str(val)) - 3, 1)
    return [(f"{key}: ", "k"), (dots + " ", "d"), (str(val), "v")]


def rule(title=""):
    label = f"─ {title} " if title else ""
    return [(label, "h"), ("─" * (W - len(label)), "d")]


def info_lines():
    return [
        [(f"{USER.lower()}@github ", "h"), ("─" * (W - len(USER) - 8), "d")],
        [],
        kv("OS", "Windows, Linux (Fedora, Ubuntu)"),
        kv("Host", "Celad"),
        kv("Role", "Data scientist / AI Engineer"),
        kv("IDE", "VS Code"),
        [],
        kv("Languages.Programming", "Python, Java, C++"),
        kv("Languages.Real", "French, English"),
        kv("Hobbies", "Video games, Cycling, Crafting"),
        [],
        rule("Contact"),
        kv("Email", "baptiste.desnouck@gmail.com"),
        kv("LinkedIn", "in/baptiste-desnouck"),
    ]


def render(mode):
    p = PALETTES[mode]
    art = ART.strip("\n").split("\n")
    info = info_lines()
    h = max(40 + len(art) * 15, 45 + len(info) * 21) + 10
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="840" height="{h}" viewBox="0 0 840 {h}" '
        'font-family="Consolas, Menlo, monospace" font-size="13px">',
        f'<rect x="0.5" y="0.5" width="839" height="{h - 1}" rx="10" fill="{p["bg"]}" stroke="{p["border"]}"/>',
    ]
    for i, line in enumerate(art):
        out.append(f'<text x="25" y="{40 + i * 15}" fill="{p["art"]}" xml:space="preserve">{html.escape(line)}</text>')
    for i, segs in enumerate(info):
        if not segs:
            continue
        spans = "".join(f'<tspan fill="{p[c]}">{html.escape(t)}</tspan>' for t, c in segs)
        out.append(f'<text x="390" y="{45 + i * 21}" xml:space="preserve">{spans}</text>')
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    for mode in PALETTES:
        with open(f"{mode}_mode.svg", "w", encoding="utf-8") as f:
            f.write(render(mode))
    print("wrote dark_mode.svg, light_mode.svg")
