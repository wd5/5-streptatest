function getScrollBarWidth () { 
  var inner = document.createElement('p'); 
  inner.style.width = "100%"; 
  inner.style.height = "200px"; 

  var outer = document.createElement('div'); 
  outer.style.position = "absolute"; 
  outer.style.top = "0px"; 
  outer.style.left = "0px"; 
  outer.style.visibility = "hidden"; 
  outer.style.width = "200px"; 
  outer.style.height = "150px"; 
  outer.style.overflow = "hidden"; 
  outer.appendChild (inner); 

  document.body.appendChild (outer); 
  var w1 = inner.offsetWidth; 
  outer.style.overflow = 'scroll'; 
  var w2 = inner.offsetWidth; 
  if (w1 == w2) w2 = outer.clientWidth; 

  document.body.removeChild (outer); 

  return (w1 - w2); 
}; 

var PhoneMask = function(){
    $('.inpt_tel').mask("(999) 999-9999");
}

var MoreReviews = function(){
    var processing;

    $(window).on('scroll', function(){
        if (processing)
            return false;

        if ($(window).scrollTop() >= ($(document).height() - $(window).height())*0.9){
            processing = true; //sets a processing AJAX request flag
            $.ajax({
                type: 'GET',
                url: 'more/',
                data: { 'current_items':$('.reviews_list .review_out_full').size() },
                success: function(data){
                    $('.reviews_list').append(data);
                },
                dataType: 'html'
            });
        }
    });

    $('.more-more').live('click', function(e){
        e.preventDefault();
        $.ajax({
            type: 'GET',
            url: 'more/',
            data: { 'current_items':$('.reviews_list .review_out_full').size() },
            success: function(data){
                $('.reviews_list').append(data);
            },
            dataType: 'html'
        });
    });
};

var addBlocked = function(prefix){
    $('body').addClass('no-scroll');
    var scrollBarWidth = getScrollBarWidth();
    if ($('body').height() > $(window).height()){
        $('body').css('padding-right',scrollBarWidth);
    }
    $('body').prepend('<div class="'+prefix+'_blocked"></div>');
    $('div.'+prefix+'_blocked').css('top', $(window).scrollTop());
    $('div.'+prefix+'_blocked').addClass('blocked')
}

var removeBlocked = function(prefix){
    $('body').removeClass('no-scroll');
    $('div.'+prefix+'_blocked').remove();
    $('body').css('padding-right','');
}

var IndexPageSliders = {
    delControls: function(type){
        if ($('#'+type+'_carousel_l a.bx-prev').size() > 1) {
            $('#'+type+'_carousel_l a.bx-prev:not(:first)').remove();
        };
        if ($('#'+type+'_carousel_r a.bx-next').size() > 1) {
            $('#'+type+'_carousel_r a.bx-next:not(:first)').remove();
        };
    },
    doctorsCarousel: function(){
        $('#doctors_carousel ul').bxSlider({
            pager: false,
            nextSelector: '#doc_carousel_r',
            prevSelector: '#doc_carousel_l',
            nextText: '',
            prevText: ''
        });
        this.delControls('doc');
    },
    patientsCarousel: function(){
        $('#patients_carousel ul').bxSlider({
            pager: false,
            nextSelector: '#patient_carousel_r',
            prevSelector: '#patient_carousel_l',
            nextText: '',
            prevText: ''
        });
        this.delControls('patient');
    }
};

var SwitchSlider = function(){
    $('.index_reviews #patients_link').on('click', function(){
        $('#doctors_carousel').hide();
        $('#doctors_link').parents('li').removeClass('curr');
        $('#patients_carousel').show();
        $('#patients_link').parents('li').addClass('curr');
        IndexPageSliders.patientsCarousel();
        return false;
    });
    $('.index_reviews #doctors_link').on('click', function(){
        $('#patients_carousel').hide();
        $('#patients_link').parents('li').removeClass('curr');
        $('#doctors_carousel').show();
        $('#doctors_link').parents('li').addClass('curr');
        IndexPageSliders.doctorsCarousel();
        return false;
    });
}

var IndexBoxAnimate = function(){
    var ShowBox = function(){
        setTimeout( function(){
            $('.index_box_img_1').css({ 'background': "url('/media/img/box_2.png') no-repeat" });
            setTimeout( function(){
                $('.index_box_img_1').css({ 'background': "url('/media/img/box_3.png') no-repeat" });
            },100);
        },100);
    };
    var ShowRoom = function(){
        setTimeout( function(){
            $('.index_box_img_1').css({ 'background': "url('/media/img/box_2.png') no-repeat" });
            setTimeout( function(){
                $('.index_box_img_1').css({ 'background': "url('/media/img/box_1.png') no-repeat" });
            },100);
        },100);
    };
    $('.index_box_img').hover(ShowBox, ShowRoom);
}

