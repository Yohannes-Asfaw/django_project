let input_image = document.getElementById('input_image');
let input_icon = document.getElementById('input_icon');
let profile_picture = document.getElementById('profile_picture');

input_icon.addEventListener('click', () => {
    input_image.click();
})

input_image.addEventListener('change', () => {
    let reader = new FileReader();

    reader.readAsDataURL(input_image.files[0]);

    reader.onload = function () {
        profile_picture.src = reader.result; 
    };
})