$(function () {
  $("#btn_translate").click(fetchTranslation);
  $("#language_code").keypress((e) => {
    if (e.keyCode === 13) fetchTranslation();
  });

  function fetchTranslation() {
    let languageCode = $("#language_code").val();
    $.get(
      `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
      (data, status) => status && $("#hello").text(data.hello)
    );
  }
});
