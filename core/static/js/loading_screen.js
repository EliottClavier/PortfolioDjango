$(window).on('load', function() {

    /* Premier setTimeout pour mettre un minimum de temps de chargement sur le site (sinon coupure immédiate et donc effet brouillon))*/
    setTimeout( function () {

        /* On active la scrollbar (desactivée de base) */
        $('*').css('overflow-y', 'visible')

        // On fait dispaitre progressivement le loading screen
        $('#loading-screen').animate({
            opacity: 0,
            display: 'none'
        }, 1000);

        // Puis on l'enlève totalement de la page avec un eduxième setTimeout pour attendre la fin de l'animation
        setTimeout(function () {
            $('#loading-screen').remove()
        }, 1000);
    }, 0)

});