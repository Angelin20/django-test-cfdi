function calcular_total() {
    var total = 0.00;
    var num_elements = parseInt(document.getElementsByName("invoicedetail_set-TOTAL_FORMS")[0].value, 10);
    for (var i = 0; i < num_elements; i++) {
        total = parseFloat(total) + parseFloat(document.getElementById('id_invoicedetail_set-' + i + '-total').value*document.getElementById('id_invoicedetail_set-' + i + '-quantity').value);
    }
    document.getElementById('id_total').value = Number(total).toFixed(2);
    document.getElementById('id_total_taxes').value = Number(total*1.16).toFixed(2);
}

function item_taxes(i) {
    document.getElementById('id_invoicedetail_set-' + i + '-total').addEventListener('change', function () {
        item=this.id.substring(21, 22);
        tot= this.value;
        document.getElementById('id_invoicedetail_set-' + item + '-total_taxes').value = Number(document.getElementById('id_invoicedetail_set-' + item + '-total').value*document.getElementById('id_invoicedetail_set-' + item + '-quantity').value*1.16).toFixed(2);
        calcular_total();
    });
    document.getElementById('id_invoicedetail_set-' + i + '-quantity').addEventListener('change', function () {
        item=this.id.substring(21, 22);
        tot= this.value;
        document.getElementById('id_invoicedetail_set-' + item + '-total_taxes').value = Number(document.getElementById('id_invoicedetail_set-' + item + '-total').value*document.getElementById('id_invoicedetail_set-' + item + '-quantity').value*1.16).toFixed(2);
        calcular_total();
    });
}

window.addEventListener('load', function () {
    var num_elements = parseInt(document.getElementsByName("invoicedetail_set-TOTAL_FORMS")[0].value, 10);
    for (var i = 0; i < num_elements; i++) {
        item_taxes(i);
    }
    document.getElementById("invoicedetail_set-group").querySelector(".add-row").querySelector("a").addEventListener("click", function() {
        item=this.parentNode.parentNode.querySelector("#id_invoicedetail_set-TOTAL_FORMS").value;
        item_taxes(item-1);
    });
})