/* Ligne qui enlève la partie de l'url ajoutée par les ancres lors du clic sur la sidebar */
history.replaceState({}, '', window.location.href.substring(0, window.location.href.indexOf('#')))

/* Menu onglet dans la sidebar contact-reco */
const tabs = document.querySelectorAll(".tabs");
const content = document.querySelectorAll(".content")
let index = 0

tabs.forEach(tab => {
    tab.addEventListener('click', () => {

        /* Ajoute la classe active à l'onglet seulement si ce dernier ne contient pas la class active */
        if(tab.classList.contains('active')) {
            return;
        } else {
            tab.classList.add('active')
        }

        index = tab.getAttribute('data-displayed')

        /* Enlève la classe active pour les onglets sur lesquels nous n'avons pas cliqué */
        for(let i = 0; i < tabs.length; i++) {
            if(tabs[i].getAttribute('data-displayed') != index) {
                tabs[i].classList.remove('active')
            }
        }

        for(let j = 0; j < content.length; j++) {
            if(content[j].getAttribute('data-displayed') === index) {
                content[j].classList.add('activeContent')
            } else {
                content[j].classList.remove('activeContent')
            }
        }

    });
});

/* Met en place un scroll dynamique quand on clique sur les liens de la sidebar menu */
$(document).ready(function () {

    $('.js-scrollTo').on('click', function() {
      var page = $(this).attr('href'); // Page cible
      var speed = 750; // Durée de l'animation (en ms)

      $('html, body').animate({
         scrollTop: $(page).offset().top
      }, speed);
      return false;
    });

    /* Bouton d'activation de la sidebar en mode mobile / tablette */
    $('button#trigger-sidebar-menu, .js-scrollTo').on('click', function () {
        $('#sidebar').toggleClass('sidebar-menu-activated')
    })

   $('button.btn-open-sidebar-contact, button.btn-open-sidebar-reco, button.cross').on('click', function() {

       const classValue = $('#sidebar-contact-reco').hasClass('sidebar-contact-reco-activated')

       if (!(classValue)) {
           $('#sidebar-contact-reco').addClass('sidebar-contact-reco-activated')
       } else {
           $('#sidebar-contact-reco').removeClass('sidebar-contact-reco-activated')
       }

       /* Activer la sidebar Contact / Recommendation */
       if ($(this).hasClass('btn-open-sidebar-contact') && !($('#tab-contact').hasClass('active'))) {

        $('#tab-contact').addClass('active'); $('#tab-reco').removeClass('active')
        $('#tab-content-contact').addClass('activeContent'); $('#tab-content-reco').removeClass('activeContent')

        } else if($(this).hasClass('btn-open-sidebar-reco') && !($('#tab-reco').hasClass('active'))) {

            $('#tab-reco').addClass('active'); $('#tab-contact').removeClass('active')
            $('#tab-content-reco').addClass('activeContent'); $('#tab-content-contact').removeClass('activeContent')

        }
        $('div.overlay').css('z-index', 999).css('opacity', 0.5)
        $('html').css('overflow-y', 'hidden')

   })


    $('button.cross, button.btn-dismiss, button.btn-recommend-send, button.btn-contact-send').on('click', function() {

       $('#sidebar-contact-reco').removeClass('sidebar-contact-reco-activated')
       $('div.overlay').css('z-index', -999).css('opacity', 0)
       $('html').css('overflow-y', 'visible')

    });

    // Fonction qui permet de créer un effet de déroulement lorsque qu'on clique sur le bouton "Mes compétences" de la section "Mes compétences et expériences"
    $('button.btn-skills').on('click',function(){
        $(this).toggleClass('btn-modern btn-modern-reverse');
        $('div.display-skills').animate({
            height: 'toggle'
        })

        if ($('div.display-experiences').is(':visible')) {
            $('div.display-experiences').animate({
                height: 'toggle'
            });
            $('button.btn-experiences').toggleClass('btn-modern btn-modern-reverse');
        }
        if ($('div.display-studies').is(':visible')) {
            $('div.display-studies').animate({
                height: 'toggle'
            });
            $('button.btn-studies').toggleClass('btn-modern btn-modern-reverse');
        }
    });

    // Fonction qui permet de créer un effet de déroulement lorsque qu'on cliquesur le bouton "Mes expériences" de la section "Mes compétences et expériences"
    $('button.btn-experiences').on('click',function(){
        $(this).toggleClass('btn-modern btn-modern-reverse');
        $('div.display-experiences').animate({
            height: 'toggle'
        });

        if ($('div.display-skills').is(':visible')) {
            $('div.display-skills').animate({
                height: 'toggle'
            });
            $('button.btn-skills').toggleClass('btn-modern btn-modern-reverse');
        }
        if ($('div.display-studies').is(':visible')) {
            $('div.display-studies').animate({
                height: 'toggle'
            });
            $('button.btn-studies').toggleClass('btn-modern btn-modern-reverse');
        }
    });

    // Fonction qui permet de créer un effet de déroulement lorsque qu'on cliquesur le bouton "Ma formation" de la section "Mes compétences et expériences"
    $('button.btn-studies').on('click',function(){
        $(this).toggleClass('btn-modern btn-modern-reverse');
        $('div.display-studies').animate({
            height: 'toggle'
        });

        if ($('div.display-experiences').is(':visible')) {
            $('div.display-experiences').animate({
                height: 'toggle'
            });
            $('button.btn-experiences').toggleClass('btn-modern btn-modern-reverse');
        }
        if ($('div.display-skills').is(':visible')) {
            $('div.display-skills').animate({
                height: 'toggle'
            });
            $('button.btn-skills').toggleClass('btn-modern btn-modern-reverse');
        }
    });

    /* Animation progress-bar */
    $(".progress-bar").css("width", "0px");
    $(function() {
      $(".progress-bar").each(function() {
         var finalWidth = parseInt($(this).attr("data-width"));
         $(this).css("width", "0px").animate({width: finalWidth+"%"}, 500);
      });
    });

    /* Défilement automatique des projets sur la page principale */
    setInterval(function () {
        var newIndex;

        $('.project').each(function() {
            if ($(this).hasClass('activeProject')) {
                $(this).removeClass('activeProject')

                newIndex = parseInt($(this).attr('data-project-index')) + 1

                if (newIndex === parseInt($('.project').length) + 1) {
                    return newIndex = 1
                }
                else {
                    return newIndex
                }
            }
        });

        $('.project').each(function() {

            if (parseInt($(this).attr('data-project-index')) === newIndex) {
                $(this).addClass('activeProject')
            }

        });
    }, 3500);

});

