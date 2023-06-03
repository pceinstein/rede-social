(function(){
    var jquery_version = '3.6.3';
    var site_url = 'https://127.0.0.1:8000/';
    var static_url = site_url + 'static/';
    var min_width = 100;
    var min_height = 100;
  
    function bookmarklet(msg) {
        // Carrega o CSS
        var css = jQuery('<link>');
        css.attr({
            rel: 'stylesheet',
            type: 'text/css',
            href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random()*99999999999999999999)
        });
        jQuery('head').append(css);
  
        // Carrega o HTML
        box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>Select an image to bookmark:</h1><div class="images"></div></div>';
        jQuery('body').append(box_html);
    
        // Evento close
        jQuery('#bookmarklet #close').click(function(){
            jQuery('#bookmarklet').remove();
        });

        // Encontra e exibe as imagens
        jQuery.each(jQuery('img[src$="jpg"]'), function(index, image) {
            if (jQuery(image).width() >= min_width && jQuery(image).height() >= min_height){
                image_url = jQuery(image).attr('src');
                jQuery('#bookmarklet .images').append('<a href="#"><img src="'+
                image_url +'" /></a>');
            }
        });
  
        // Quando uma imagem for selecionada, acessa seu URL
        jQuery('#bookmarklet .images a').click(function(e){
            selected_image = jQuery(this).children('img').attr('src');
            // Oculta o bookmarklet
            jQuery('#bookmarklet').hide();
            // Abre uma nova janela para submeter a imagem
            window.open(site_url +'images/create/?url='
                        + encodeURIComponent(selected_image)
                        + '&title='
                        + encodeURIComponent(jQuery('title').text()),
                        '_blank');
        });
  
    };
  
    // Verifica se a jQuery está carregada
    if(typeof window.jQuery != 'undefined') {
        bookmarklet();
    } else {
        // Verifica se há conflitos
        var conflict = typeof window.$ != 'undefined';
        // Cria o script e aponta para a API do Google
        var script = document.createElement('script');
        script.src = '//ajax.googleapis.com/ajax/libs/jquery/' +
            jquery_version + '/jquery.min.js';
        // Adiciona o script no 'head' para processamento
        document.head.appendChild(script);
        // Determina uma forma de esperar até que o script seja carregado
        var attempts = 15;
        (function(){
            // Verifica novamente se a jQuery está indefinida
            if(typeof window.jQuery == 'undefined') {
                if(--attempts > 0) {
                    // Chama a si mesmo em alguns milissegundos
                    window.setTimeout(arguments.callee, 250)
                } else {
                    // Excesso de tentativas para carregar, envia um erro
                    alert('An error occurred while loading jQuery')
                }
            } else {
                bookmarklet();
            }
        })();
    }
})()