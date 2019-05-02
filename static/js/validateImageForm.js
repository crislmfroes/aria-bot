const form = document.querySelector('#image-form');
form.addEventListener('submit', e => {
    imageFile = document.querySelector('#fileInput');
    if (imageFile.files.length !== 1) {
        //e.preventDefault();
        console.error('Você só pode fazer upload de 1 imagem.');
    }
    const formats = ['png', 'jpg'];
    if (formats.indexOf(imageFile.files[0].name.split('.')[1]) == -1) {
        //e.preventDefault();
        console.error('Você deve fazer upload de 1 imagem no formato .png ou .jpg');
    }
});