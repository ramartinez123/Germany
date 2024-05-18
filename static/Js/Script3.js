
const colors4 = ['#131a09','#293614','#4e6b21', '#719c30', '#67823a', '#99c255','#131a09',
'#293614', '#4e6b21','#719c30','#67823a','#99c255', '#131a09','#293614', '#4e6b21','#719c30'];
const colorsb4 = ['white'];
const graph4 = document.querySelector("#grafica4");
const datasa44=[] 
const labels44= [] 
arrpopulation4.forEach(element => datasa44.push(element[1]))
arrpopulation4.forEach(element => labels44.push(element[0]))
const datasa4 = datasa44.filter((x,i) => i!=6)
const labels4 = labels44.filter((x) => x !=="Sum")
console.log(datasa4,labels4)
   
const data4 = {
        labels: labels4,
        datasets: [{
            data: datasa4,  
            backgroundColor: colors
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


