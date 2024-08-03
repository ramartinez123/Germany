
const colors4 = ['#e5f5e0', '#c7e9c0', '#a1d99b', '#74c476', '#31a354', '#006d2c'];
const colorsb4 = ['white'];
const graph4 = document.querySelector("#grafica4");
const datasa44=[] 
const labels44= [] 
arrpopulation4.forEach(element => {
    datasa44.push(element[1])
    labels44.push(element[0])
})

const datasa4 = datasa44.filter((x,i) => i!=6)
const labels4 = labels44.filter((x) => x !=="Sum")

const data4 = {
        labels: labels4,
        datasets: [{
            data: datasa4,  
            backgroundColor: colors4
        }]
    };
    const config4 = {
        type: 'pie',
        data: data4,
        options:{
            legend:{
                display: false
            }
        }
    };

new Chart(graph4, config4);


