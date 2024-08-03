// Configuración del primer gráfico (grafica)
const colors = ['#a8d5ba', '#6aab6b'];
const colorsb = ['white'];
const graph = document.querySelector("#grafica");

// Asignar datos específicos para el primer gráfico
const data_ = [];
const label_ = [];
arrpopulation.forEach(element => {
  data_.push(element[1]); 
  label_.push(element[0]);
});

const data = {
  labels: label_,
  datasets: [{
    data: data_,
    backgroundColor: colors,
    borderColor: colorsb,
    borderWidth: 1
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

// Configuración del segundo gráfico (grafica2)
const colors2 = ['#a8d5ba', '#6aab6b'];
const graph2 = document.querySelector("#grafica2");

// Asignar datos específicos para el segundo gráfico
const data_2 = [];
const label_2 = [];
arrpopulation.forEach(element => {
  data_2.push(element[2]); 
  label_2.push(element[0]);
});

const data2 = {
  labels: label_2,
  datasets: [{
    data: data_2,
    backgroundColor: colors2,
    borderColor: colorsb,
    borderWidth: 1
  }]
};

const config2 = {
  type: 'pie',
  data: data2,
  options: {
    plugins: {
      legend: {
        display: true
      }
    }
  }
};

new Chart(graph2, config2);


