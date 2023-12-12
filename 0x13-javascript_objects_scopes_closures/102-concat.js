#!/usr/bin/node

const fs = require('fs/promises');
const [source1, source2, destination] = process.argv.slice(2);

(async () => {
  try {
    const data1 = await fs.readFile(source1, 'utf8');
    const data2 = await fs.readFile(source2, 'utf8');
    const combinedData = data1 + data2;
    await fs.writeFile(destination, combinedData);
    console.log('Files successfully concatenated to:', destination);
  } catch (err) {
    console.error('Error:', err);
  }
})();
