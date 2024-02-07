$(function () {
  $("DIV#add_item").on("click", () => $("UL.my_list").append("<li>Item</li>"));

  $("DIV#remove_item").on("click", () => {
    let listItems = $("UL.my_list").children();
    listItems.last().remove();
  });

  $("DIV#clear_list").on("click", () => $("UL.my_list").empty());
});
