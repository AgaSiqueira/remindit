const cadastroForm = document.getElementById("cadastro-form");
const cadastroButton = document.getElementById("cadastro-form-submit");
const cadastroErrorMsg = document.getElementById("cadastro-error-msg");

cadastroButton.addEventListener("click", (e) => {
    e.preventDefault();
    const nome = cadastroForm.usuario.value;
    const email = cadastroForm.email.value;
    const senha = cadastroForm.senha.value;
    
    var sucessoCadastro = false;

    if(!cadastroForm.checkValidity()) {
        cadastroForm.reportValidity();
        return;
    }

    payload = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    headers = {
        "Content-Type": "application/json"
    }

    window.api.post('/usuario', payload, headers)
    .then(function (response) {
        if(response['status'] == 201) {
            sucessoCadastro=true
        }
    })
    .catch(function (error) {
        Alpine.store('erroVisivel').toggle();
    })
    .finally(function () {
        if(sucessoCadastro==true) {
                payload = {
                    "nome": nome,
                    "senha": senha
                }
                headers = {
                    "Content-Type": "application/json"
            }
            window.api.post('/login', payload, headers)
            .then(function (response) {
                if(response['status'] == 200) {
                    window.localStorage.setItem('tokenLogin', response.data.auth_token);
                    window.location.href = "./home.html"
                }
            })
        }
    })
})

document.addEventListener('alpine:init', () => {
    Alpine.store('erroVisivel', {
        on: false,

        toggle() {
            this.on = true
        }
    })
})