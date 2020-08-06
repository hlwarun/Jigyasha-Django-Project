// Check if cart exists, if not create an EMPTY json object cart
if (localStorage.getItem("cart")==null) {
  var cart = {};
}
// If cart item is present get that item
else {
  cart = JSON.parse(localStorage.getItem('cart'));
}

// Add click event to ADD TO CART button
$(document).on('click', '.arun-cart', function() {
  console.log("clicked");
  var item_id = this.id.toString();
  console.log(item_id);

  // Check if the item with given ID is already present in the cart
  if (cart[item_id] != undefined) {
    // If the item with given ID is already in the cart increase its QUANTITY by 1
    cart[item_id] = cart[item_id] + 1;
  } else {
    // if the item is not already present in the cart make the QUANTITY = 1
    cart[item_id] = 1;
  }
  console.log(cart);
  // We save the cart values to our localStorage named CART so that it won't get reset when we refresh the page
  localStorage.setItem('cart', JSON.stringify(cart));
  // Getting the number of items in the CART and printing it to navbar
  document.getElementById('navbar-cart-items').innerHTML = Object.keys(cart).length;
});
