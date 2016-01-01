var serialport = require("serialport");
var SerialPort = serialport.SerialPort;

var serialport = new SerialPort("/dev/ttyACM0", {baudrate: 9600, parser: serialport.parsers.readline("\r\n")});
serialport.on('open', function(){
	console.log('Serial Port Opend');
	serialport.on('data', function(data){
		console.log('ok');
		console.log(data[0]);
	});
});
