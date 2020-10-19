document.addEventListener("DOMContentLoaded", () => {

  document.querySelector(".icon").onclick = () => {
    var nav = document.querySelector(".menu");
    nav.style.display = "flex";
    nav.style.animation = "move_in 1s 1 forwards";
    document.querySelector(".close").onclick = () => {
      nav.style.animation = "move_out 4s 1 forwards";

      document.querySelector(".icon").style.display = "block";
    };
  };


  var request = new XMLHttpRequest();
  request.open("GET", "/online");
  request.onload = () => {
    var data = request.responseText;
    console.log(data);
    if (data == "login") {
      document.querySelector(".loggers_block").style.display = "flex";
      document.querySelector(".signout").style.display="block";
      document.querySelector(".visited").innerHTML="Profile";

    } else {
      document.querySelector(".loggers_block").style.display = "none";
      document.querySelector(".signout").style.display="none";
    }
  };
  request.send();

  document.querySelector(".logout").onclick = () => {
    const request = new XMLHttpRequest();
    request.open("GET", "/logout");
    request.onload = () => {
      const response = request.responseText;
      document.querySelector(".loggers_block").style.display = "none";
      alert("Log out Sucessfully ");
    };
    request.send();
    return false;
  };

  return false;
});
