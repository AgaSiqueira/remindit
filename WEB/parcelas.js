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

window.assinaturas = [];

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

document.addEventListener('alpine:init', () => {
    Alpine.store('assinaturas', {
        assi: [],

        get() {
            this.assi = window.assinaturas
        }
    })

    criarCards()


    

})

// Array de objetos de produtos
window.produtos = [
    {
        id: "assinatura1",
        titulo: "Carregando Assinaturas...",
        descricao: "",
        renovacao: "",
        preco: 0,
        ciclo: ""
    }
    // Adicione mais objetos conforme necessário
];

// Função para criar cards de produtos
function criarCards() {
    const teste = document.getElementById('container');

     document.querySelectorAll('.card').forEach(card => card.remove());

    produtos.forEach((produto, index) => {
        // Crie um novo card usando o design existente
        const card = document.createElement('div');
        card.classList.add('card');
        card.innerHTML = `
            <h1>${produto.assinatura}</h1>
            <p>Data parcela:</p> <h2>${produto.data}</h2>
            <p>Valor:</p> <h3>${produto.valor}</h3>
            <button class="btn-delete" onclick="deletarProduto('${produto.id}')">Deletar</button>
        `;

        teste.appendChild(card);
    });
}

function deletarProduto(id) {
    console.log('Deletando renovacao com ID:', id);

    window.api.delete('/renovacao/'+id, {headers})
        .then(function (response) {
            if(response['status'] == 200) {
                console.log('Deletado')
            }
        })
        
    atualizarCards(); // Atualiza os cards na página
}

// Função para atualizar os cards após deletar um produto
function atualizarCards() {
    window.api.get('/renovacoes', {headers})
        .then(function (response) {
        if(response['status'] == 200) {
            window.produtos = [];
            let prod = [];
            for(var i = 0; i<response['data'].length; i++) {
                prod.push({
                    id: response['data'][i][0],
                    data: response['data'][i][1],
                    valor: response['data'][i][2],
                    assinatura: response['data'][i][6]
                })
            }
            console.log(prod);
            window.produtos = prod;
            criarCards();
            
            window.assinaturas = response['data']

            console.log(window.assinaturas)
        }
})
.catch(function (error) {
    
})
}

window.api.get('/renovacoes', {headers})
        .then(function (response) {
        if(response['status'] == 200) {
            window.produtos = [];
            let prod = [];
            for(var i = 0; i<response['data'].length; i++) {
                prod.push({
                    id: response['data'][i][0],
                    data: response['data'][i][1],
                    valor: response['data'][i][2],
                    assinatura: response['data'][i][6]
                })
            }
            console.log(prod);
            window.produtos = prod;
            criarCards();
            
            window.assinaturas = response['data']

            console.log(window.assinaturas)
        }
})
.catch(function (error) {
    
})
