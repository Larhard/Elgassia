function getCookie(name) {
    var cookieValue = null;
    //noinspection JSValidateTypes
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function find_first_children(containers, pattern) {
    var result = $();
    while (containers.size()) {
        var k = containers.children();
        containers = k.not(pattern);
        result = result.add(k.filter(pattern));
    }
    return result;
}

function submit_and_redirect(url, data, redirect) {
    data = typeof data != 'undefined' ? data : {};

    data['csrfmiddlewaretoken'] = csrftoken;
    $.post(url,
        data,
        function(data) {
            console.log(data);
            if (data['success'] == true) {
                if (typeof redirect == 'undefined') {
                    location.reload();
                } else {
                    location.href = redirect;
                }
            } else {
                console.log(data['error']);
                alert(data['error']);
            }
        }
    ).fail(
        function() {
            user_save_button.prop("disabled", false);
            alert("Undefined Error");
        }
    );
}