var ShowFullReview = function(){
    $('.review_more').on('click', function(){
        var targetReview = $(this).parents('.review').attr('data-review');
        $(this).parents('.review').hide();
        var fullReview = $('.review[data-review-full='+targetReview+']')
        fullReview.addClass('opened');
        fullReview.show();
        if($(this).hasClass('more_index')){
            var cont = $(this).parents('.bx-viewport');
            var oldHeight = cont.height();
            var newHeight = fullReview.find('.review_blob').height()+26;
            if (newHeight>oldHeight){
                cont.height(newHeight);
            }            
        };
    });
}

var HideFullReview = function(){
    $('.blob_close').on('click', function(){
        var targetReview = $(this).parents('.review').attr('data-review-full');
        var review = $('.review[data-review='+targetReview+']');
        $(this).parents('.review').removeClass('opened');
        $(this).parents('.review').hide();
        review.show();
        if($(this).hasClass('close_review_index')){
            var cont = $(this).parents('.bx-viewport');
            var oldHeight = cont.height();
            var newHeight = 303;
            if (newHeight<oldHeight){
                cont.height(newHeight);
            }            
        };
    });
    $('.index_carousel .bx-prev, .index_carousel .bx-next').on('click', function(){
        var cont = $(this).parents('.index_carousel').find('.bx-viewport');
        var oldHeight = cont.height();
        var newHeight = 303;
        if (newHeight<oldHeight){
            cont.height(newHeight);
        }
    });
}

var OrderSwitchProduct = {
    bindLinks: function(){
        $('.5_link').on('click', function(){
            OrderSwitchProduct.show5();
        });
        $('.20_link').on('click', function(){
            OrderSwitchProduct.show20();
        });
        $('.carousel_l, .carousel_r').on('click', function(){
            if ($(this).hasClass('5-link-c')) {
                OrderSwitchProduct.show5();
            } else {
                OrderSwitchProduct.show20();
            };
        });
    },
    show5: function(){
        $('.20_link').removeClass('curr');
        $('.5_link').addClass('curr');
        $('.20_input').attr('checked', false);
        $('.5_input').attr('checked', true);
        $('.20_elem').hide();
        $('.5_elem').show();
        $('.20-image-box').hide();
        $('.5-image-box').show();
        $('.carousel_l, .carousel_r').removeClass('5-link-c');
        $('.carousel_l, .carousel_r').addClass('20-link-c');

        var currentPrice = parseInt($('.buy_calc_price .5_elem').text());
        var currentQnt = parseInt($('.buy_calc_qty .inpt').attr('value'));
        var newSum = currentQnt*currentPrice;
        $('.buy_calc_sum .5_elem .sum').html(newSum);
    },
    show20: function(){
        $('.5_link').removeClass('curr');
        $('.20_link').addClass('curr');
        $('.5_input').attr('checked', false);
        $('.20_input').attr('checked', true);
        $('.5_elem').hide();
        $('.20_elem').show();
        $('.5-image-box').hide();
        $('.20-image-box').show();
        $('.carousel_l, .carousel_r').removeClass('20-link-c');
        $('.carousel_l, .carousel_r').addClass('5-link-c'); 

        var currentPrice = parseInt($('.buy_calc_price .20_elem').text());
        var currentQnt = parseInt($('.buy_calc_qty .inpt').attr('value'));
        var newSum = currentQnt*currentPrice;
        $('.buy_calc_sum .20_elem .sum').html(newSum);
    }
}

var MailCheckbox = function(){
    $('.mail_checkbox').live('click', function(){
        if ($('.mail_inpt').attr('checked')){
            $('.mail_inpt').attr('checked',false);
            $(this).removeClass('mail_checked');
        } else {
            $('.mail_inpt').attr('checked',true);
            $(this).addClass('mail_checked');
        };
    });
}

