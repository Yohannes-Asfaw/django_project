let data = document.getElementById("data");
let verification = document.getElementById("verification");

const request = new XMLHttpRequest();


// Full name validity checker
function check_fullname() {

  let fullname = document.getElementById('fullname').value;
  let help = document.querySelector('.help.fullname');

  help.innerText = "";

  if (fullname.length == 0) {
    help.innerText = "Name cannot be empty";
    return false;
  }

  return true;

}

// Username validity checker

function check_username() {

  let username = document.getElementById('username').value;
  let help = document.querySelector('.help.username');

  help.innerText = "";

  if (username.length < 5) {
    help.innerText = "A username must have at least 5 characters.";
    return false;
  }

  request.open("GET", `http://127.0.0.1:8000/checkusername?username=${username}`, false);
  request.send();

  response = JSON.parse(request.response);

  if (response.exists) {
    help.innerText = "Sorry, this username is already taken.";
    return false;
  }

  return true;

}

// Email validity checker

function check_email() {

  let email = document.getElementById('email').value;
  let help = document.querySelector('.help.email');

  help.innerText = "";

  request.open("GET", `http://127.0.0.1:8000/checkemail?email=${email}`, false);
  request.send();

  let response = JSON.parse(request.response)

  if (response.exists) {
    help.innerText = "Sorry, this email is already registered.";
    return false;
  }

  return true;
}


// Password validity checker

function check_password() {

  let password = document.getElementById('password');
  let confirm = document.getElementById('confirm');
  let help = document.querySelector('.help.password');

  help.innerText = "";

  if (!(password.value == confirm.value)) {
    help.innerText = "Your password doesn't match."
  }

  return password.value == confirm.value;
}



// Step 1: Check if all fields are good to go
// Step 2: Send the code to the email

let submit = document.getElementById("submit");

submit.addEventListener("click", (event) => {

  event.preventDefault();

  let name = check_fullname();
  let email = check_email();
  let password = check_password();
  let username = check_username();

  if (name && email && username && password) {

    data.style.display = 'none';
    verification.style.display = 'block';

    let name = document.getElementById("fullname").value;
    let email = document.getElementById("email").value;

    request.open("GET", `http://127.0.0.1:8000/sendcode?email=${email}&name=${name}`);
    request.send();
  }
});


// Verify whether or not the inserted code is correct

let verify = document.getElementById('verify');

verify.addEventListener('click', (event) => {

  let code = document.getElementById("code").value;
  let email = document.getElementById("email").value;
  let help = document.querySelector('.help.verification');

  request.open("GET", `http://127.0.0.1:8000/checkcode?email=${email}&code=${code}`, false);
  request.send();

  let response = JSON.parse(request.response)

  if (!response.is_correct) {
    event.preventDefault();
    help.innerText = "The code you entered is incorrect";
    return;
  }
});