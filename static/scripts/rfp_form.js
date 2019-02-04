RFP_FORM = {
  init: function() {
    $("#confirmation-modal-title").html("Are you sure you?");
    $("#confirmation-modal-content").html("This operation is permanent and cannot be reversed.");
  },
  form_confirmation: function(event){
    var form = $(event).parent("form");
    $("#confirmation-modal-yes").on("click", function(event){
      form.submit();
    });
    $("#confirmation-modal").modal('show');
    return false;
  }
}