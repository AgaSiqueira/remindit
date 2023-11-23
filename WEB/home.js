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
            <h1>${produto.titulo}</h1>
            <p>${produto.descricao}</p>
            <p>Data da próxima parcela:</p> <h2>${produto.renovacao}</h2>
            <p>Valor da próxima parcela:</p> <h3>R$ ${produto.preco.toFixed(2)}</h3>
            <p>Renovação:</p> <h3>${produto.ciclo}</h3>
            <button class="btn-delete" onclick="deletarProduto('${produto.id}')">Deletar <ion-icon name="trash"></ion-icon></button> 
        `;

        teste.appendChild(card);
    });
}

function deletarProduto(id) {
    console.log('Deletando produto com ID:', id);

    window.api.delete('/assinatura/'+id, {headers})
        .then(function (response) {
            if(response['status'] == 200) {
                console.log('Deletado')
            }
        })

    atualizarCards(); // Atualiza os cards na página
}

// Função para atualizar os cards após deletar um produto
function atualizarCards() {
    window.api.get('/assinaturas', {headers})
        .then(function (response) {
        if(response['status'] == 200) {
            window.produtos = [];
            let prod = [];
            for(var i = 0; i<response['data'].length; i++) {
                prod.push({
                    id: response['data'][i][0],
                    titulo: response['data'][i][1],
                    descricao: response['data'][i][2],
                    renovacao: response['data'][i][3],
                    preco: response['data'][i][4],
                    ciclo: cicloParaTexto(response['data'][i][7])
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

window.api.get('/assinaturas', {headers})
.then(function (response) {
    if(response['status'] == 200) {
        window.produtos = [];
        let prod = [];
        for(var i = 0; i<response['data'].length; i++) {
            prod.push({
                id: response['data'][i][0],
                titulo: response['data'][i][1],
                descricao: response['data'][i][2],
                renovacao: response['data'][i][3],
                preco: response['data'][i][4],
                ciclo: cicloParaTexto(response['data'][i][7])
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