var OrderForm = function(){ 
    $('.cash_radio').on('click', function(){
        $('.credit_radio').removeClass('buy_form_option_checked');
        $('.cash_radio').addClass('buy_form_option_checked');
        $('.inpt_cash').attr('disabled', false);
        $('.credit_input').attr('checked', false);
        $('.cash_input').attr('checked', true);
    });
    $('.credit_radio').on('click', function(){
        $('.cash_radio').removeClass('buy_form_option_checked');
        $('.credit_radio').addClass('buy_form_option_checked');
        $('.inpt_cash').attr('disabled', true);
        $('.cash_input').attr('checked', false);
        $('.credit_input').attr('checked', true);
    });
    $('.buy_calc_qty_plus').on('click', function(){
        if ($('.buy_calc_sum strong:not(:hidden)').hasClass('20_elem')){
            var currentSumBox = $('.buy_calc_sum .20_elem .sum');
            currentQntBox = $('.buy_calc_qty .inpt');
            var currentPrice = $('.buy_calc_price .20_elem').text();
        } else {
            var currentSumBox = $('.buy_calc_sum .5_elem .sum');
            currentQntBox = $('.buy_calc_qty .inpt');
            var currentPrice = $('.buy_calc_price .5_elem').text();
        }
        var currentPrice = parseInt(currentPrice);
        var currentQnt = parseInt(currentQntBox.attr('value'));
        var newQnt = currentQnt+1;
        var newSum = newQnt*currentPrice;
        currentQntBox.attr('value',newQnt);
        currentSumBox.html(newSum);
    });
    $('.buy_calc_qty_minus').on('click', function(){
        if ($('.buy_calc_sum strong:not(:hidden)').hasClass('20_elem')){
            var currentSumBox = $('.buy_calc_sum .20_elem .sum');
            currentQntBox = $('.buy_calc_qty .inpt');
            var currentPrice = $('.buy_calc_price .20_elem').text();
        } else {
            var currentSumBox = $('.buy_calc_sum .5_elem .sum');
            currentQntBox = $('.buy_calc_qty .inpt');
            var currentPrice = $('.buy_calc_price .5_elem').text();
        }
        var currentPrice = parseInt(currentPrice);
        var currentQnt = parseInt(currentQntBox.attr('value'));
        var newQnt = currentQnt-1;
        if (newQnt < 1) {
            newQnt = 1;
        }
        var newSum = newQnt*currentPrice;
        currentQntBox.attr('value',newQnt);
        currentSumBox.html(newSum);
    });
    $('#quantity_input').on('focus', function(){
        oldOrderQInputValue = $(this).attr('value');
    });
    $('#quantity_input').on('change', function(){
        var newValue = $(this).attr('value');
        if ( !(/^[0-9]+$/.test(newValue)) || newValue < 1) {
            $(this).attr('value',oldOrderQInputValue);
        }        
    });
}

var HeaderContact = function(){
    var modal = $('.contact_map_modal');
    // ymaps.ready(initMap);
    var myMap;
    function InitMap(){     
        myMap = new ymaps.Map ("contact_map", {
            center: [55.76, 37.64],
            zoom: 7,
        });
    }
    var ShowContactModal = function(){
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        var height = modal.height();
        var width = modal.width();
        modal.css('margin-left', -(width/2));
        modal.css('z-index', '99');
        modal.css('top', scroll);
        modal.css('margin-top', (windowHeight-height)/2 );
        addBlocked('contmod');
        modal.show();
        modal.addClass('current-modal');
    };
    $('.header_contacts_lnk').on('click', function(){
        ShowContactModal();
        InitMap();
    });
    $('.blob_modal_close.close_contacts').on('click', function(){
        modal.hide();
        myMap.destroy();
        removeBlocked('contmod');
    });
    $('div.contmod_blocked').live('click', function(){
        modal.hide();
        myMap.destroy();
        removeBlocked('contmod');
    });
}

var ClinicsModal = function(){
    var modal = $('.clinics_modal');
    var ShowClinicsModal = function(){
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        var height = modal.height();
        var width = modal.width();
        modal.css('margin-left', -(width/2));
        modal.css('z-index', '99');
        modal.css('top', scroll);
        modal.css('margin-top', (windowHeight-height)/2 );
        addBlocked('clmod');
        modal.show();
    };
    $('.clinics_modal_link').on('click', function(){
        ShowClinicsModal();
    });
    $('.blob_modal_close.close_clinics').on('click', function(){
        modal.hide();
        removeBlocked('clmod');
    });
    $('div.clmod_blocked').live('click', function(){
        modal.hide();
        removeBlocked('clmod');
    });
}

var FriendsModal = function(){
    var modal = $('.friends_modal');
    var ShowFriendsModal = function(){
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        var height = modal.height();
        var width = modal.width();
        modal.css('margin-left', -(width/2));
        modal.css('z-index', '99');
        modal.css('top', scroll);
        modal.css('margin-top', (windowHeight-height)/2 );
        addBlocked('frmod');
        modal.show();
    };
    $('#friends_modal_link').on('click', function(){
        ShowFriendsModal();
    });
    $('.blob_modal_close.close_friends').on('click', function(){
        modal.hide();
        removeBlocked('frmod');
    });
    $('div.frmod_blocked').live('click', function(){
        modal.hide();
        removeBlocked('frmod');
    });
}

