$('.more-more').live('click', function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: 'more/',
        data: { 'current_items':$('.reviews-container li.review-item').size() },
        success: function(data){
            $('.reviews-container li.review-item:last').append(data);
        },
        dataType: 'html'
    });
});

$('.form-link').live('click', function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: 'form/',
        success: function(data){
            $('.form-modal').html(data);
            $('.form-modal').show();
        },
        dataType: 'html'
    });
})

$('.review-form').live('submit', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: 'form/',
        data: $(this).serialize(),
        dataType: 'html'
    }).fail(function(data) {
        alert($(data).text())
  });;
})