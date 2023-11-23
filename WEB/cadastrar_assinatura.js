headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "+window.localStorage.getItem('tokenLogin')
}

window.api.get('/usuario', {headers})
.then(function (response) {
    if(response['status'] == 200) {
        document.getElementById('nomeUsuario').innerHTML = (response['data'][1])
    }
})
.catch(function (error) {
    
});

const novaForm = document.getElementById("nova-form");
const novaButton = document.getElementById("nova-form-submit");
novaButton.addEventListener("click", (e) => {
    e.preventDefault();
    const nome = novaForm.nome.value;
    const descricao = novaForm.descricao.value;
    const dataJS = new Date(novaForm.data.value);
    const data = dataFormatada(dataJS);
    // const data = novaForm.data.value;
    const valor = novaForm.valor.value;
    const ciclo = novaForm.ciclo_renovacao.value;

    payload = {
        "nome": nome,
        "descricao": descricao,
        "data": data,
        "valor_proxima": valor,
        "tamanho_ciclo": null,
        "ativo": 1,
        "cd_tipo_ciclo": textoParaCiclo(ciclo),
        "cd_metodo_pagamento": 1
    }
    headers2 = {
        "Authorization": "Bearer "+window.localStorage.getItem('tokenLogin')
    }

    window.api.post('/assinatura', payload, {headers: {
        "Content-Type": "application/json",
        'Authorization': "Bearer "+window.localStorage.getItem('tokenLogin')
      }})
        .then(function (response) {
            if(response['status'] == 201) {
                payload = {
                    "data": data,
                    "valor": valor,
                    "ativo": 1,
                    "cd_assinatura": 1,
                    "cd_notificacao_renovacao": 1
                }
                window.api.post('/renovacao', payload, {headers: {
                    "Content-Type": "application/json",
                    'Authorization': "Bearer "+window.localStorage.getItem('tokenLogin')
                  }})
                  .finally(function (response) {
                    window.location.href = "./home.html"                    
                  })


            }
        })
})

function cicloParaTexto(ciclo) {
    let resul;
    switch(ciclo){
        case 1:
            resul = "Diária"
            break;
        case 2:
            resul = "Semanal"
            break;
        case 3:
            resul = "Mensal"
            break;
        case 4:
            resul = "Trimestral"
            break;
        case 5:
            resul = "Semestral"
            break;
        case 6:
            resul = "Anual"
            break;
        default:
            resul = "Diária"
            break;
    }
    return resul;
}
function textoParaCiclo(ciclo) {
    let resul;
    switch(ciclo){
        case "Diária":
            resul = 1
            break;
        case "Semanal":
            resul = 2
            break;
        case "Mensal":
            resul = 3
            break;
        case "Trimestral":
            resul = 4
            break;
        case "Semestral":
            resul = 5
            break;
        case "Anual":
            resul = 6
            break;
        default:
            resul = 3
            break;
    }
    return resul;
}

function dataFormatada(data){
    var
        dia  = (data.getDate()+1).toString(),
        diaF = (dia.length == 1) ? '0'+dia : dia,
        mes  = (data.getMonth()+1).toString(), //+1 pois no getMonth Janeiro começa com zero.
        mesF = (mes.length == 1) ? '0'+mes : mes,
        anoF = data.getFullYear();
    return diaF+"/"+mesF+"/"+anoF;
}

