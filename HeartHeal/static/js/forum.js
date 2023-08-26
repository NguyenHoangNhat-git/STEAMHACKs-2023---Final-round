document.querySelector('#comment-input').focus();
document.querySelector('#comment-input').onkeyup = function(e) {
    if (e.key === 'Enter') { 
        document.querySelector('#comment-submit').click();
    }
};

const upload_input = document.getElementById('upload-input-fake');
const upload_button = document.getElementById('upload-btn-fake');
upload_input.addEventListener('focus', function() {
    upload_button.click();
});


const checkbox = document.getElementById('like');
const button = document.getElementById('like-submit');
checkbox.addEventListener('change', function() {
    button.click();
});


const form_file = document.getElementById('upload-form-file');
const form_file_name = document.getElementById('upload-form-file-name');
form_file.addEventListener('change', function() {
    filename = form_file.files[0].name;
    form_file_name.innerText = filename;
});

