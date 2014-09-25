function main_menu_save() {
    var main_menu_list = $("#main_menu_list");
    var idx = [];
    var title = [];
    var dest_name = [];
    var dest_url = [];
    var dest_page = [];
    var remove = [];
    main_menu_list.find("input[name*='idx']").each(function() {
        idx.push($(this).val());
    });
    main_menu_list.find("input[name*='title']").each(function() {
        title.push($(this).val());
    });
    main_menu_list.find("input[name*='dest_page']").each(function() {
        dest_page.push($(this).val());
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

    submit_and_redirect($(this).attr("data-url"),
        {
            'idx[]': idx,
            'title[]': title,
            'dest_page[]': dest_page,
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
    submit_and_redirect($(this).attr("data-url"))
}

function login_button() {
    var login = $(".login_entry[name*='login']").val();
    var password = $(".login_entry[name*='password']").val();

    submit_and_redirect($(this).attr("data-url"), {"login": login, "password": password});
}

function page_list_add() {
    $("#page_list").append(
        '<tr>' +
        '    <td class="page_list_entry" data-name="idx">-1</td>' +
        '    <td class="page_list_entry" data-name="title" contenteditable="true">None</td>' +
        '    <td>' +
        '        <label>remove:' +
        '            <input class="page_list_entry" type="checkbox" name="remove"></label>' +
        '    </td>' +
        '</tr>'
    )
}

function page_list_save() {
    var idx = [];
    var title = [];
    var remove = [];

    $(".page_list_entry[data-name*='idx']").each(function() {
        idx.push($(this).html());
    });
    $(".page_list_entry[data-name*='title']").each(function() {
        title.push($(this).html())
    });
    $(".page_list_entry[name*='remove']").each(function() {
        remove.push($(this).prop("checked"));
    });

    submit_and_redirect($(this).attr("data-url"), {
        'idx': idx,
        'title': title,
        'remove': remove
    })
}

function page_editor_save() {
    var idx = $(".page_editor_entry[name*='idx']").val();
    var content = $(".page_editor_entry[name*='content']").val();
    submit_and_redirect($(this).attr("data-url"), {
        'idx': idx,
        'content': content
    }, $(this).attr("data-redirect"))
}

function button_href() {
    location.href = $(this).attr('data-href');
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
    $("#login_button").click(login_button);
    $("input.login_entry").keypress(function(key) {
        if ((key.which && key.which == 13) || (key.keyCode && key.keyCode == 13)) {
            $("#login_button").click();
            return false;
        } else {
            return true;
        }
    });
    $("#logout_button").click(logout_button);
    $("#page_list_add_button").click(page_list_add);
    $("#page_list_save_button").click(page_list_save);
    $("#page_editor_save_button").click(page_editor_save);
    $("button.href").click(button_href);
});