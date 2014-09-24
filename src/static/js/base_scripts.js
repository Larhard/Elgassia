function main_menu_save() {
    var main_menu_list = $("#main_menu_list");
    var entries = main_menu_list.children();
    var menu_order = [];
    entries.each(function() {
        menu_order.push($(this).attr('data-id'))
    });
    console.log(menu_order);

    $.post("config/save_main_menu/",
        {
            'csrfmiddlewaretoken': csrftoken,
            'menu_order[]': menu_order
        },
        function(data) {
            if (data['success'] == true) {
                console.log("Successfully saved")
                alert("Successfully saved")
            } else {
                console.log("Something went wrong")
                alert("Something went wrong")
            }
        }
    );
}

$(document).ready(function() {
    $("#popup_menu_hide_button").click(function() {
        $("#popup_menu_list").slideToggle();
    });

    var main_menu_list = $("#main_menu_list");
    main_menu_list.sortable();
    main_menu_list.disableSelection();

    $("#main_menu_save_button").click(main_menu_save);
});