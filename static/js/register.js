// Get the select element
var selectElement = document.getElementById("school");

// Create the disabled option element
var disabledOption = document.createElement("option");
disabledOption.value = "";
disabledOption.text = "Please select an option";
disabledOption.disabled = true;
disabledOption.selected = true;

// Add the disabled option as the first option
selectElement.insertBefore(disabledOption, selectElement.firstChild);

// Get the radio buttons
var radioOne = document.getElementById("radioOne");
var radioTwo = document.getElementById("radioTwo");

// Get the div elements
var emailDiv = document.querySelector(".email-input");
var schoolDiv = document.querySelector(".school-select");
var footerDiv = document.querySelector(".footer");
var registerDiv = document.querySelector(".register");
var passwordDiv = document.querySelector(".password-input");
var nameDiv = document.querySelector(".name-input");
var schoolNameDiv = document.querySelector(".school-name");

function toggleElementVisibility(element, isVisible) {
  if (isVisible) {
    element.style.display = "block";
  } else {
    element.style.display = "none";
  }
}
function resetElementValues(...elements) {
  elements.forEach((element) => {
    element.value = "";
  });
}
function resetClassName(...elements) {
  elements.forEach((element) => {
    element.className = "validate";
  });
}

function handleRadioOneSelection() {
  toggleElementVisibility(emailDiv, true);
  toggleElementVisibility(schoolDiv, true);
  toggleElementVisibility(footerDiv, true);
  toggleElementVisibility(registerDiv, true);
  toggleElementVisibility(schoolNameDiv, false);
  toggleElementVisibility(passwordDiv, true);
  toggleElementVisibility(nameDiv, true);

  document.getElementById("firstName").required = true;
  document.getElementById("otherNames").required = true;
  document.getElementById("schoolName").required = false;

  resetElementValues(
    document.getElementById("firstName"),
    document.getElementById("otherNames"),
    document.getElementById("schoolName"),
    document.getElementById("emailInput"),
    document.getElementById("password"),
    document.getElementById("password2")
  );
  resetClassName(
    document.getElementById("emailInput"),
    document.getElementById("schoolName"),
    document.getElementById("password"),
    document.getElementById("password2"),
  )
}

function handleRadioTwoSelection() {
  toggleElementVisibility(emailDiv, true);
  toggleElementVisibility(schoolNameDiv, true);
  toggleElementVisibility(schoolDiv, false);
  toggleElementVisibility(footerDiv, true);
  toggleElementVisibility(registerDiv, true);
  toggleElementVisibility(passwordDiv, true);
  toggleElementVisibility(nameDiv, false);

  document.getElementById("firstName").required = false;
  document.getElementById("otherNames").required = false;
  document.getElementById("schoolName").required = true;

  resetElementValues(
    document.getElementById("firstName"),
    document.getElementById("otherNames"),
    document.getElementById("schoolName"),
    document.getElementById("emailInput"),
    document.getElementById("password"),
    document.getElementById("password2"),
    document.getElementById("school")
  );
  resetClassName(
    document.getElementById("firstName"),
    document.getElementById("otherNames"),
    document.getElementById("emailInput"),
    document.getElementById("schoolName"),
    document.getElementById("password"),
    document.getElementById("password2"),
  )
}

// Add event listener to radioOne
radioOne.addEventListener("click", handleRadioOneSelection);

// Add event listener to radioTwo
radioTwo.addEventListener("click", handleRadioTwoSelection);
