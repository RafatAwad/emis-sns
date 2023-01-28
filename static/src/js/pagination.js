$(document).on('click', '.page-link' , function () {
  var url = $(this).attr("id");
  var district = $("#districts").val();

  $.ajax({
    type: 'GET',
    url: url+"&school_address__district__name="+district,  
    success: function (data) {
        $("#rafat").html(data);
    }
    });

});
