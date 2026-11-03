const fs = require('fs');
const path = require('path');

const srcDir = path.join(__dirname, 'public');
const distDir = path.join(__dirname, 'dist');

console.log('Building Haworth Industrial Technologies static site...');

if (!fs.existsSync(srcDir)) {
  console.error(`Error: Source directory '${srcDir}' does not exist.`);
  process.exit(1);
}

if (fs.existsSync(distDir)) {
  fs.rmSync(distDir, { recursive: true, force: true });
}

fs.mkdirSync(distDir, { recursive: true });
fs.cpSync(srcDir, distDir, { recursive: true });

console.log(`Build successful! Static files copied from public to dist.`);