/* Bouton suivant précèdent de la section projet */
// $('button#btn-project-previous').on('click', function() {
//
//     var newIndex;
//
//     $('.project').each(function() {
//         if ($(this).hasClass('activeProject')) {
//             $(this).removeClass('activeProject')
//             newIndex = parseInt($(this).attr('data-project-index')) - 1
//
//             if ((newIndex) === 0) {
//                 return newIndex = $('.project').length
//             } else {
//                 return newIndex
//             }
//         }
//     });
//
//     $('.project').each(function() {
//
//         if (parseInt($(this).attr('data-project-index')) === newIndex) {
//             $(this).addClass('activeProject')
//         }
//
//     });
//
// });
//
// $('button#btn-project-next').on('click', function() {
//
//     var newIndex;
//
//     $('.project').each(function() {
//         if ($(this).hasClass('activeProject')) {
//             $(this).removeClass('activeProject')
//
//             newIndex = parseInt($(this).attr('data-project-index')) + 1
//
//             if (newIndex === parseInt($('.project').length) + 1) {
//                 return newIndex = 1
//             }
//             else {
//                 return newIndex
//             }
//         }
//     });
//
//     $('.project').each(function() {
//
//         if (parseInt($(this).attr('data-project-index')) === newIndex) {
//             $(this).addClass('activeProject')
//         }
//
//     });
//
// });