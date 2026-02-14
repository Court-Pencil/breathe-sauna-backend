console.log("booking_validation.js loaded");



document.addEventListener('DOMContentLoaded', function(){
    const form = document.getElementById('booking-form');
    console.log("form element:", form);

    if (!form) return;

    const fieldsWrapper = document.getElementById('booking-form-fields');
    const validateUrl = form.dataset.validateUrl;

    async function validateForm() {
        const formData = new FormData(form);
        console.log("validateUrl =", validateUrl)
        

        const response = await fetch(validateUrl,  {
            
            method : 'POST',
            body : formData,
            headers: { "X-Requested-With": "XMLHttpRequest" },
            
            
        });
        


        const data = await response.json();
        if (data.form_html){
            fieldsWrapper.innerHTML = data.form_html;
        }
    }

    form.addEventListener("change", function (e) {
        console.log("changed:", e.target.id);
  if (["id_booking_date", "id_time_slot", "id_number_of_guests", "id_sauna"].includes(e.target.id)) {
    

    validateForm();
  }
});


form.addEventListener("input", function (e) {
  if (e.target.id === "id_number_of_guests") {
    validateForm();
  }
});

})