function update_quantity(book_id, url) {
  $.ajax({url: url, dataType: 'json'}).success(
    function(data) {
      $('#book-' + book_id).find('.is-quantity').html(data.quantity);
      $('#book-' + book_id).find('.is-quantity-total').html(data.quantity_total);
      console.log($('#book-' + book_id).find('.is-quantity'));
    }
  );

}

function book_reserve(book_id) {
  if ($('#book-' + book_id).find('.is-quantity').html() <= 0) {
    return false;
  }
  update_quantity(book_id, '/api/book/reserve?id=' + book_id);
  return false;
}

function book_return(book_id) {
  var quanity = $('#book-' + book_id).find('.is-quantity').html();
  var quantity_total = $('#book-' + book_id).find('.is-quantity-total').html();
  if (quanity >= quantity_total) {
    return false;
  }

  update_quantity(book_id, '/api/book/return?id=' + book_id);
  return false;
}
