let myobject = new Array()
let newIndex
var ctx = document.getElementById('myChart');

var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["00:00", "02:00", '04:00', "06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"],

        datasets: [{
            label: 'Häufigkeit von verschiedenen Transportmittel',
            data: [3, 3, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
let y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

function get() {

    fetch("http://localhost:3000/receive")
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log(data);
            if (JSON.stringify(data) != JSON.stringify(myobject[myobject.length - 1])) {
                myobject.push(data)
                manipulateObject()
                myChart.destroy()
                myChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: ["00:00", "02:00", '04:00', "06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"],

                        datasets: [{
                            label: 'Häufigkeit von verschiedenen Transportmittel',
                            data: y,
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)'
                            ],
                            borderColor: [
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgba(255, 159, 64, 1)'
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            } else {
                console.log("no news");
            }



        })
        .catch((err) => {
            console.log(err + " Error")
        })
}

function manipulateObject() {
    let element = myobject[myobject.length - 1];
    console.log(element);
    let time = element.time.split(" ")
    time = time[1].split(":");
    time = time[0]
    if (parseInt(time) % 2 != 0) { time = parseInt(time) - 1 }
    time += ":00"
    let x = myChart.data.labels.indexOf(time)
    y[x] += parseInt(element.car);

}
setInterval(get, 5000);