const colors3 = ['#131a09','#293614','#4e6b21', '#719c30', '#67823a', '#99c255','#131a09',
'#293614', '#4e6b21','#719c30','#67823a','#99c255', '#131a09','#293614', '#4e6b2'];
const colorsb3 = ['white'];
const graph3 = document.querySelector("#grafica3");


const data_3=[] 
const label_3= [] 
arrunemployment.forEach(element => data_3.push(element[1]))
arrunemployment.forEach(element => label_3.push(element[0]))
console.log(data_3,label_3)
   
const data3 = {

        labels: label_3,
        datasets: [{
            data: data_3,
            backgroundColor: colors3,
            borderColor: colorsb3
        }]
    };
    const config3 = {
        type: 'bar',
        data: data3,
        options : {
            title: {
                display: true,
                text: "unemployment rate",
                fontSize: 18,
           },
            legend: {
                display: false,
            }
            
        }

    };

new Chart(graph3, config3);