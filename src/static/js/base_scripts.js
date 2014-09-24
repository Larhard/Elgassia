function main_menu_save() {
    var main_menu_list = $("#main_menu_list");
    var entries = main_menu_list.find(".main_menu_entry_edit");
    var idx = [];
    var title = [];
    var dest_name = [];
    var dest_url = [];
    main_menu_list.find("input[name*='idx']").each(function() {
        idx.push($(this).val())
    });
    main_menu_list.find("input[name*='title']").each(function() {
        title.push($(this).val())
    });
    main_menu_list.find("input[name*='dest_name']").each(function() {
        dest_name.push($(this).val())
    });
    main_menu_list.find("input[name*='dest_url']").each(function() {
        dest_url.push($(this).val())
    });

    $.post("config/save_main_menu/",
        {
            'csrfmiddlewaretoken': csrftoken,
            'idx[]': idx,
            'title[]': title,
            'dest_name[]': dest_name,
            'dest_url[]': dest_url
        },
        function(data) {
            console.log(data);
            if (data['success'] == true) {
                console.log("Successfully saved");
            } else {
                console.log("Something went wrong");
            }
        }
    );
}

function edit_button() {
    var editable_container = $(this).closest(".editable_container");

    editable_container.find(".editable").each(function() {
        $(this).toggle();
    });
}

function simple_edit_button() {
    $(this).toggle();
    var editable_container = $(this).closest(".editable_container");

    editable_container.find(".sortable").each(function() {
        console.log($(this));
        $(this).sortable();
    });
    editable_container.find(".editable").each(function() {
        $(this).toggle();
    });
}

$(document).ready(function() {
    $("#popup_menu_hide_button").click(function() {
        $("#popup_menu_list").slideToggle();
    });

    $("#main_menu_save_button").click(main_menu_save);

    $(".edit_button").each(function() {
        $(this).click(edit_button)
    });
    $(".simple_edit_button").each(function() {
        $(this).click(simple_edit_button)
    });
});