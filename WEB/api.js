window.apiUrl = 'http://localhost:5000'

window.api = axios.create({
    baseURL: window.apiUrl
})