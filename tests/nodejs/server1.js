var io = require('socket.io')(8081);
//io.set('origins', 'http://192.168.95.34:8081');
io.set('origins', '*domain.com*:*');

var exec = require('child_process').exec;

var fs = require('fs');

console.log('server started');

io.on('connection', function (socket) {
    console.log('new connection');

    setInterval(function () {
        fs.readFile('../DGIPyDrOnePY/lastProperties.txt', 'utf8', function (err, data) {
            if (err) {
                return console.log(err);
            }
            socket.emit('news', data);
        });
    }, 250);

    socket.on('command', function (data) {
        console.log(data);

        exec('./test.sh "' + data + '"',
            function (error, stdout, stderr) {
                console.log('stdout: ' + stdout);
                console.log('stderr: ' + stderr);
                if (error !== null) {
                    console.log('exec error: ' + error);
                }
            });
    });

    socket.on('disconnect', function () {
        console.log('disconnect device');
    });
});
