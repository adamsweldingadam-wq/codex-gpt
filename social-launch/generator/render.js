const { chromium } = require('playwright');
const path = require('path');
const SIZES = { profile: [800, 800], xheader: [1500, 500], youtube: [2560, 1440], ig1: [1080, 1350], ig2: [1080, 1350], ig3: [1080, 1350] };
const OUT = {
  profile: 'adams-profile-800.png',
  xheader: 'adams-header-x-1500x500.jpg',
  youtube: 'adams-banner-youtube-2560x1440.jpg',
  ig1: 'adams-ig-launch-1-bins-beads-bearings-booms.jpg',
  ig2: 'adams-ig-launch-2-four-trades.jpg',
  ig3: 'adams-ig-launch-3-on-call-24-7.jpg',
};
(async () => {
  const which = process.argv.slice(2);
  const list = which.length ? which : Object.keys(SIZES);
  const browser = await chromium.launch();
  for (const a of list) {
    const [w, h] = SIZES[a];
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    await page.goto('file://' + path.join(__dirname, 'art.html') + '?a=' + a);
    await page.waitForSelector('body[data-ready="1"]');
    await page.waitForTimeout(300);
    const file = path.join(__dirname, '..', 'images', OUT[a]);
    const opts = { path: file, clip: { x: 0, y: 0, width: w, height: h } };
    if (file.endsWith('.jpg')) { opts.type = 'jpeg'; opts.quality = 92; }
    await page.screenshot(opts);
    console.log('wrote', OUT[a]);
    await page.close();
  }
  await browser.close();
})();
