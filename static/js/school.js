document.addEventListener("DOMContentLoaded", function () {
  var countryField = document.getElementById("id_country");
  var stateField = document.getElementById("id_state");

  // Disable the state field initially
  stateField.disabled = true;
  stateField.required = false;

  var countryDefaultOption = document.createElement("option");
  var stateDefaultOption = document.createElement("option");
  countryDefaultOption.text = "Select Country";
  countryDefaultOption.disabled = true;
  countryDefaultOption.selected = true;
  stateDefaultOption.text = "Select State";
  stateDefaultOption.disabled = true;
  stateDefaultOption.selected = true;
  countryField.add(countryDefaultOption, countryField.options[0]);
  stateField.add(stateDefaultOption, stateField.options[0]);

  countryField.addEventListener("change", function () {
    var countryId = this.value;

    // Clear existing options
    stateField.innerHTML = "";

    if (countryId !== "") {
      // Enable the state field
      stateField.disabled = false;

      // Fetch the related states for the selected country
      fetch("/get_states/" + countryId + "/")
        .then((response) => response.json())
        .then((data) => {
          // Check if the returned JSON is empty
          if (data.length === 0) {
            // Set the state select to an empty string value
            stateField.value = "";
            stateField.setAttribute("novalidate", true);
          } else {
            // Sort the states alphabetically by name
            data.sort((a, b) => a.name.localeCompare(b.name));

            // Create new options for each state and append them to the state field
            data.forEach((state) => {
              var option = document.createElement("option");
              option.value = state.name;
              option.text = state.name;
              stateField.appendChild(option);
            });

            // Remove the "novalidate" attribute if it was set previously
            stateField.removeAttribute("novalidate");
          }
        });
    } else {
      // Disable the state field if no country is selected
      stateField.disabled = true;
      stateField.removeAttribute("novalidate");
    }
  });

  // Function to sort select options alphabetically
  function sortSelectOptions(selectId) {
    var selectElement = document.getElementById(selectId);
    var optionList = Array.from(selectElement.options);

    optionList.sort((a, b) => a.text.localeCompare(b.text));

    optionList.forEach((option) => {
      selectElement.add(option);
    });
  }

  // Sort the state options alphabetically
  sortSelectOptions("id_state");

  // Form submission event listener
  var form = document.getElementById("school-form");
  form.addEventListener("submit", function (event) {
    // Check if the stateField value is an empty string
    if (stateField.value === "") {
      // Set the stateField value to null or an empty string
      stateField.value = ""; // or stateField.value = null;
    }
  });
});
