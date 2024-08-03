    const colors3 =  [
        '#003300', // Verde muy oscuro
        '#004d00', // Verde oscuro
        '#006600', // Verde fuerte
        '#008000', // Verde
        '#009933', // Verde brillante
        '#00cc44', // Verde brillante más claro
        '#00e64d', // Verde claro
        '#33ff77', // Verde lima
        '#003300', // Verde muy oscuro
        '#004d00', // Verde oscuro
        '#006600', // Verde fuerte
        '#008000', // Verde
        '#009933', // Verde brillante
        '#00cc44', // Verde brillante más claro
        '#00e64d', // Verde claro
        '#33ff77', // Verde lima
    ];;
    const colorsb3 = ['white'];
    const graph3 = document.querySelector("#grafica3");


    const data_3=[] 
    const label_3= [] 
    arrunemployment.forEach(element => {
        data_3.push(element[1]);
        label_3.push(element[0]);
    });
    
    const data3 = {

            labels: label_3,
            datasets: [{
                data: data_3,
                backgroundColor: colors3,
                borderColor: 'rgba(0, 0, 0, 0.1)',
                borderWidth: 1,
                hoverBackgroundColor: 'rgba(0, 123, 255, 0.5)',
                hoverBorderColor: 'rgba(0, 0, 0, 0.1)',
                borderRadius: 5,
                barThickness: 30,
                maxBarThickness: 40
            }]
        };
        const config3 = {
            type: 'bar',
            data: data3,
            options : {
                plugins: {
                    title: {
                        display: true,
                        text: 'Unemployment Rate',
                        font: {
                            size: 18 // Tamaño de la fuente del título
                        },
                        color: '#000', // Color del título
                        padding: {
                            top: 10,
                            bottom: 30
                        }
                    },
                    legend: {
                        display: false
                    }
                },
  
                
            }

        };

    new Chart(graph3, config3);