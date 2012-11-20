$('.more_more').live('click', function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: 'more/',
        data: { 'current_items':$('.reviews_container li.review_item').size() },
        success: function(data){
            $('.reviews_container li.review_item:last').append(data);
        },
        dataType: 'html'
    });
});