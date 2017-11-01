var fs = require('fs');

function readPromise(file) {
    return new Promise(function(resolve, reject) {
        fs.readFile(file, "utf8", function(err, data) {
            if (err) {
                reject('error');
            } else {
                resolve(data);
            }
        });
     });
}

readPromise('text.txt').then(function (m) {
    // normal execution
    console.log(m);
}, function (e) {
    // catch error
    console.log(e);
});


// chaining
readPromise('text.txt')
    // see how much more beautiful this is
    .then(m => console.log(m))

    // second process
    .then(m => console.log(undefinedFunction(m)))

    // catches original 'reject' and subsequent errors
    .catch(e => console.log(e));
