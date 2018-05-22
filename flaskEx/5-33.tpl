var uploader = new plupload.Uploader({
    browse_button: 'browse',
    url: '/file_upload’,
    file_data_name: 'attach'
});

uploader.init();