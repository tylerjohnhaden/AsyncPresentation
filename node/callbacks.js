var fs = require('fs');

function read(file) {
    var myData = null;
    fs.readFile('text.txt', "utf8", function(err, data) {
        myData = err ? 'error' : data;
    });

    // returns before myData is updated
    return myData;
}

var result = read('text.txt');
console.log(result);

// must write code inside callbacks

function readCallback(file, callback) {
    fs.readFile('text.txt', "utf8", function(err, data) {
        callback(err ? 'error' : data);
    });
}

readCallback('text.txt', function (m) {
    console.log(m);
});