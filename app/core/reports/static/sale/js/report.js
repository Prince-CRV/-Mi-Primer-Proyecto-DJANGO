$(function () {
    $('input[name="date_range"]').daterangepicker({
        locale: {
            format: 'yyyy-MM-DD',
            applyLabel: '<i class="fa-solid fa-chart-pie"></i> Aplicar',
            cancelLabel: '<i class="fa-solid fa-times"></i> Cancelar',
        }
    });
});