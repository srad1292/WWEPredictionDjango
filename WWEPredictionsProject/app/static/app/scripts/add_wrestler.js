$(document).ready(function () {

    $("#add_wrestler_button").click(function () {
        $("#view_wrestler_container").hide();
        $("#edit_wrestler_container").hide();
        $("#add_wrestler_container").show();
    });

    $("#edit_wrestler_button").click(function () {
        $("#view_wrestler_container").hide();
        $("#add_wrestler_container").hide();
        $("#edit_wrestler_container").show();
        var select_name = $("#sel1 option:selected").text();
        $('#edit_old_name').html(select_name);
    });


    $("#cancel_new_wrestler_button").click(function () {
        $("#add_wrestler_container").hide();
    });



    $("#cancel_edit_wrestler_button").click(function () {
        $("#edit_wrestler_container").hide();
    });

    $("#view_wrestler_button").click(function () {
        $("#edit_wrestler_container").hide();
        $("#add_wrestler_container").hide();
        $("#view_wrestler_container").show();
    })
});