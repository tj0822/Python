var uploader = new plupload.Uploader({
    multipart: false,
    chunk_size: "1mb",

    url: "/file_upload",
    browse_button: 'browse’
});