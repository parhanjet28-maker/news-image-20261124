// news-image-20261124 entry (Node 22, standard library only).
// The entry image is the front page in this repository (entry.png,
// drawn by draw.py from the day's news); this program copies it to
// the output directory as /output/entry.png.
// Local check: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(
  new URL('./entry.png', import.meta.url),
  join(outDir, 'entry.png'),
);
