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
            dataSrc: "",
            headers: {
                'X-CSRFToken': csrftoken
            }
        },
        columns: [
            {"data": "position"},
            {"data": "name"},
            {"data": "cat.name"},
            {"data": "image"},
            {"data": "stock"},
            {"data": "pvp"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-4],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="'+data+'" class="img-fluid d-block mx-auto" style="width: 20px; height: 20px;">';
                }
            },
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if (data > 0) {
                        return '<span class="badge badge-success">' + data + '</span>'
                    }
                    return '<span class="badge badge-danger">' + data + '</span>'
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '$'+parseFloat(data).toFixed(2);
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/product/update/' + row.id + '/" class="btn btn-outline-warning btn-xs btn-flat"><i class="fa-solid fa-edit" style="color: #000000;"></i></a> ';
                    buttons += '<a href="/erp/product/delete/' + row.id + '/" type="button" class="btn btn-outline-danger btn-xs btn-flat"><i class="fa-solid fa-trash" style="color: #000000;"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
