document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Dados fictícios de usuário e senha
    const validUsername = "123";
    const validPassword = "123";

    if (username === validUsername && password === validPassword) {
        alert("Login bem-sucedido!");
        window.location.href = "https://www.google.com";
        // Aqui você pode redirecionar para a página principal do site
        // window.location.href = "pagina-principal.html";
    } else {
        document.getElementById("error").style.display = "block";
    }
});
