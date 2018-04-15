
// Toggle table 
$("#articles").ready(function () {
    $(".toggler").click(function (e) {
        e.preventDefault();
        $('.' + $(this).attr('data-source')).toggle();
    });
});