var AsideOrderLink = {
    show5: function(){
        $('.5-link-a').addClass('curr');
        $('.20-link-a').removeClass('curr');
        $('.20-box-a').hide();
        $('.5-box-a').show();
        $('.carousel_zs_l, .carousel_zs_r').removeClass('5-link-c');
        $('.carousel_zs_l, .carousel_zs_r').addClass('20-link-c');
        var oldUrl = $('.btn_zs_in a').attr('href');
        $('.btn_zs_in a').attr('href', oldUrl.replace('?chosed_product=2',''));
    },
    show20: function(){
        $('.20-link-a').addClass('curr');
        $('.5-link-a').removeClass('curr');
        $('.5-box-a').hide();
        $('.20-box-a').show();
        $('.carousel_zs_l, .carousel_zs_r').removeClass('20-link-c');
        $('.carousel_zs_l, .carousel_zs_r').addClass('5-link-c');             
        var oldUrl = $('.btn_zs_in a').attr('href');
        $('.btn_zs_in a').attr('href', oldUrl+'?chosed_product=2');
    },
    bindLinks: function(){
        $('.5-link-a').on('click', function(){
            AsideOrderLink.show5();
        });
        $('.20-link-a').on('click', function(){
            AsideOrderLink.show20();
        });
        $('.carousel_zs_l, .carousel_zs_r').on('click', function(){
            if ($(this).hasClass('5-link-c')) {
                AsideOrderLink.show5();
            } else {
                AsideOrderLink.show20();
            };
        });
    },
}

var ShowOutReviewFull = function(){
    $('.review_out .show_review_out_full').live('click', function(){
        var targetReview = $(this).parents('.review_out .review').attr('data-target');
        $('.review_out_full[data-review='+targetReview+']').show();
        $(this).parents('.review_out').hide();
    });
}

var InstructionsModal = function(){
    var modal = $('.instructions_modal');
    var showModal = function(){
        // var windowHeight = document.documentElement.clientHeight;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        var height = modal.height();
        var width = modal.width();
        modal.css('margin-left', -(width/2));
        modal.css('z-index', '99');
        modal.css('top', scroll);
        modal.css('margin-top', (windowHeight-height)/2);
        modal.show()
    }
    $('.res_lnk a').on('click', function(){
        addBlocked('instmod');
        showModal();
    });
    modal.find('.close_instruction').on('click', function(){
        modal.hide();
        removeBlocked('instmod');
    });
    $('div.instmod_blocked').live('click', function(){
        modal.hide();
        removeBlocked('instmod');
    });
}
var TestScr = function(){
    alert('mmm');
}

var ReviewForm = function(){
    var showModal = function(){
        var modal = $('.review_form_modal');
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        var height = modal.height();
        var width = modal.width();
        modal.css('margin-left', -(width/2));
        modal.css('z-index', '99');
        modal.css('top', scroll);
        modal.css('margin-top', (windowHeight-height)/2);
        modal.show();
        addBlocked('revform');
    }
    $('.form-link').live('click', function(e){
        e.preventDefault();
        var reviewerType = $(this).attr('data-reviewer-type');
        $.ajax({
            type: 'GET',
            url: 'form/',
            data: {'reviewer_type': reviewerType},
            success: function(data){
                $('.review_form_modal').html(data);
                showModal();
            },
            dataType: 'html'
        });
    });

    $('.close_review_form').live('click', function(){
        $('.review_form_modal').hide();
        removeBlocked('revform');
    });
    $('div.revform_blocked').live('click', function(){
        $('.review_form_modal').hide();
        removeBlocked('revform');
    });

    $('#doc_link').live('click', function(){
        $('#doc_radio').prop('checked', true);
        $('#doc_link').parent().addClass('curr');
        $('#patient_radio').prop('checked', false);
        $('#patient_link').parent().removeClass('curr');
    });
    $('#patient_link').live('click', function(){
        $('#patient_radio').prop('checked', true);
        $('#patient_link').parent().addClass('curr');
        $('#doc_radio').prop('checked', false);
        $('#doc_link').parent().removeClass('curr');
    });
}

