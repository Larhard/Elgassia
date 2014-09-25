function main_menu_save() {
    var main_menu_list = $("#main_menu_list");
    var idx = [];
    var title = [];
    var dest_name = [];
    var dest_url = [];
    var remove = [];
    main_menu_list.find("input[name*='idx']").each(function() {
        idx.push($(this).val());
    });
    main_menu_list.find("input[name*='title']").each(function() {
        title.push($(this).val());
    });
    main_menu_list.find("input[name*='dest_name']").each(function() {
        dest_name.push($(this).val());
    });
    main_menu_list.find("input[name*='dest_url']").each(function() {
        dest_url.push($(this).val());
    });
    main_menu_list.find("input[name*='remove']").each(function() {
        remove.push($(this).prop("checked"));
    });

    submit_and_reload(main_menu_save_url,
        {
            'idx[]': idx,
            'title[]': title,
            'dest_name[]': dest_name,
            'dest_url[]': dest_url,
            'remove[]': remove
        });
}

function toggle_button() {
    find_first_children($(this).closest(".toggleable_container"), ".toggleable").each(function() {
        $(this).toggle();
    });
}

function sorting_button() {
    find_first_children($(this).closest(".sortable_container"), ".sortable").each(function() {
        $(this).sortable();
    });
}

function main_menu_add_entry() {
    $("#main_menu_list").append(
        '<li>' +
        '    <div class="main_menu_entry editable main_menu_entry_edit">' +
        '        <ul class="clean">' +
        '            <li><label>title:<br><input name="title" type="text"></label></li>' +
        '            <li><label>dest_name:<br><input name="dest_name" type="text"></label></li>' +
        '            <li><label>dest_url:<br><input name="dest_url" type="text"></label></li>' +
        '            <li><label>remove: <input type="checkbox" name="removed"></label></li>' +
        '            <input type="hidden" name="idx" value="-1">' +
        '        </ul>' +
        '    </div>' +
        '</li>'
    );
}

function logout_button() {
    submit_and_reload(logout_url)
}

function login_button() {
    var login = $(".login_entry[name*='login']").val();
    var password = $(".login_entry[name*='password']").val();

    submit_and_reload(login_url, {"login": login, "password": password});
}

$(document).ready(function() {
    $("#popup_menu_hide_button").click(function() {
        $("#popup_menu_list").slideToggle();
    });

    $("#main_menu_save_button").click(main_menu_save);

    $(".toggle_button").each(function() {
        $(this).click(toggle_button)
    });
    $(".sorting_button").each(function() {
        $(this).click(sorting_button)
    });
    $("#main_menu_add_entry_button").click(main_menu_add_entry);
    $("#login_button").click(login_button)
    $("input.login_entry").keypress(function(key) {
        if ((key.which && key.which == 13) || (key.keyCode && key.keyCode == 13)) {
            $("#login_button").click();
            return false;
        } else {
            return true;
        }
    });
    $("#logout_button").click(logout_button)
});