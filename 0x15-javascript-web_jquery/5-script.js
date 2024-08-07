$('DIV#add_item').click(function () {
  const myList = $('UL.my_list');
  myList.append('<li>Item</li>');
});
