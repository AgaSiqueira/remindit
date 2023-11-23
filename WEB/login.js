const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");
loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const nome = loginForm.nome.value;
    const senha = loginForm.senha.value;

    payload = {
        "nome": nome,
        "senha": senha
    }
    headers = {
        "Content-Type": "application/json"
    }

    if(!loginForm.checkValidity()) {
        loginForm.reportValidity();
        return;
    }
    

    window.api.post('/login', payload, headers)
    .then(function (response) {
        if(response['status'] == 200) {
            window.localStorage.setItem('tokenLogin', response.data.auth_token);
            window.location.href = "./home.html"
        }
    })
    .catch(function (error) {
        Alpine.store('erroVisivel').toggle();
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