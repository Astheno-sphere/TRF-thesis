#!/usr/bin/env python3
"""Render an Archify diagram HTML to a high-resolution PNG (3x), hiding the viewer toolbar.
    python3 handoff_tools/render_figure.py <abs path to .html> <abs path to .png>
Needs playwright and Chromium at /opt/pw-browsers/chromium-1194 (adjust executable_path elsewhere)."""
import sys
from playwright.sync_api import sync_playwright
src, out = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width':1600,'height':1800}, device_scale_factor=3, color_scheme='light')
    pg.goto('file://'+src); pg.wait_for_timeout(800)
    pg.evaluate("""()=>{for(const e of document.querySelectorAll('body *')){const s=getComputedStyle(e);if(s.position==='fixed'||s.position==='sticky')e.style.display='none';}}""")
    pg.wait_for_timeout(200)
    pg.query_selector('svg').screenshot(path=out)
    b.close()
