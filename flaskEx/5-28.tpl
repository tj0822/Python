uploader.bind('FilesAdded', function(up, files) {
    var html = '';
    plupload.each(files, function(file) {
        html += '<li id="' + file.id + '">' + file.name + ' (' + plupload.formatSize(file.size) + ') <b></b></li>';
    });
    document.getElementById('filelist').innerHTML += html;
});