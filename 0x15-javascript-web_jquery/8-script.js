$(function () {
  $.get(
    "https://swapi-api.alx-tools.com/api/films/?format=json",
    (data, status) =>
      status &&
      data.results.forEach((item) =>
        $("UL#list_movies").append(`<li>${item.title}</li>`)
      )
  );
});
