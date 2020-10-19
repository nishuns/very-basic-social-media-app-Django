var check = 0;
document.addEventListener("DOMContentLoaded", () => {
  document.querySelector("#signup_profile").style.opacity = 0;

  var name = document.querySelector("#fullname");
  var username = document.querySelector("#username");
  var email = document.querySelector("#email");
  var password = document.querySelector("#password_one");
  var confirm_password = document.querySelector("#password_two");
  var dob = document.querySelector("#dob");

  document.querySelector("#validate").onclick = () => {
    if (name.value.length <= 0) {
      document.querySelector(".name_war").innerHTML = "/field is empty";
      check = 0;
    } else {
      check += 1;
    }

    if (username.value.length <= 0) {
      document.querySelector(".username_war").innerHTML = "/field is empty";
      check = 0;
    } else {
      check += 1;
    }

    if (email.value.length <= 0) {
      document.querySelector(".email_war").innerHTML = "/field is empty";
      check = 0;
    } else {
      check += 1;
    }

    if (password_one.value.length <= 0 && password_two.value.length <= 0) {
      document.querySelector(".password_war").innerHTML = "/field is empty";
      check = 0;
    } else {
      if (password_one.value == password_two.value) {
        check += 1;
      } else {
        document.querySelector(".password_war").innerHTML =
          "/Password doesn't match";
      }
    }

    if (check == 4) {
      document.querySelector("#signup_profile").style.opacity = 1;
    } else {
      check = 0;
    }
  };

});
