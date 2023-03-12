(function(){
    if(window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src='https://127.0.0.1:8000/static/js/bookmarklet.js?r=' + Math.floor(Math.random()*99999999999999999999);
    }
})();

// O script anterior descobre se o bookmarklet já foi carregado verificando se a variável myBookmarklet está definida.
// Ao fazer isso, evitamos carregá-lo novamente caso o usuário clique no bookmarklet repetidamente.
// Se myBookmarklet não estiver definida, carregamos outro arquivo JavaScript acrescentando um elemento <script> no documento. 
// A tag script carrega o script bookmarklet.js usando um número aleatório como parâmetro para evitar que o arquivo seja carregado do cache do navegador.
// O código propriamente dito do bookmarklet está no arquivo estático bookmarklet.js. 
// Isso lhe permite atualizar o código de seu bookmarklet sem exigir que seus usuários atualizem o marcador que eles adicionaram antes em seus navegadores.

// Melé, Antonio. Aprenda Django 3 com Exemplos. Seção: Implementando um bookmarklet com jQuery
