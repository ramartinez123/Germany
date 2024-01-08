
const colors = ['#131a09','#293614','#4e6b21', '#719c30', '#67823a', '#99c255','#131a09',
'#293614', '#4e6b21','#719c30','#67823a','#99c255', '#131a09','#293614', '#4e6b21','#719c30'];
const colorsb = ['white'];
const graph = document.querySelector("#grafica");

const data_=[] 
const label_= [] 
arrpopulation.forEach(element => data_.push(element[3]))
arrpopulation.forEach(element => label_.push(element[0]))
console.log(data_,label_)
   
const data = {
        labels: label_,
        datasets: [{
            data: data_,
            backgroundColor: colors,
            borderColor: colorsb
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

const data_2=[] 
const label_2= [] 
arrpopulation.forEach(element => data_2.push(element[2]))
arrpopulation.forEach(element => label_2.push(element[0]))
console.log(data_2,label_2)
   
const data2 = {

        labels: label_2,
        datasets: [{
            data: data_2,
            backgroundColor: colors,
            borderColor: colorsb
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


