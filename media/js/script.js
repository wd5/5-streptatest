var IndexPageSliders = {
    doctorsCarousel: function(){
        $('#doctors_carousel ul').bxSlider({
            pager: false,
            nextSelector: '#doc_carousel_r',
            prevSelector: '#doc_carousel_l',
            nextText: '',
            prevText: ''
        });
    },
    patientsCarousel: function(){
        $('#patients_carousel ul').bxSlider({
            pager: false,
            nextSelector: '#patient_carousel_r',
            prevSelector: '#patient_carousel_l',
            nextText: '',
            prevText: ''
        });
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

$(function(){
    SwitchSlider();
    IndexPageSliders.doctorsCarousel();
    IndexBoxAnimate();
    ShowFullReview();
    HideFullReview();
    DrugstoresMapChange();
});