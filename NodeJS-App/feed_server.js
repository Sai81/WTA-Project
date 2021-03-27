const spawn = require("child_process").spawn;

const pythonProcess = spawn('python3',["getting_feed.py"]);
pythonProcess.stdout.on('data',(data) => {

	mystr = data.toString();
	myjson = JSON.parse(mystr);
	console.log('JSON IS : ${myjson}');
	//console.log(myjson.Data);
	console.log(myjson.Message);


});