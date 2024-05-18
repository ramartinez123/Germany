function formatNumber() {
    var number = $('.format-number').val();
    var formattedNumber = Number(number).toLocaleString('en-US');
    $('.format-number').val(formattedNumber);

}
