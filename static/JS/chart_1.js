window.onload = function() {
    const pieChartElement = document.getElementById('pieChart');

    if (pieChartElement && typeof Chart !== 'undefined') {
        const ctx = pieChartElement.getContext('2d');
        var labels = { labels,safe };
        var data = { data,safe };

        const generateColorArray = (baseColor, opacity, length) => 
            Array(length).fill().map(() => `rgba(${baseColor}, ${opacity})`);

        const backgroundColors = generateColorArray('255, 99, 132', 0.7, data.length);
        const borderColors = generateColorArray('255, 99, 132', 1, data.length);

        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: labels,
                datasets: [{
                    data: data,
                    backgroundColor: backgroundColors,
                    borderColor: borderColors,
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                width: 800,
                height: 800,
            }
        });
    } else {
        console.error('Element with id "pieChart" not found or Chart.js not loaded');
    }
};