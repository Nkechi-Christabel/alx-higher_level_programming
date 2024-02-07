$(function () {
  $.get(
    "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    (data, status) => status && $("DIV#character").text(`${data.name}`)
  );
});
