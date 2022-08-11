document.addEventListener("DOMContentLoaded", function() {
    // side nav initialization function 
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // date picker initialization function 
    let datepicker = document.querySelectorAll(".datepicker");
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"}
    });

    // select initialization function 
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);
});