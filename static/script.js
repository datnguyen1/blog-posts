function showModalWindow(title) {
    // Get the modal element

    var modal = document.getElementById('modal-window');
    let h2 = document.getElementById('modal-title');
    let p = document.getElementById('modal-content');

    // Retrieve the title and content values from the <div> element
    let divElement = document.querySelector(`div[data-title="${title}"]`);
    let content = divElement.getAttribute('data-content');
    // Change the content of the h2 element
    h2.innerHTML = title;

    // Change the content of the h2 element
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
  

  