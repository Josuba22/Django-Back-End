document.addEventListener('DOMContentLoaded', function() {
    const posts = document.querySelectorAll('.post');
  
    posts.forEach(post => {
      const lerMaisLink = post.querySelector('a:last-of-type'); // Seleciona o último link (Ler mais) dentro do post
      const conteudoCompleto = post.querySelector('p:nth-child(3)'); // Seleciona o terceiro parágrafo (conteúdo completo)
  
      conteudoCompleto.style.display = 'none'; // Oculta o conteúdo completo por padrão
  
      lerMaisLink.addEventListener('click', function(event) {
        event.preventDefault(); // Impede o comportamento padrão do link
  
        // Alterna a exibição do conteúdo completo
        if (conteudoCompleto.style.display === 'none') {
          conteudoCompleto.style.display = 'block';
          lerMaisLink.textContent = 'Ler menos'; // Altera o texto do link
        } else {
          conteudoCompleto.style.display = 'none';
          lerMaisLink.textContent = 'Ler mais'; // Reverte o texto do link
        }
      });
    });
  });