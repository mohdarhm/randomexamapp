document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.getElementById("expand-button");
    const menuModal = document.getElementById("menu-modal");
  
    menuToggle.addEventListener("click", function() {
      menuModal.style.display = "flex";
    });
  
    menuModal.addEventListener("click", function(event) {
      if (event.target === menuModal) {
        menuModal.style.display = "none";
      }
    });
  });
  
