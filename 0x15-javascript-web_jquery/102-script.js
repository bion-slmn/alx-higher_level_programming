$('document').ready(function () {
  const lang = $('INPUT#language_code').val();
  const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
  $.get(url, function (data) {
    $('INPUT#btn_translate').click(function () {
      $('DIV#hello').text(data.hello);
    });
  });
});
