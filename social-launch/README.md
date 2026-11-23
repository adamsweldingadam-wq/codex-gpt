# Adams Welding: social launch kit

Brand pictures and profile copy for the new Instagram, Threads, X, TikTok, YouTube and Nextdoor accounts (Nov 2026).

- `images/`: final files. Profile picture 800×800, X header 1500×500, YouTube banner 2560×1440, three Instagram launch posts at 1080×1350.
- `copy.json`: bios, names and launch posts for each platform. `copy.py` rebuilds it and checks every character limit and the Playbook's banned phrases.
- `generator/`: re-renders the pictures. Run `node generator/render.js` (Playwright + Chromium). Pass an asset name (`profile`, `xheader`, `youtube`, `ig1`, `ig2`, `ig3`) to render just one. Text lives in `generator/art.html`.

Fonts: Oswald and Open Sans (SIL Open Font License), the same faces as adamswelding.net. Logo: `generator/icon-512.png` from adamswelding.net.

Posting is handled by the content engine (monday Daily Content Calendar + the Runbook in Google Drive, section M). This folder only holds the launch assets.
