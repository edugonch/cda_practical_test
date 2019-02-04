RFP_FORM = {
  init: function() {
    $("#confirmation-modal-title").html("Are you sure you?");
    $("#confirmation-modal-content").html("This operation is permanent and cannot be reversed.");
    $("#confirmation-modal-yes").on("click", function(event){
      $("#delete_rfp_form").submit();
    });
  },
  form_confirmation: function(form){
    $("#confirmation-modal").modal('show');
    return false;
  }
}