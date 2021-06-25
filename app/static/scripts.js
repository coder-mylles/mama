// Business Logic
var totalPriceArray = []; //Only global variable in code
function Order (customSize, cheese) {
  this.customSize = customSize;
  this.crust = 0;
  this.cheese = cheese;
  this.toppings = 150;
  this.flavor = 200;
  this.pizzaPrice = 0;
  this.sidePrice = 100;
}
Order.prototype.pizzaCost = function () {
  if (this.customSize === "Small 10 in.") {
    this.pizzaPrice += 300;
  } else if (this.customSize === "Medium 14 in.") {
    this.pizzaPrice += 550;
  } else if (this.customSize === "Large 18 in.") {
    this.pizzaPrice += 750;
  } else if (this.customSize === "Jumbo 22 in.") {
    this.pizzaPrice += 1200;
  }
  if (this.cheese === "cheese") {
    this.pizzaPrice += 100;
  } else if (this.cheese === "light cheese") {
    this.pizzaPrice += 50;
  } else if (this.cheese === "extra cheese") {
    this.pizzaPrice += 150;
  }
  this.pizzaPrice += this.crust;
  this.pizzaPrice += this.toppings;
  this.pizzaPrice += this.flavor;
  return this.pizzaPrice;
}
Order.prototype.finalCost = function () {
  var cartTotalPrice = 0;
  for (var arrayElement = 0; arrayElement < totalPriceArray.length; arrayElement ++) {
    cartTotalPrice += totalPriceArray[arrayElement];
  }
  return cartTotalPrice;
}
function Address (streetAddress, city, county) {
  this.streetAddress = streetAddress;
  this.city = city;
  this.county = county;
  this.deliveryAddress = (streetAddress + "  " + city + ", " + county);
}
//User Interface Logic
$(document).ready(function(event) {

  $("form#custom-pizza").submit(function(event) {
    event.preventDefault();
    var customSize = $("select#size").val();
    var crust = $("select#crust").val();
    var cheese = $("select#cheese").val();
    var toppings = $("select#toppings").val();
    var flavor = $("select#flavor").val();
    var pizzaDetails = (customSize + " - " + crust + ", " + cheese + ", " + toppings + ", "  + flavor);
    var newPizzaOrder = new Order(customSize, cheese);
    newPizzaOrder.pizzaCost();
    totalPriceArray.push(newPizzaOrder.pizzaPrice);
    $("#pizza-details-dropdown").show();
    $("#final-cost").text(newPizzaOrder.finalCost());
    $("#pizza-details").append("<ul><li>" + pizzaDetails + "</li></ul>");
    $("#size, #crust, #cheese, #toppings, #flavor").val("");
  });
  $("#pizza-details-dropdown").click(function() {
    $("#pizza-details").toggle();
  });
///Checkout Btn
  $("#checkout-btn").click(function() {
    location.reload();
  });
  $("#delivery-btn").click(function() {
    $("#address").show();
  });
    $("form#address-form").submit(function(event) {
    event.preventDefault();
    var streetAddress = $("input#street-add").val();
    var city = $("input#city-add").val();
    var county = $("select#county-select").val();
    var newAddress = new Address(streetAddress, city, county)
    $("#order-content").show();
    $("#landing-content").hide();
    $("#delivery-option").text("DELIVER TO: " + newAddress.deliveryAddress);
  });
});