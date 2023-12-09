document.addEventListener("DOMContentLoaded", function () {
    var ctx = document.getElementById('pieChart').getContext('2d');
    var labels = JSON.parse(document.getElementById('pieChart').getAttribute('data-labels'));
    var data = JSON.parse(document.getElementById('pieChart').getAttribute('data-data'));

    var pieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(255, 205, 86, 0.7)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(255, 205, 86, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            width: 400,
            height: 400,
        }
    });
});
