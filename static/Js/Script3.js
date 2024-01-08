
const colors = ['#67823a', '#a4b489','#dladc4','darkgreen','#a4b489', '#67823a','darkgreen',
'#a4b489',];
const graph = document.querySelector("#grafica");

const datasa=[] 
const labels= [] 
arrpopulation2.forEach(element => datasa.push(element[2]))
arrpopulation2.forEach(element => labels.push(element[0]))
console.log(datasa,labels)
   
const data = {

        labels: labels,
        datasets: [{
            data: datasa,
            backgroundColor: colors
        }]
    };
    const config = {
        type: 'pie',
        data: data,
        options:{
            legend:{
                display: false
            }
        }
        
        
    };

new Chart(graph, config);


const colors2 = ['blue', 'red'];
const graph2 = document.querySelector("#grafica2");

const datasa2=[] 
const labels2= [] 
arrpopulation.forEach(element => datasa2.push(element[2]))
arrpopulation.forEach(element => labels2.push(element[0]))
console.log(datasa2,labels2)
   
const data2 = {

        labels: labels2,
        datasets: [{
            data: datasa2,
            backgroundColor: colors
        }]
    };
    const config2 = {
        type: 'pie',
        data: data2,
        options:{
            legend:{
                display: false
            }
        }
    };

new Chart(graph2, config2);

var canvas = document.getElementById('grafica3');
var heightRatio = 1.5;
canvas.height = grafica3 * heightRatio;
