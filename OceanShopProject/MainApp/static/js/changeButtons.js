$(".changeButtonPrevious").on("click", function() {
    let product = $(this).data("product");
    let countInput = $("form[data-product='"+product+"']").find("#id_quantity");
    let count = countInput.val().replace(/\s/g, "");
    if(count > 1) count--;
    else if(count > 0) count = .0;
    countInput.val(count);
});

$(".changeButtonNext").on("click", function() {
    let product = $(this).data("product");
    let countInput = $("form[data-product='"+product+"']").find("#id_quantity");
    let count = countInput.val().replace(/\s/g, "");
    count = +count + 1;
    countInput.val("");
    countInput.val(count);
});