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
            {"data": "first_name"},
            {"data": "last_name"},
            {"data": "username"},
            {"data": "date_joined"},
            {"data": "image"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="' + row.image + '" class="img-fluid mx-auto d-block" style="width: 20px; height: 20px;">';
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/user/update/' + row.id + '/" class="btn btn-outline-warning btn-xs btn-flat"><i class="fa-solid fa-edit" style="color: #000000;"></i></a> ';
                    buttons += '<a href="/erp/delete/' + row.id + '/" type="button" class="btn btn-outline-danger btn-xs btn-flat"><i class="fa-solid fa-trash" style="color: #000000;"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});