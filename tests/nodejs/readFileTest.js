fs = require('fs')

setInterval(function() {
fs.readFile('../DGIPyDrOnePY/lastProperties.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
}, 250);
