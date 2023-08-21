$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            }, // parametros
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
                    var buttons = '<a href="/core/category/update/'+row.id+'/" class="btn btn-outline-warning btn-flat"><i class="fa-solid fa-pen-to-square" style="color: #000000;"></i></a> ';
                    buttons += '<a href="/core/category/delete/'+row.id+'/" class="btn btn-outline-danger btn-flat "><i class="fa-solid fa-trash" style="color: #000000;"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});