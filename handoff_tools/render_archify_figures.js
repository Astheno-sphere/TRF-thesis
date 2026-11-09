const { chromium } = require('playwright');
(async () => {
  const jobs = [
    ['.archify/architecture-system-map-20261031-020000/system-map.html', 'figures/fig1_1_system_map.png'],
    ['.archify/architecture-cei-mechanism-20261005/cei-mechanism.html', 'figures/fig4_1_cei_mechanism.png'],
    ['.archify/architecture-trf-artefact-20261005/trf-artefact.html', 'figures/fig5_1_trf_artefact.png'],
  ];
  const b = await chromium.launch();
  for (const [src, out] of jobs) {
    const p = await b.newPage({ viewport: { width: 1800, height: 1200 }, deviceScaleFactor: 3, colorScheme: 'light' });
    await p.goto('file://' + process.cwd() + '/' + src);
    await p.waitForTimeout(800);
    await p.evaluate(() => {
      document.querySelectorAll('[fill="url(#grid)"]').forEach(e => e.setAttribute('fill', '#FFFFFF'));
    });
    const svg = await p.$('svg');
    await svg.screenshot({ path: out });
    console.log(out);
    await p.close();
  }
  await b.close();
})();
