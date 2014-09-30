function edit_toggle(button) {
    find_first_children(button.closest(".editable_container"), ".editable").each(function() {
        $(this).prop("contentEditable", $(this).prop("contentEditable") != "true");
    });
}

function slide_toggle(button) {
    find_first_children(button.closest(".slidable_container"), ".slidable").slideToggle();
}

function toggle_toggle(button) {
    find_first_children(button.closest(".toggleable_container"), ".toggleable").toggle();
}

function sorting_toggle(button) {
    find_first_children(button.closest(".sortable_container"), ".sortable").each(function() {
        if ($(this).hasClass("ui-sortable-disabled")) {
            $(this).sortable("enable")
        } else if ($(this).hasClass("ui-sortable")) {
            $(this).sortable("disable")
        } else {
            $(this).sortable();
        }
    });
}

function href_button(button) {
    location.href = $(this).attr('data-href');
}

$(document).ready(function() {
    $(document).on("click", ".edit_button", function() {edit_toggle($(this))});
    $(document).on("click", ".slide_button", function() {slide_toggle($(this))});
    $(document).on("click", ".toggle_button", function() {toggle_toggle($(this))});
    $(document).on("click", ".sorting_button", function() {sorting_toggle($(this))});
    $(document).on("click", ".href", href_button)
});