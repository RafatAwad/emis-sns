$("#id_school_address__governorate__name ").on('change',function () {
  var url = $("#filterForm").attr("load-district");
  var governorateId = $(this).val();


  $.ajax({
    url: url,
    data: {
      'governorate': governorateId,
    },       

    success: function (data) {
      $("#id_school_address__district__name").html(data);
    }
  });

});

$("#id_governorate ").on('change',function () {
  var url = $("#StudentRegistrationForm").attr("load-schools-entry");
  var governorateId = $(this).val();
  var district = $("#id_district").val();
  var sub_district = $("#id_sub_district").val();
  var village = $("#id_village").val();

  $.ajax({
    url: url,
    data: {
      'governorate': governorateId,
    },    
    data2: {
      'district': district,
    },     
    data3: {
      'sub_district': sub_district,
    },     
    data4: {
      'village': village,
    },     

    success: function (data, data2, data3, data4) {
      $("#id_district").html(data);
      $("#id_sub_district").html(data2);
      $("#id_village").html(data3);
      $("#id_sub_village").html(data4);
    }
  });

});
$("#id_district").on('change',function () {
  var url = $("#StudentRegistrationForm").attr("load-schools-entry");
  var district = $(this).val();
  var sub_district = $("#id_sub_district").val();
  var village = $("#id_village").val();

  $.ajax({
    url: url,
    data: {
      'district': district,
    },    
    data2: {
      'sub_district': sub_district,
    },    
    data3: {
      'village': village,
    },
    success: function (data,data2,data3) {
      $("#id_sub_district").html(data);
      $("#id_village").html(data2);
      $("#id_sub_village").html(data3);
    }
  });

});

$("#id_sub_district").on('change',function () {
  var url = $("#StudentRegistrationForm").attr("load-schools-entry");
  var sub_district = $(this).val();
  var village = $("#id_village").val();

  $.ajax({
    url: url,   
    data: {
      'sub_district': sub_district,
    },
    data2: {
      'village': village,
    },    

    success: function (data,data2) {
      $("#id_village").html(data);
      $("#id_sub_village").html(data2);
    }
  });

});

$("#id_village").on('change',function () {
  var url = $("#StudentRegistrationForm").attr("load-schools-entry");
  var village = $("#id_village").val();

  $.ajax({
    url: url,   
    data: {
      'village': village,
    },    

    success: function (data) {
      $("#id_sub_village").html(data);
    }
  });

});

$("#id_sub_village").on('change',function () {
  var url = $("#StudentRegistrationForm").attr("load-schools-entry");
  var sub_village = $("#id_sub_village").val();

  $.ajax({
    url: url,   
    data: {
      'sub_village': sub_village,
    },    

    success: function (data) {
      $("#id_school").html(data);
    }
  });

});
