// form visible
// Address Information
$('#address_info_btn').on('click', function(){
  $('.address_info').hide();
  $('.personal_info').show();
});

$('#personal_info_prev_btn').on('click', function(){
  $('.personal_info').hide();
  $('.address_info').show();
});

$('#personal_info_btn').on('click', function(){
  $('.personal_info').hide();
  $('.certificates').show();
});

$('#certificates_prev_btn').on('click', function(){
  $('.certificates').hide();
  $('.personal_info').show();
});

$('#certificates_btn').on('click', function(){
  $('.certificates').hide();
  $('.parent_info').show();
});

$('#parent_info_prev_btn').on('click', function(){
  $('.parent_info').hide();
  $('.certificates').show();
});