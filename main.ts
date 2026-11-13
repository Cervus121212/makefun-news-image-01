// news-image-01 entrypoint.
// Copies the pre-rendered entry image next to this file into the
// harness output directory, unchanged. Nothing else happens here.

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const sourceImage = join(here, "entry.png");

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outputDir, { recursive: true });

copyFileSync(sourceImage, join(outputDir, "entry.png"));
