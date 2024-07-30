const fs = require('fs');

try {
  let data = fs.readFileSync(process.argv[2], 'utf8');
  console.log(data);
}
catch (e) {
  console.error(e);
}
