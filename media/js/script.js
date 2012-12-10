var SwitchSlider = function(){
    $('.index_reviews #patients_link').on('click', function(){
        $('#doctors_carousel').hide('slide');
        $('#doctors_link').parents('li').removeClass('curr');
        $('#patients_carousel').show('slide');
        $('#patients_link').parents('li').addClass('curr');
    });
    $('.index_reviews #doctors_link').on('click', function(){
        $('#patients_carousel').hide('slide');
        $('#patients_link').parents('li').removeClass('curr');
        $('#doctors_carousel').show('slide');
        $('#doctors_link').parents('li').addClass('curr');
    });
}

var IndexPageSliders = function(){
    $('#doctors_carousel ul').bxSlider({
        pager: false,
        nextSelector: '#doc_carousel_r',
        prevSelector: '#doc_carousel_l',
        nextText: '',
        prevText: ''
    });
    $('#patients_carousel ul').bxSlider({
        pager: false,
        nextSelector: '#patient_carousel_r',
        prevSelector: '#patient_carousel_l',
        nextText: '',
        prevText: ''
    });
}

var IndexBoxAnimate = function(){
    var ShowBox = function(){
        $('.index_box_img_1').css({ 'background': "url('/media/img/box_2.png') no-repeat" }).delay(1000).css({ 'background': "url('/media/img/box_3.png') no-repeat" });
    }
    var ShowRoom = function(){
        $('.index_box_img_1').css({ 'background': "url('/media/img/box_2.png') no-repeat" }).delay(1000).css({ 'background': "url('/media/img/box_1.png') no-repeat" });
    }
    $('.index_box_img').hover(ShowBox, ShowRoom);
}

$(function(){
    SwitchSlider();
    IndexPageSliders();
    IndexBoxAnimate();
});