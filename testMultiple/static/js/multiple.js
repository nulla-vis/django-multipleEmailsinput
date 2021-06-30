$('#demo').multiple_emails();

$('#current_emails').text($('#demo').val());

$('#demo').change( function(){
    $('#current_emails').text($(this).val());
    let eList = document.getElementById('emailList')
    eList.value = document.getElementById('demo').value
    console.log(eList)
});

function isi() {
    $('.emailList').val = document.getElementById('demo').value
    console.log(document.getElementById('demo').value)
}