// console.log("working");
if(localStorage.getItem('cart') == null){
    var cart={};
  }
  else{
    cart = JSON.parse(localStorage.getItem('cart'));
    updateCart(cart);
  }
 // updateCart(cart);
  //$('.cart').click(function(){
    $('.divproductId').on('click','button.cart',function(){
    //console.log('clicked');
    var idstr = this.id.toString();
    //console.log(idstr); 
    if(cart[idstr] != undefined){
      qty = cart[idstr][0] + 1;
    }
    else{
      qty = 1;
      name = document.getElementById('name' + idstr).innerHTML;
      price = document.getElementById('price' + idstr).innerHTML;
     
      cart[idstr] = [qty,name,parseInt(price)];
      
    }
    updateCart(cart);
   
  });

//$('#popcart').popover();
//document.getElementById('popcart').setAttribute('data-content','<h5>Cart for your item in my shopping</h5>');

$('#popcart').popover();
updatePopover(cart);
function updatePopover(cart)
{
  var popStr = "";
  popStr = popStr + "<h6 class='font-weight-bold text-muted'>Cart for your item in my shopping </h6>";
  var i = 1;
  for (var item in cart)
  {
    popStr = popStr + "<b>" + i + "</b>.";
    popStr = popStr + document.getElementById('name' + item).innerHTML.slice(0,16) +"<b> - </b>"+ "<b>Qty-</b>" + cart[item][0] +  '<br>';

    i = i + 1;
  }
  popStr = popStr + "<a href='/checkout/'><button class='btn btn-primary' id='checkout'>Checkout</button></a><button class='mx-2 btn btn-primary' onclick='clearCart()' id='clearCart'>Clear Cart</button>"
  document.getElementById('popcart').setAttribute('data-content', popStr);
  $('#popcart').popover('show');
}

function clearCart(){
  cart = JSON.parse (localStorage.getItem('cart'));
  
  for (var item in cart)
  {
    document.getElementById('div' + item).innerHTML = '<button id="'+ item +'" class="btn btn-primary cart m-1 my-2">Add To Cart</button>'
    //updateCart(cart);
  }
  localStorage.clear();
  cart = {};
  updateCart(cart);
}


function updateCart(cart){
  var sum = 0;
  console.log(cart);
  for(var item in cart){
    sum = sum + cart[item][0];
    document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus m-1 my-2'> - </button> <span id='val" + item + "''>" + cart[item][0] + "</span> <button id='plus" + item + "' class='btn btn-primary plus m-1 my-2'> + </button>";
    
  }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = sum;
    updatePopover(cart); 
}



$('.divproductId').on("click","button.minus",function(){
  //console.log("minus clicked");
  a = this.id.slice(14,);
  cart['productId' + a][0] = cart['productId' + a][0] - 1;
  cart['productId' + a][0] = Math.max(0, cart['productId' + a][0])
  document.getElementById('valproductId' + a).innerHTML = cart['productId' + a][0];
  /*
  if(cart['productId' + a][0] == 0){
    document.getElementById('divproductId' + a).innerHTML='<button id = "productId '+ a +'" class="btn btn-primary cart my-2">Add To Cart</button>'
    delete cart['productId' + a];
  }
  else{
    document.getElementById('valproductId' + a).innerHTML = cart['productId' + a][0];
  }
  */
  updateCart(cart);
});


$('.divproductId').on("click","button.plus",function(){
  //console.log("plus clicked");
  a = this.id.slice(13,);
  cart['productId' + a][0] = cart['productId' + a][0] + 1;
  document.getElementById('valproductId' + a).innerHTML = cart['productId' + a][0];
  updateCart(cart);
});
