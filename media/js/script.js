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
        $('.review[data-review-full='+targetReview+']').show();
    });
}

var HideFullReview = function(){
    $('.blob_close').on('click', function(){
        var targetReview = $(this).parents('.review').attr('data-review-full');
        $(this).parents('.review').hide();
        $('.review[data-review='+targetReview+']').show();
    });
}

var DrugstoresMapChange = function(){
    $('.drugstore-map-link').on('click', function(){
        var targetMap = $(this).attr('data-target-city');
        $('.drugstore-map-link').parents('li.curr').removeClass('curr')
        $('.drugstore-map.curr').hide();
        $(this).parents('li').addClass('curr')
        $('.drugstore-map[data-city='+targetMap+']').show();
        fid_135478862065364205712_1()
    })
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
    }
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
    $('.mail_checkbox').on('click', function(){
        if ($('.mail_inpt').attr('checked')){
            $('.mail_inpt').attr('checked',false);
            $(this).removeClass('mail_checked');
        } else {
            $('.mail_inpt').attr('checked',true);
            $(this).addClass('mail_checked');
        };
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
        var newSum = newQnt*currentPrice;
        currentQntBox.attr('value',newQnt);
        currentSumBox.html(newSum);
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
    $('.review_out .show_review_out_full').on('click', function(){
        var targetReview = $(this).parents('.review_out .review').attr('data-target');
        $('.review_out_full[data-review='+targetReview+']').show();
        $(this).parents('.review_out').hide();
    });
}
var InstructionsModal = function(){
    var modal = $('.instructions_modal');
    var showModal = function(){
        var height = modal.find('img').height();
        var width = modal.find('img').width();
        modal.css('margin-left', -(width/2));
        modal.css('z-index', '10');
        modal.show()
    }
    $('.res_lnk a').on('click', function(){
        showModal();
    });
}

$(function(){
    SwitchSlider();
    IndexPageSliders.doctorsCarousel();
    IndexBoxAnimate();
    ShowFullReview();
    HideFullReview();
    // DrugstoresMapChange();
    OrderSwitchProduct.bindLinks();
    OrderForm();
    AsideOrderLink.bindLinks();
    ShowOutReviewFull();
    InstructionsModal();
});