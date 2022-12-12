function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
    
}

function grafico_despesas_anuais(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById('despesasanuais').getContext('2d');
        var cores_despesas_anuais = gera_cor(qtd=12)
        console.log(data.meses)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                datasets: [{
                    label: 'despesas',
                    data: data["valor mensal"],
                    backgroundColor: cores_despesas_anuais[0],
                    borderColor: cores_despesas_anuais[1],
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


    })


    

}

function grafico_receitas_anuais(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById('receitasanuais').getContext('2d');
        var cores_receitas_anuais = gera_cor(qtd=12)
        console.log(data.meses)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                datasets: [{
                    label: 'receitas',
                    data: data["valor mensal"],
                    backgroundColor: cores_receitas_anuais[0],
                    borderColor: cores_receitas_anuais[1],
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


    })


    

}

function receitavsdespesa(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById('receitavsdespesa').getContext('2d');
        var cores_receitas_anuais = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                datasets: [{
                    label: 'despesas anuais',
                    data:data['despesas'],
                    backgroundColor: cores_receitas_anuais[0],
                    borderColor: cores_receitas_anuais[1],
                    borderWidth: 1
                },{
                    label: 'receitas anuais',
                    data:data['receitas'],
                    backgroundColor: cores_receitas_anuais[0],
                    borderColor: cores_receitas_anuais[1],
                    borderWidth: 1
                }]

            }

        });

                
    })


}


function graficos_categoria_despesas(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById('categoriadispesa').getContext('2d');
        var cores = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data['categorias'],
                datasets: [{
                    label: 'despesas por categoria',
                    data:data['valores'],
                    backgroundColor: cores[0],
                    borderColor: cores[1],
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


    })


    

}


function graficos_categoria_receitas(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById('categoriareceita').getContext('2d');
        var cores = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data['categorias'],
                datasets: [{
                    label: 'receitas por categoria',
                    data:data['valores'],
                    backgroundColor: cores[0],
                    borderColor: cores[1],
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


    })
}

function graficos_lucros(url){
    fetch(url, {
        method:"get"
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById('lucros').getContext('2d');
        var cores = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] ,
                datasets: [{
                    label: 'lucros',
                    data:data['lucro'],
                    backgroundColor: cores[0],
                    borderColor: cores[1],
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
})
}