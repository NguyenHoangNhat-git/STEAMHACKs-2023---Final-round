document.querySelector('#module-textfield').addEventListener('click', function() {
    var slidingDiv = this.querySelector('#module-document');
    slidingDiv.style.display = slidingDiv.style.display === 'none' ? 'block' : 'none';
});

document.querySelector('#module-videofield').addEventListener('click', function() {
    var slidingDiv = this.querySelector('#module-video');
    slidingDiv.style.display = slidingDiv.style.display === 'none' ? 'block' : 'none';
});


