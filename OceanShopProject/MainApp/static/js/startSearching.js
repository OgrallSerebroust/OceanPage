$("#buttonConfirmSearch").on("click", function() {
    let data = {
        search: $("#inputSearch").val()
    };
    $("#inputSearch").val("");
    $.ajax({
        type: "POST",
        headers: {
            "X-CSRFToken": window.CSRF_TOKEN
        },
        mode: "same-origin",
        url: "search/",
        data: data,
        dataType: "html",
        success: function(data) {
            $("#searchResultsBlock").html(data);
        }
    });
});