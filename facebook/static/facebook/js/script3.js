document.addEventListener("DOMContentLoaded", () => {
  window.onscroll = () => {
    console.log(window.scrollY);
    if (window.scrollY > 150) {
        
        document.querySelector(".loggers_block").style.position="fixed";
      document.querySelector(".loggers_block").style.top="-8%";
    }
    else{
        document.querySelector(".loggers_block").style.position="relative";
    }
  };
});
