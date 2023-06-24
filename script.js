 // Função para atualizar a posição do retângulo do "Não" aleatoriamente
 function atualizarPosicaoNao() {
    var nao = document.getElementById("nao");
    var windowWidth = window.innerWidth;
    var windowHeight = window.innerHeight;
    var maxLeft = windowWidth / nao.offsetWidth +450;
    var maxTop = windowHeight / nao.offsetHeight +450 ;
   
    var newLeft = Math.floor(Math.random() * maxLeft);
    var newTop = Math.floor(Math.random() * maxTop);
  
    nao.style.left = newLeft + "px";
    nao.style.top = newTop + "px";
  }
  
  document.getElementById("nao").addEventListener("click", function(event) {
    event.stopPropagation();
    atualizarPosicaoNao();
  });
  
  
      // Event listener para o clique no retângulo "Sim"
      document.getElementById("sim").addEventListener("click", function() {
        window.location.href = "/html/index2.html";
      });