const endpoint = 'https://flicker.appspot.com/sonics'

fetch(endpoint)
    .then(response => {
        return response.json()
    })
    .then(data => {
        stats = data.stats.map(o => ({
            reading: o.reading,
            date: o.created
        }))
        plotSensorData(stats)
    });

const plotSensorData = (data) => {
    let sortedData = data.sort(function(a, b) {
        aDate = new Date(a.date)
        bDate = new Date(b.date)
        // print(a.getTime())
        return aDate.getTime() - bDate.getTime()
    })
    const x = sortedData.map(o => o.date)
    const y = sortedData.map(o => o.reading)
    const blue = '#4891ce'
    const config = {
        type: 'line',
        data: {
            labels: x,
            datasets: [{
                label: 'Ultrasonic',
                fill: false,
                backgroundColor: blue,
                borderColor: blue,
                lineTension: 0,
                data: y,
            }]
        },
        options: {
            responsive: true,
            title: { display: true, text: 'Sensor Readings', fontSize: 18 },
            tooltips: { mode: 'index', intersect: false },
            hover: { mode: 'nearest', intersect: true },
            scales: {
                xAxes: [{
                    display: true,
                    type: 'time',
                    time: {
                        displayFormats: {
                            millisecond: 'MMM DD',
                            second: 'MMM DD',
                            minute: 'MMM DD',
                            hour: 'MMM DD',
                            day: 'MMM DD',
                            week: 'MMM DD',
                            month: 'MMM DD',
                            quarter: 'MMM DD',
                            year: 'MMM DD',
                         }
                    },
                    scaleLabel: { display: true, labelString: 'Date', fontSize: 14, fontStyle: 'bold' }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: { display: true, labelString: 'Reading', fontSize: 14, fontStyle: 'bold' }
                }]
            }
        }
    }
    const canvas = document.getElementById('canvas').getContext('2d')
    new Chart(canvas, config)
}
