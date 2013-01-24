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
};

var IndexPageSliders = function(){
    var doctorsCarousel;
    var patientsCarousel;
    var initDoctorsCarousel = function(){
        doctorsCarousel = $('#doctors_carousel ul').bxSlider({
            pager: false,
            nextSelector: '#doc_carousel_r',
            prevSelector: '#doc_carousel_l',
            nextText: '',
            prevText: '',
            onPrevSlide: function(){
                var openedReview = $('.review_full.opened');
                openedReview.hide();
                openedReview.removeClass('opened');
                var targetReview = openedReview.attr('data-review-full');
                $('.review[data-review='+targetReview+']').show();
            },
            onNextSlide: function(){
                var openedReview = $('.review_full.opened');
                openedReview.hide();
                openedReview.removeClass('opened');
                var targetReview = openedReview.attr('data-review-full');
                $('.review[data-review='+targetReview+']').show();
            }
        });
    };
    var initPatientsCarousel = function(){
        patientsCarousel = $('#patients_carousel ul').bxSlider({
            pager: false,
            nextSelector: '#patient_carousel_r',
            prevSelector: '#patient_carousel_l',
            nextText: '',
            prevText: ''
        });
    };
    var patientsLink = $('.index_reviews #patients_link');
    var bindPatientsLink = function(){
        patientsLink.on('click', function(){
            $('#doctors_carousel').hide();
            doctorsCarousel.destroyShow();
            $('#doctors_link').parents('li').removeClass('curr');
            $('#patients_carousel').show();
            patientsLink.off();
            initPatientsCarousel();
            bindDoctorsLink();
            $('#patients_link').parents('li').addClass('curr');
            return false;
        });
    };
    var doctorsLink = $('.index_reviews #doctors_link');
    var bindDoctorsLink = function(){
        doctorsLink.on('click', function(){
            $('#patients_carousel').hide();
            patientsCarousel.destroyShow();
            $('#patients_link').parents('li').removeClass('curr');
            doctorsLink.off();
            $('#doctors_carousel').show();
            initDoctorsCarousel();
            bindPatientsLink();
            $('#doctors_link').parents('li').addClass('curr');
            return false;
        });
    };
    initDoctorsCarousel();
    bindPatientsLink();
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
            var cont = $(this).parents('.review');
            var oldHeight = cont.height();
            var newHeight = fullReview.find('.review_blob').height()+56;
            if (newHeight>oldHeight){
                $(this).parents('.bx-window').height(newHeight);
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
            var cont = $(this).parents('.bx-window');
            var oldHeight = cont.height();
            var newHeight = 303;
            if (newHeight<oldHeight){
                cont.height(newHeight);
            }            
        };
    });
    $('.index_carousel .bx-prev, .index_carousel .bx-next').on('click', function(){
        var cont = $(this).parents('.index_carousel').find('.bx-window');
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

var FancyBox = function(){
    $('.fancybox').fancybox({
        padding:0,
        type : 'inline',
        tpl : {
            closeBtn : '<div class="blob_modal_close"></div>'
        }
    });
}

var ReviewForm = function(){
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
    $('.patients-question-form').live('submit', function(e){
        e.preventDefault();
        var url = $(this).attr('action');
        $.ajax({
            type: 'POST',
            url: url,
            data: $(this).serialize(),
            success: function(data){
                window.location = '/thanks_for_question'
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
    $('.subscribe_form').live('submit', function(e){
        e.preventDefault();
        var url = $(this).attr('action');
        $.ajax({
            type: 'POST',
            url: url,
            data: $(this).serialize(),
            success: function(data){
                window.location = '/thanks_for_subscribe'
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
    $('.patients-school-form').live('submit', function(e){
        e.preventDefault();
        var url = $(this).attr('action');
        $.ajax({
            type: 'POST',
            url: url,
            data: $(this).serialize(),
            success: function(data){
                window.location = '/thanks_school'
            },
            error: function(ts){
                $('.patients_school_form_modal').html(ts.responseText);
            },
            dataType: 'html'
        });
    });
}

$(function(){
    IndexPageSliders();
    IndexBoxAnimate();
    ShowFullReview();
    HideFullReview();
    OrderSwitchProduct.bindLinks();
    OrderForm();
    AsideOrderLink.bindLinks();
    ShowOutReviewFull();
    FancyBox();
    ReviewForm();
    PatientsQuestionForm();
    PatientsSchoolForm();
    MailCheckbox();
    SubscribeForm();
    MoreReviews();
});