$('DIV#add_item').click(function () {
  const Items = $('<li>Item</li>');
  $('UL.my_list').append(Items);
});
