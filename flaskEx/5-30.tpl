uploader.bind('Error', function(up, err) {
    document.getElementById('console').innerHTML += "\nError #" + err.code + ": " + err.message;
}); 