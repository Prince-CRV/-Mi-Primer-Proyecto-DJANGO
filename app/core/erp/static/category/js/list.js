$(function () {
    $('#data').DataTable({
        //responsive: true,
        scrollX: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "name"},
            {"data": "desc"},
            {"data": "desc"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/category/update/' + row.id + '/" class="btn btn-outline-warning btn-xs btn-flat"><i class="fa-solid fa-edit" style="color: #000000;"></i></a> ';
                    buttons += '<a href="/erp/category/delete/' + row.id + '/" type="button" class="btn btn-outline-danger btn-xs btn-flat"><i class="fa-solid fa-trash" style="color: #000000;"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});