var PatientsQuestionForm = function(){
    var showModal = function(){
        var modal = $('.patients_question_form_modal');
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        var height = modal.height();
        var width = modal.width();
        modal.css('margin-left', -(width/2));
        modal.css('z-index', '99');
        modal.css('top', scroll);
        modal.css('margin-top', (windowHeight-height)/2);
        addBlocked('patqform');
        modal.show();
    }
    $('.patients-q-form-link').live('click', function(e){
        e.preventDefault();
        var url = $(this).attr('data-url');
        $.ajax({
            type: 'GET',
            url: url,
            success: function(data){
                $('.patients_question_form_modal').html(data);
                showModal();
            },
            dataType: 'html'
        });
    });

    $('.patients_question_modal_close').live('click', function(){
        $('.patients_question_form_modal').hide();
        removeBlocked('patqform');
    });
    $('div.patqform_blocked').live('click', function(){
        $('.patients_question_form_modal').hide();
        removeBlocked('patqform');
    });

    $('.patients-question-form').live('submit', function(e){
        e.preventDefault();
        var url = $(this).attr('action');
        $.ajax({
            type: 'POST',
            url: url,
            data: $(this).serialize(),
            success: function(data){
                window.location = '/thanks'
            },
            error: function(ts){
                var modal = $('.patients_question_form_modal')
                modal.html(ts.responseText);
            },
            dataType: 'html'
        });
    });
}

var SubscribeForm = function(){
    var showModal = function(){
        var modal = $('.subscribe_modal');
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        var height = modal.height();
        var width = modal.width();
        modal.css('margin-left', -(width/2));
        modal.css('z-index', '99');
        modal.css('top', scroll);
        modal.css('margin-top', (windowHeight-height)/2);
        addBlocked('subscr');
        modal.show();
    }

    $('#subscribe_link').live('click', function(e){
        e.preventDefault();
        var url = $(this).attr('data-url');
        $.ajax({
            type: 'GET',
            url: url,
            success: function(data){
                $('.subscribe_modal').html(data);
                showModal();
            },
            dataType: 'html'
        });
    });

    $('.close_subscribe').live('click', function(){
        $('.subscribe_modal').hide();
        removeBlocked('subscr');
    });
    $('div.subscr_blocked').live('click', function(){
        $('.subscribe_modal').hide();
        removeBlocked('subscr');
    });

    $('.subscribe_form').live('submit', function(e){
        e.preventDefault();
        var url = $(this).attr('action');
        $.ajax({
            type: 'POST',
            url: url,
            data: $(this).serialize(),
            success: function(data){
                window.location = '/thanks'
            },
            error: function(ts){
                var modal = $('.subscribe_modal')
                modal.html(ts.responseText);
            },
            dataType: 'html'
        });
    });
}

var PatientsSchoolForm = function(){
    var showModal = function(){
        var modal = $('.patients_school_form_modal');
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        var height = modal.height();
        var width = modal.width();
        modal.css('margin-left', -(width/2));
        modal.css('z-index', '99');
        modal.css('top', scroll);
        modal.css('margin-top', (windowHeight-height)/2);
        addBlocked('patsform');
        modal.show();
    }
    $('.patients-school-form-link').live('click', function(e){
        e.preventDefault();
        var url = $(this).attr('data-url');
        $.ajax({
            type: 'GET',
            url: url,
            success: function(data){
                $('.patients_school_form_modal').html(data);
                showModal();
            },
            dataType: 'html'
        });
    });

    $('.patients_school_modal_close').live('click', function(){
        $('.patients_school_form_modal').hide();
        removeBlocked('patsform');
    });
    $('div.patsform_blocked').live('click', function(){
        $('.patients_school_form_modal').hide();
        removeBlocked('patsform');
    });

    $('.patients-school-form').live('submit', function(e){
        e.preventDefault();
        var url = $(this).attr('action');
        $.ajax({
            type: 'POST',
            url: url,
            data: $(this).serialize(),
            success: function(data){
                window.location = '/thanks'
            },
            error: function(ts){
                $('.patients_school_form_modal').html(ts.responseText);
            },
            dataType: 'html'
        });
    });
}

$(function(){
    SwitchSlider();
    IndexPageSliders.doctorsCarousel();
    IndexBoxAnimate();
    ShowFullReview();
    HideFullReview();
    OrderSwitchProduct.bindLinks();
    OrderForm();
    AsideOrderLink.bindLinks();
    ShowOutReviewFull();
    InstructionsModal();
    ClinicsModal();
    ReviewForm();
    PatientsQuestionForm();
    PatientsSchoolForm();
    MailCheckbox();
    FriendsModal();
    SubscribeForm();
    MoreReviews();
    PhoneMask();
});