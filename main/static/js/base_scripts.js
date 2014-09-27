function slide_button() {
    find_first_children($(this).closest(".slidable_container"), ".slidable").slideToggle();
}

function toggle_button() {
    find_first_children($(this).closest(".toggleable_container"), ".toggleable").toggle();
}

function sorting_button() {
    find_first_children($(this).closest(".sortable_container"), ".sortable").sortable();
}

function button_href() {
    location.href = $(this).attr('data-href');
}

$(document).ready(function() {
    $(document).on("click", ".slide_button", slide_button);
    $(document).on("click", ".toggle_button", toggle_button);
    $(document).on("click", ".sorting_button", sorting_button);
    $(document).on("click", ".href", button_href)
});