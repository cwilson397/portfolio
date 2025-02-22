// form-demo.js

function validateForm(event) {
    // Get a reference to the form. Since we attached a submit event listener to the form,
    // we can access the form either through event.target or "this"
    const theForm = event.target;
    // The default behavior for a form submit is to navigate to another page where the form is processed.
    // To prevent that (if we have invalid data), we call event.preventDefault().
    // We will store error messages in an array.
    const errors = [];
    // Start by assuming the form is valid.
    let isValid = true;
    
    // Validation: If payment method is credit card, check the credit card number.
    if (theForm.paymentMethod.value === "creditCard") {
      // Normally, we would contact the credit card company to verify the number.
      // For simplicity, we only allow one valid credit card number.
      if (theForm.creditCardNumber.value !== "1234123412341234") {
        isValid = false;
        errors.push("Invalid Credit Card Number");
      }
    }
    
    // Validation: Only allow users named "Bob" to submit.
    if (theForm.fullName.value !== "Bob") {
      isValid = false;
      errors.push("Your name is not Bob");
    }
    
    // If any validation failed, prevent submission, display errors, and return false.
    if (!isValid) {
      event.preventDefault();
      showErrors(errors);
      return false;
    }
  }
  
  function togglePaymentDetails(e) {
    // Get a reference to the form. We can access all the named form inputs through the form element.
    const theForm = document.querySelector("#checkoutForm");
    // Also get the credit card container and PayPal container.
    const creditCardContainer = document.getElementById("creditCardNumberContainer");
    const paypalContainer = document.getElementById("paypalUsernameContainer");
  
    // Hide both payment containers.
    creditCardContainer.classList.add("hide");
    paypalContainer.classList.add("hide");
  
    // Disable required attributes for hidden fields so the browser doesn't trigger validation errors.
    theForm.creditCardNumber.required = false;
    theForm.paypalUsername.required = false;
  
    // Show the container based on the selected payment method and re-enable the required attribute.
    if (theForm.paymentMethod.value === "creditCard") {
      creditCardContainer.classList.remove("hide");
      theForm.creditCardNumber.required = true;
    } else if (theForm.paymentMethod.value === "paypal") {
      paypalContainer.classList.remove("hide");
      theForm.paypalUsername.required = true;
    }
  }
  
  // Helper function to display errors.
  function showErrors(errors) {
    const errorEl = document.querySelector(".errors");
    // Wrap each error message in a <p> tag.
    const html = errors.map((error) => `<p>${error}</p>`);
    errorEl.innerHTML = html.join("");
  }
  
  // Attach a change event handler to the paymentMethod input.
  document.querySelector("#paymentMethod").addEventListener("change", togglePaymentDetails);
  
  // Attach the form submit event handler to validate the form.
  document.querySelector("#checkoutForm").addEventListener("submit", validateForm);
  