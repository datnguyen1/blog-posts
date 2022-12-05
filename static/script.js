function showModalWindow(id) {
    // Get the modal element
    var modal = document.getElementById('modal-window');
    let h2 = document.getElementById('modal-title');
    let p = document.getElementById('modal-content');

    // Retrieve the <div> element using the id attribute
    let divElement = document.getElementById(id);

    // Retrieve the title and content values from the <div> element
    let title = divElement.getAttribute('data-title');
    let content = divElement.getAttribute('data-content');

    // Change the content of the h2 and p elements
    h2.innerHTML = title;
    p.innerHTML = content;

    // Set the modal's display property to "block" to show it
    modal.style.display = "block";
  }

  
  function unshowModalWindow() {
    // Get the modal element
    var modal = document.getElementById('modal-window');

    // Set the modal's display property to "none" to hide it
    modal.style.display = "none";
  }
  

  