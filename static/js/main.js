// Navbar background color change on scroll
window.addEventListener("scroll", function () {
  const navbar = document.querySelector(".navbar");
  navbar.classList.toggle("scrolled", window.scrollY > 0);
});
// Get both "Sign Up Now" buttons
const signUpButtons = document.querySelectorAll(".text-center .btn");

// Add a click event listener to each button
signUpButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    // Create the modal element
    const modal = document.createElement("div");
    modal.classList.add("modal");

    // Create the modal content
    const modalContent = `
<div class="modal-content">
<h3>Are you creating an for an</h3>
<label><input type="radio" name="role" value="individual"> Individual</label>
<label><input type="radio" name="role" value="instuition"> Higher Instuition</label>
<button class="btn btn-primary" id="modalSubmit">Submit</button>
</div>
`;

    // Set the modal content
    modal.innerHTML = modalContent;

    // Append the modal to the body
    document.body.appendChild(modal);

    // Get the modal content
    const modalContentElement = modal.querySelector(".modal-content");

    // Add a click event listener to the modal content to prevent event bubbling
    modalContentElement.addEventListener("click", function (event) {
      event.stopPropagation();
    });

    // Close the modal when clicking outside the modal content
    modal.addEventListener("click", function () {
      document.body.removeChild(modal);
    });

    // Get the submit button inside the modal
    const modalSubmitButton = modal.querySelector("#modalSubmit");

    // Add a click event listener to the submit button
    modalSubmitButton.addEventListener("click", function () {
      // Get the selected role
      const selectedRole = modal.querySelector('input[name="role"]:checked');

      // Redirect based on the selected role
      if (selectedRole && selectedRole.value === "individual") {
        window.location.href = "/register/user/";
      } else if (selectedRole && selectedRole.value === "instuition") {
        window.location.href = "/register/school/";
      }
    });
  });
});
