addEventListener("load", () => {
  $('DIV#add_item').click(function () {
    const myList = $('UL.my_list');
    myList.append('<li>Item</li>');
  });

  $('DIV#remove_item').click(function () {
    const myList = $('UL.my_list li:first');
    myList.remove();
  });

  $('DIV#clear_list').click(function () {
    const myList = $('UL.my_list');
    myList.empty();
  });
});
