const ws = new WebSocket("ws://127.0.0.1:8000/ws");

const ctx = document.getElementById("chart").getContext("2d");

const chart = new Chart(ctx, {
    type: "line",
    data: {
        labels: [],
        datasets: [
            {
                label: "Temperature",
                data: [],
                borderWidth: 2
            },
            {
                label: "Moving Avg",
                data: [],
                borderWidth: 2
            }
        ]
    },
    options: {
        animation: false,
        scales: {
            y: {
                beginAtZero: false
            }
        }
    }
});

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);

    // update labels
    chart.data.labels.push("");

    // push values
    chart.data.datasets[0].data.push(data.value);
    chart.data.datasets[1].data.push(data.moving_avg);

    // limit points
    if (chart.data.labels.length > 20) {
        chart.data.labels.shift();
        chart.data.datasets.forEach(ds => ds.data.shift());
    }

    chart.update();

    // alerts
    if (data.alert) {
        const li = document.createElement("li");
        li.textContent = ` ALERT! Value: ${data.value} (Z=${data.z_score})`;
        document.getElementById("alerts").appendChild(li);
    }
};