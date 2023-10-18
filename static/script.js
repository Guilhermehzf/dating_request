document.addEventListener("DOMContentLoaded", function () {
  // Função para atualizar a posição do retângulo do "Não" aleatoriamente
  function atualizarPosicaoNao() {
    var nao = document.getElementById("nao");
    var windowWidth = window.innerWidth;
    var windowHeight = window.innerHeight;
    var maxLeft = windowWidth - nao.offsetWidth;
    var maxTop = windowHeight - nao.offsetHeight;

    var newLeft = Math.floor(Math.random() * maxLeft);
    var newTop = Math.floor(Math.random() * maxTop);

    nao.style.left = newLeft + "px";
    nao.style.top = newTop + "px";
  }

  document.getElementById("nao").addEventListener("click", function(event) {
    event.stopPropagation();
    atualizarPosicaoNao();
    enviarResposta("nao"); // Envia a resposta "nao" para o Flask
  });

  document.getElementById("sim").addEventListener("click", function() {
    enviarResposta("sim"); // Envia a resposta "sim" para o Flask
    window.location.href = "/../dating/index.html";
  });

  function enviarResposta(resposta) {
    fetch('/', {
      method: 'POST',
      body: JSON.stringify({ resposta }),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.text())
      .then(data => {
        // Manipule a resposta do servidor aqui, se necessário.
        console.log(data);
      });
  }
});
