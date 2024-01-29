$(".buttonAddProductToCart").on("click", function() {
    let productId = $(this).data("product");
    let data = {
        product_id: productId,
        quantity: $('form[data-product="'+productId+'"]').find("#id_quantity").val().replace(/\s/g, "")
    };
    $.ajax({
        type: "POST",
        headers: {
            "X-CSRFToken": window.CSRF_TOKEN
        },
        mode: "same-origin",
        url: "cart/add_product_to_cart",
        data: data
    });
});